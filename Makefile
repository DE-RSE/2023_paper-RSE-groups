all:	plots paper.pdf

paper.pdf:	paper.tex positionpaper.bib contributors.tex
		latexmk -pdflatex paper.tex

contributors.tex:	contributors.tex.j2 contributors.yml
		python3 contributors.py

plots::
	$(MAKE) -C group_composition_plot
