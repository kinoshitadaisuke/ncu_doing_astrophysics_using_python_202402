#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/04/28 18:45:03 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# construction of parser object for argparse
descr  = 'visualisation of proper motion of stars'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-i', '--input', help='input file name')
parser.add_argument ('-o', '--output', help='output file name')
parser.add_argument ('-r', '--resolution', type=float, default=150.0, \
                     help='resolution in DPI (default: 150)')
parser.add_argument ('-a1', type=float, default=0.0, \
                     help='minimum proper motion in RA to plot (default: 0)')
parser.add_argument ('-a2', type=float, default=0.0, \
                     help='maximum proper motion in RA to plot (default: 0)')
parser.add_argument ('-d1', type=float, default=0.0, \
                     help='minimum proper motion in Dec to plot (default: 0)')
parser.add_argument ('-d2', type=float, default=0.0, \
                     help='maximum proper motion in Dec to plot (default: 0)')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
file_input     = args.input
file_output    = args.output
resolution_dpi = args.resolution
pmra_min       = args.a1
pmra_max       = args.a2
pmdec_min      = args.d1
pmdec_max      = args.d2

# lists to store data
list_id       = []
list_ra       = []
list_dec      = []
list_parallax = []
list_pmra     = []
list_pmdec    = []
list_rv       = []
list_b        = []
list_g        = []
list_r        = []
list_br       = []
list_bg       = []
list_gr       = []

# opening file
with open (file_input, 'r') as fh:
    # reading file line by line
    for line in fh:
        # if the line starts with '#', then skip
        if (line[0] == '#'):
            continue
        # removing new line at the end of the line
        line = line.strip ()
        # splitting the line
        data = line.split ()
        # fields
        list_id.append (data[0])
        list_ra.append (float (data[1]) )
        list_dec.append (float (data[2]) )
        list_parallax.append (float (data[3]) )
        list_pmra.append (float (data[4]) )
        list_pmdec.append (float (data[5]) )
        list_rv.append (float (data[6]) )
        list_b.append (float (data[7]) )
        list_g.append (float (data[8]) )
        list_r.append (float (data[9]) )
        list_br.append (float (data[10]) )
        list_bg.append (float (data[11]) )
        list_gr.append (float (data[12]) )

# making numpy arrays
data_id       = numpy.array (list_id)
data_ra       = numpy.array (list_ra)
data_dec      = numpy.array (list_dec)
data_parallax = numpy.array (list_parallax)
data_pmra     = numpy.array (list_pmra)
data_pmdec    = numpy.array (list_pmdec)
data_rv       = numpy.array (list_rv)
data_b        = numpy.array (list_b)
data_g        = numpy.array (list_g)
data_r        = numpy.array (list_r)
data_br       = numpy.array (list_br)
data_bg       = numpy.array (list_bg)
data_gr       = numpy.array (list_gr)

# clearing lists
list_id.clear ()
list_ra.clear ()
list_dec.clear ()
list_parallax.clear ()
list_pmra.clear ()
list_pmdec.clear ()
list_rv.clear ()
list_b.clear ()
list_g.clear ()
list_r.clear ()
list_br.clear ()
list_bg.clear ()
list_gr.clear ()

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# axes
ax.set_xlabel ('Proper motion in RA [mas/yr]')
ax.set_ylabel ('Proper motion in Dec [mas/yr]')
ax.set_aspect ('equal')
ax.grid ()
ax.set_xlim (pmra_min, pmra_max)
ax.set_ylim (pmdec_min, pmdec_max)

# plotting stars
ax.plot (data_pmra, data_pmdec, \
         linestyle='None', marker='o', markersize=1, color='blue', alpha=0.5, \
         label='Stars in Gaia DR3')
ax.legend (bbox_to_anchor=(1.05, 0.95), loc='upper left')

# saving file
fig.savefig (file_output, dpi=resolution_dpi, bbox_inches="tight")
