#!/usr/bin/env python3
import jinja2
import os
import yaml
import argparse
from pathlib import Path


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("contributors", type=Path,
                        help="yml file containing the contributors")
    parser.add_argument("-t", "--template", type=Path, required=True,
                        help="name of template to use")
    parser.add_argument("-o", "--output", type=Path,
                        help="the name of the output file")
    args = parser.parse_args()

    with args.contributors.open('r') as f:
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
        if 'corresponding_author' in author and author['corresponding_author']:
            data['corresponding_author'] = author['email']
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

    contribs = env.get_template(args.template.name).render(data=data)

    if args.output is not None:
        args.output.write_text(contribs)
    else:
        print(contribs)


if __name__ == '__main__':
    main()
