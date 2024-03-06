#!/usr/bin/python3
# author: Frank Löffler <frank.loeffler@uni-jena.de>
# license: CC0

import numpy as np
import matplotlib.pyplot as plt

# preliminary names
names = ["RSE Network",
         "Partner Network",
         "RSE Teaching",
         "RSE Consultation",
         "SW Development",
         "SW Maintenance",
         "RSE Infrastructure",
         "RSE Research",
         "RSE Outreach",
        ]
# some example values
data = np.array([[1, 0.2],
                 [3, 0.6,],
                 [1, 0.1,],
                 [3, 0.2,],
                 [4, 0.4,],
                 [3, 0.3,],
                 [0, 0.8,],
                 [2, 0.6,],
                 [3, 1,],
                ])

fig = plt.figure(figsize=(10,5))

# percentages of the widths of the left and middle section of the plot, with the right
# part being calculated from those (assuming 100% plot width)
widths = [0.2, 0.1]
widths.append(1-sum(widths))
ax_l = fig.add_axes((0,                   0, widths[0], 1))
ax_c = fig.add_axes((widths[0],           0, widths[1], 1))
ax_r = fig.add_axes((widths[0]+widths[1], 0, widths[2], 1))

xstep = 0.1

# eps: small value to ensure that where-clauses do not leave some range un-plotted
# should roughly be half of the smallest step-size you want in x-direction
eps = xstep/2

x =  np.arange(0, 1+eps, xstep)
y = [np.repeat(0, len(x))]
p = [np.repeat(0, len(x))]
ye = [[0, 0],]
ysum = np.sum(data[:,0])
for i in np.arange(len(data)):
  y.append(np.repeat(data[i,0], len(x))/ysum + y[-1])
  p.append(np.repeat(data[i,1], len(x)))
  ye.append([(i+1)/len(data), y[-1][0]])

for i in np.arange(len(data))+1:
  ax_l.fill_between([0,1], [ye[i][0], ye[i][0]], facecolor="none", edgecolor='k')
  ax_l.text(0.05, (ye[i][0]+ye[i-1][0])/2, names[i-1])

  ax_c.fill_between([0,1], ye[i], facecolor="none", edgecolor='k')

  ax_r.fill_between(x, y[i-1], y[i], facecolor="none", edgecolor='k', hatch='/',  where=p[i]>x-eps)
  ax_r.fill_between(x, y[i-1], y[i], facecolor="none", edgecolor='k', hatch='\\', where=p[i]<x+eps)

for ax in [ax_l, ax_c, ax_r]:
  ax.set_xlim(0,1)
  ax.set_ylim(0,1)
  ax.set_xticks([])
  ax.set_yticks([])



plt.savefig("group_composition_plot.pdf")
#plt.show()
