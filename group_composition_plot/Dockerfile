FROM python:3-slim

RUN pip install dash_bootstrap_components numpy

WORKDIR /script/

ADD interactive_RSE_comp_plot.py .

CMD python interactive_RSE_comp_plot.py
