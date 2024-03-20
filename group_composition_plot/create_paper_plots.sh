./group_composition_plot.py --legend \
--outfile group_composition_plot_the_fantastic_four.pdf \
submissions/2023-12-06/Friedrich_Schiller_University_Jena_2023-12-06_10-43-44.json \
submissions/2023-12-06/Scientific_Software_Center_2023-12-21_13-13-27.json \
submissions/2023-12-06/University_of_Reading_2023-12-11_10-18-14.json \
submissions/2023-12-06/Princeton_University_2023-11-29_18-33-21.json

find submissions/2023-12-06 -type f -name "*.json" -print0 | \
  xargs -0 -P 0 -I{} \
  bash -c 'f=$(basename "{}"); ./group_composition_plot.py --outfile pdf/"${f%.json}.pdf" "{}"'
