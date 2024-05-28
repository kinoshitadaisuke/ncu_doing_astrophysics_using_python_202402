#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/28 09:09:16 (UT+8) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib
import matplotlib.figure
import matplotlib.backends.backend_agg

# input file name
file_input = 'appy_s15_08_02.data'

# output file name
file_output = 'appy_s15_08_03.png'

# making an empty list
list_group = []

# opening file for reading
with open (file_input, 'r') as fh:
    # reading file line-by-line
    for line in fh:
        # if line starts with '#', then skip
        if (line[0] == '#'):
            continue
        # reading data
        (x_str, y_str, group_str) = line.split ()
        # appending data to list
        list_group.append (group_str)

# making a set
set_group = set (list_group)

# making an empty 2-D list for storing data
data = []
for i in range (len (set_group)):
    data.append ([])

# opening file for reading
with open (file_input, 'r') as fh:
    # reading file line-by-line
    for line in fh:
        # if line starts with '#', then skip
        if (line[0] == '#'):
            continue
        # reading data
        (x_str, y_str, group_str) = line.split ()
        # conversion from string into float
        x = float (x_str)
        y = float (y_str)
        # conversion from string into integer
        group = int (group_str)
        # appending data to list
        data[group].append ([x, y])

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Feature X [arbitrary unit]')
ax.set_ylabel ('Feature Y [arbitrary unit]')

# axes
ax.grid ()
ax.set_aspect ('equal')

# for each group of data
for i in range (len (data)):
    # re-arrangement of data
    array_data = numpy.array (data[i])
    x, y = array_data.T
    # plotting data
    if (i < len (data) - 1):
        ax.plot (x, y, linestyle='None', marker='o', markersize=1, \
                 label=f'clustering {i}')
    else:
        ax.plot (x, y, linestyle='None', marker='o', markersize=1, \
                 label=f'background')

# title
ax.set_title ('Results of DBSCAN analysis')

# legend
ax.legend ()

# saving plot into a file
fig.savefig (file_output, dpi=150)
