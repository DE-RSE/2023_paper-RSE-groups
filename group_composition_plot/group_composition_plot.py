#!/usr/bin/env python3
import sys, argparse
import matplotlib.pyplot as plt
import json
from pprint import pprint

def errorexit(msg='internal error', code=1):
    print(msg, file=sys.stderr)
    sys.exit(code)

parser = argparse.ArgumentParser(
    description="Plot activity fields of different institutions", add_help=False)
parser.add_argument('infiles', metavar='infile', nargs="+",
                    help="json files containing compositions of individual institutions")
parser.add_argument('--legend', action='store_true',
                    help="add a legend")
args = vars(parser.parse_args())

data = {}
activity_names = None
for infilename in args['infiles']:
    try:
        infile = open(infilename, 'r')
    except:
        errorexit(f'Error: cannot read file {infilename}')
    try:
        data[infilename] = json.loads(infile.read())
    except:
        errorexit(f'Error: cannot parse data in file {infilename}')
    if activity_names and data[infilename]['activity_names'] != activity_names:
        errorexit(f'Error: inconsitent activity names between {infilename} and others in {data.keys()}')
    else:
        activity_names = data[infilename]['activity_names']

colors = plt.cm.Paired(range(len(activity_names)))

# Mapping activities to colors
activity_to_color = {activity: colors[i] for i, activity in enumerate(activity_names)}

# Creating the joint plot
iymax = (len(data)+1)//2
fig, axs = plt.subplots(iymax, 2, figsize=(16, 8*iymax))

ix = iy = 0
for inst, idata in data.items():
    axs[iy, ix].pie(idata['activity_weights'], colors=colors, startangle=140)
    inst_name = idata['institution_name']
    if 'group_name' in idata:
        inst_name = idata['group_name'] + "\n" + inst_name
    axs[iy, ix].set_title(inst_name, fontsize=20)
    iy += ix
    ix = 1 if ix == 0 else 0

# Shared legend
if args['legend']:
  fig.legend(activity_names, title="Activities", loc="center right", bbox_to_anchor=(1.1, 0.5), fontsize=20)

plt.tight_layout()
fig.savefig("group_composition_plot.pdf", bbox_inches='tight')
# plt.show()
