all:	plots paper.pdf

clean:
		latexmk -c
		rm -f paper.pdf plos.bib norm.bib

paper.pdf:	paper.tex positionpaper.bib contributors.tex plos.bib
		latexmk -pdflatex paper.tex

contributors.tex:	 contributors.yml contributors.tex.j2
		python3 contributors.py $< -t contributors.tex.j2 -o $@

# this step is to convert the input files to proper biblatex files
# so we can turn them into bibtex files later on
norm.bib:	positionpaper.bib bibliography.bib
		biber --tool $^  --output-file $@

plos.bib:	norm.bib
		biber --tool $<  --output-file $@  \
                  --configfile=biberconf.xml \
                  --output-field-replace=location:address,journaltitle:journal

plots::
	$(MAKE) -C group_composition_plot
