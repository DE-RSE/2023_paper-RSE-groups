GOOD = $(wildcard submissions/good/*.json)
GOOD_PLOTS_PDF = $(patsubst submissions/good/%.json,pdf/%.pdf,$(GOOD))
GOOD_PLOTS_TIFF = $(patsubst submissions/good/%.json,tiff/%.tiff,$(GOOD))

all:	group_composition_plot_the_fantastic_four.pdf \
        group_composition_plot_the_fantastic_four.tiff \
        group_composition_plot_all.pdf \
        group_composition_plot_all.tiff \
	$(GOOD_PLOTS_PDF) \
	$(GOOD_PLOTS_TIFF)

group_composition_plot_the_fantastic_four.pdf: \
	submissions/2023-12-06/Friedrich_Schiller_University_Jena_2023-12-06_10-43-44.json \
	submissions/2023-12-06/Scientific_Software_Center_2023-12-21_13-13-27.json \
	submissions/2023-12-06/University_of_Reading_2023-12-11_10-18-14.json \
	submissions/2023-12-06/Princeton_University_2023-11-29_18-33-21.json \
	group_composition_plot.py
	./group_composition_plot.py --legend --outfile $@ $(filter %.json,$^)

group_composition_plot_the_fantastic_four.tiff: \
	submissions/2023-12-06/Friedrich_Schiller_University_Jena_2023-12-06_10-43-44.json \
	submissions/2023-12-06/Scientific_Software_Center_2023-12-21_13-13-27.json \
	submissions/2023-12-06/University_of_Reading_2023-12-11_10-18-14.json \
	submissions/2023-12-06/Princeton_University_2023-11-29_18-33-21.json \
	group_composition_plot.py
	./group_composition_plot.py --legend --outfile $@ $(filter %.json,$^)

group_composition_plot_all.pdf:	$(GOOD)
	./group_composition_plot.py --legend --outfile $@ $^

group_composition_plot_all.tiff: $(GOOD)
	./group_composition_plot.py --legend --outfile $@ $^

pdf/%.pdf: submissions/good/%.json
	mkdir -p pdf
	./group_composition_plot.py --outfile $@ $^

tiff/%.tiff: submissions/good/%.json
	mkdir -p tiff
	./group_composition_plot.py --outfile $@ $^