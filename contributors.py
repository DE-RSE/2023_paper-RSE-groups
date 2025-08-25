#!/usr/bin/env python3
import jinja2
import os
import yaml


def main():

    with open("contributors.yml") as f:
        data = yaml.safe_load(f)

    # Sort by last name and contribution tier
    data["authors"] = list(
        sorted(
            sorted(data["authors"], key=lambda x: x["lastName"]),
            key=lambda x: x.get("tier", 2)))

    # Ensure that we have unique indices for the affiliations
    affiliations = []
    for author in data["authors"]:
        if 'affiliations' in author:
            affiliations.extend(author["affiliations"])
    # make sure affiliations are not duplicated - here by checking
    # for exact name string
    affiliations = list({aff['name']: aff for aff in affiliations}.values())

    # create and add unique index and also a reverse lookup table
    data["affiliations"] = {i + 1: aff for i, aff in enumerate(affiliations)}
    aff_index_by_name = {
        aff['name']: i for i, aff in data["affiliations"].items()}

    # attach index to authors
    for author in data["authors"]:
        if 'affiliations' in author:
            author["affiliations"] = [
                aff_index_by_name[
                    aff['name']] for aff in author["affiliations"]]

    env = jinja2.Environment(
       loader=jinja2.FileSystemLoader(os.getcwd()),
       keep_trailing_newline=True,
    )

    with open("./contributors.tex", "w") as out:
        out.write(env.get_template("contributors.tex.j2").render(data=data))


if __name__ == '__main__':
    main()
