#!/usr/bin/env python3
import sys, argparse
import matplotlib
rc_params = {'text.usetex': True,
         'svg.fonttype': 'none',
         'text.latex.preamble': r'\usepackage{libertine}',
         'font.size': 14,
         'font.family': 'Linux Libertine',
         'mathtext.fontset': 'custom',
         'mathtext.rm': 'libertine',
         'mathtext.it': 'libertine:italic',
         'mathtext.bf': 'libertine:bold'
         }
matplotlib.rcParams.update(rc_params)
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
parser.add_argument('--outfile', default='group_composition_plot.pdf',
                    help="specifies output file name, and by extension also the output format")
parser.add_argument('--legend', action='store_true',
                    help="add a legend")
parser.add_argument('--hide-titles', action='store_true',
                    help="hide the pie plot titles")
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
scaling = 6
iymax = (len(data)+1)//2
fig = plt.figure(figsize=(scaling, scaling/2*iymax))

i = 1
inst_names = {}
for inst, idata in data.items():
    ax = fig.add_subplot(iymax, min(2, len(data)), i)
    ax.pie(idata['activity_weights'], colors=colors, startangle=90, shadow=True, radius=1)
    inst_name = idata['institution_name']
    if 'group_name' in idata:
        inst_name = idata['group_name'] + ", " + inst_name
    if not args['hide_titles']:
        ax.set_title(chr(ord('a')-1+i), y=-0.05)
        inst_names[chr(ord('a')-1+i)] = inst_name
    i += 1

# Shared legend
if args['legend']:
  legend = fig.legend(activity_names, title="Activities",
      loc="upper right", bbox_to_anchor=(1.4, .7), frameon=False)
  #nothing = matplotlib.patches.Rectangle((0,0), 1, 1, fill=False, edgecolor='none', visible=False)
  #legend_inst = plt.legend([nothing]*len(inst_names),
  #                         [i+": "+inst_name for i, inst_name in inst_names.items()],
  #    loc="upper left", bbox_to_anchor=(-1.2, 0.0), frameon=False)
  #plt.gca().add_artist(legend_inst)
  with open(args['outfile'].replace('.pdf', '.labels'), 'w') as f:
      f.write(', '.join([i+": "+inst_name for i, inst_name in inst_names.items()]))

plt.tight_layout()
fig.subplots_adjust(bottom=0)
fig.savefig(args['outfile'], bbox_inches='tight')
# plt.show()
