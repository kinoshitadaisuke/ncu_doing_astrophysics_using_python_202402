#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/28 08:21:14 (UT+8) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib
import matplotlib.figure
import matplotlib.backends.backend_agg

# input file name
file_input = 'appy_s15_08_00.data'

# output file name
file_output = 'appy_s15_08_01.png'

# making empty lists for storing data
list_A_x  = []
list_A_y  = []
list_B_x  = []
list_B_y  = []
list_C_x  = []
list_C_y  = []
list_bg_x = []
list_bg_y = []

# opening file for reading
with open (file_input, 'r') as fh:
    # reading file line-by-line
    for line in fh:
        # if line starts with '#', then skip
        if (line[0] == '#'):
            continue
        # reading data
        (x_str, y_str, group) = line.split ()
        # conversion from string into float
        x = float (x_str)
        y = float (y_str)
        # appending data to lists
        if (group == 'A'):
            list_A_x.append (x)
            list_A_y.append (y)
        elif (group == 'B'):
            list_B_x.append (x)
            list_B_y.append (y)
        elif (group == 'C'):
            list_C_x.append (x)
            list_C_y.append (y)
        else:
            list_bg_x.append (x)
            list_bg_y.append (y)

# making numpy arrays
array_A_x  = numpy.array (list_A_x)
array_A_y  = numpy.array (list_A_y)
array_B_x  = numpy.array (list_B_x)
array_B_y  = numpy.array (list_B_y)
array_C_x  = numpy.array (list_C_x)
array_C_y  = numpy.array (list_C_y)
array_bg_x = numpy.array (list_bg_x)
array_bg_y = numpy.array (list_bg_y)

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

# plotting data
ax.plot (array_A_x, array_A_y, \
         linestyle='None', marker='o', markersize=1, color='blue', \
         label='Known A')
ax.plot (array_B_x, array_B_y, \
         linestyle='None', marker='o', markersize=1, color='green', \
         label='Known B')
ax.plot (array_C_x, array_C_y, \
         linestyle='None', marker='o', markersize=1, color='red', \
         label='Known C')
ax.plot (array_bg_x, array_bg_y, \
         linestyle='None', marker='o', markersize=1, color='brown', \
         label='background')

# title
ax.set_title ('Synthetic dataset for classification')

# legend
ax.legend ()

# saving plot into a file
fig.savefig (file_output, dpi=150)
