#!/usr/bin/env python3
import jinja2
import os
import yaml


with open("contributors.yml") as f:
    data = yaml.safe_load(f)

# Sort by last name and contribution tier
data["authors"] = list(sorted(sorted(data["authors"], key=lambda x: x["lastName"]), key=lambda x: x.get("tier", 2)))

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
