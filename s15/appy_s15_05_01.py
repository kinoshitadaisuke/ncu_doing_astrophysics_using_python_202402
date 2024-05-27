#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/27 15:15:31 (UT+8) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib
import matplotlib.figure
import matplotlib.backends.backend_agg

# data file
file_data = 'appy_s15_05_00.data'

# figure file
file_fig = 'appy_s15_05_01.png'

# lists for storing data
list_a_x = []
list_a_y = []
list_a_z = []
list_b_x = []
list_b_y = []
list_b_z = []

# opening data file
with open (file_data, 'r') as fh:
    # reading data line-by-line
    for line in fh:
        # stripping line feed at the end of line
        line = line.strip ()
        # skipping line if the line starts with '#'
        if (line[0] == '#'):
            continue
        # splitting line into fields
        (x_str, y_str, z_str, group) = line.split ()
        # converting string into float
        x = float (x_str)
        y = float (y_str)
        z = float (z_str)
        # appending data to lists
        if (group == 'A'):
            list_a_x.append (x)
            list_a_y.append (y)
            list_a_z.append (z)
        elif (group == 'B'):
            list_b_x.append (x)
            list_b_y.append (y)
            list_b_z.append (z)

# making numpy arrays
array_a_x = numpy.array (list_a_x)
array_a_y = numpy.array (list_a_y)
array_a_z = numpy.array (list_a_z)
array_b_x = numpy.array (list_b_x)
array_b_y = numpy.array (list_b_y)
array_b_z = numpy.array (list_b_z)

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax1    = fig.add_subplot (121)
ax2    = fig.add_subplot (122)

# labels
ax1.set_xlabel ('Feature X [arbitrary unit]')
ax1.set_ylabel ('Feature Y [arbitrary unit]')

# axes
ax1.grid ()

# plotting data
ax1.plot (array_a_x, array_a_y, \
          linestyle='None', marker='o', markersize=3, color='blue', \
          label='Known A')
ax1.plot (array_b_x, array_b_y, \
          linestyle='None', marker='^', markersize=3, color='red', \
          label='Known B')

# title
ax1.set_title ('Synthetic dataset')

# legend
ax1.legend ()

# labels
ax2.set_xlabel ('Feature X [arbitrary unit]')
ax2.set_ylabel ('Feature Z [arbitrary unit]')

# axes
ax2.grid ()

# plotting data
ax2.plot (array_a_x, array_a_z, \
          linestyle='None', marker='o', markersize=3, color='blue', \
          label='Known A')
ax2.plot (array_b_x, array_b_z, \
          linestyle='None', marker='^', markersize=3, color='red', \
          label='Known B')

# title
ax2.set_title ('Synthetic dataset')

# legend
ax2.legend ()

# saving plot into a file
fig.tight_layout ()
fig.savefig (file_fig, dpi=150)
