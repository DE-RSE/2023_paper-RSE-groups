import jinja2
import os
import yaml


with open("contributors.yml") as f:
    data = yaml.safe_load(f)

# Ensure that we have unique indices for the affiliations
affiliations = list()
for authors in data["authors"]:
    affiliations.extend(authors.get("affiliations", []))
data["affiliations"] = {aff: i + 1 for i, aff in enumerate(set(affiliations))}
for author in data["authors"]:
    author["affiliations"] = [data["affiliations"][aff] for aff in author.get("affiliations", [])]

env = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.getcwd()),
   keep_trailing_newline=True,
)

with open("./contributors.tex", "w") as out:
    out.write(env.get_template("contributors.tex.j2").render(data=data))
