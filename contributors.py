#!/usr/bin/env python3
import jinja2
import os
import yaml

CORRESPONDING_AUTHOR = "Kempf"

with open("contributors.yml") as f:
    data = yaml.safe_load(f)

# sort list of authors by last name
sorted_authors = sorted(data["authors"], key=lambda a: a["lastName"])
# and move corresponding author to front of the list
idx = None
for i, a in enumerate(sorted_authors):
    if a["lastName"] == CORRESPONDING_AUTHOR:
        idx = i
        break
if idx is not None:
    sorted_authors.insert(0, sorted_authors.pop(idx))
data["authors"] = sorted_authors

# Ensure that we have unique indices for the affiliations
affiliations = list()
for author in data["authors"]:
    if 'affiliations' in author:
        affiliations.extend(author["affiliations"])
data["affiliations"] = {aff: i + 1 for i, aff in enumerate(list(dict.fromkeys(affiliations)))}
for author in data["authors"]:
    if 'affiliations' in author:
        author["affiliations"] = [data["affiliations"][aff] for aff in author["affiliations"]]

env = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.getcwd()),
   keep_trailing_newline=True,
)

with open("./contributors.tex", "w") as out:
    out.write(env.get_template("contributors.tex.j2").render(data=data))
