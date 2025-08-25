all:	plots paper.pdf

clean:
		latexmk -c
		rm paper.pdf

paper.pdf:	paper.tex positionpaper.bib contributors.tex
		latexmk -pdflatex paper.tex

contributors.tex:	 contributors.yml contributors.tex.j2
		python3 contributors.py $< -t contributors.tex.j2 -o $@

plots::
	$(MAKE) -C group_composition_plot
