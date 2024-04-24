#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/23 17:30:26 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# construction of parser object for argparse
descr  = 'making HR diagram and superimposing location of main-sequence'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-i', '--input', help='input file name')
parser.add_argument ('-o', '--output', help='output file name')
parser.add_argument ('-m', '--mainsequence', default='ms.data', \
                     help='main-sequence data file (default: ms.data)')
parser.add_argument ('-t', '--title', help='title of plot')
parser.add_argument ('-r', '--resolution', type=float, default=225.0, \
                     help='resolution in DPI (default: 225)')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
file_input     = args.input
file_output    = args.output
file_ms        = args.mainsequence
title          = args.title
resolution_dpi = args.resolution

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
    # reading file
    for line in fh:
        # removing new line at the end of the line
        line = line.strip ()
        # splitting the line
        data = line.split ()
        # fields
        list_id.append (int (data[0]) )
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

# calculation of g-band absolute magnitude
data_g_abs = data_g + 5.0 * numpy.log10 (data_parallax / 1000.0) + 5.0

# making empty lists for storing data
list_ms_colour = []
list_ms_absmag = []

# opening data file
with open (file_ms, 'r') as fh_ms:
    # reading data file line-by-line
    for line in fh_ms:
        # strip
        line = line.strip ()
        # if line is empty, then stop the script
        if (line == ''):
            break
        # if line starts with '#', then skip
        if (line[0] == '#'):
            continue
        # splitting line
        fields = line.split ()
        # spectral type
        sptype = fields[0]
        # effective temperature
        teff = float (fields[1])
        # Gaia (b-r) colour index
        try:
            colour_br = float (fields[11])
        except:
            colour_br = 999.999
        # Gaia g-band absolute magnitude
        try:
            absmag_g = float (fields[13])
        except:
            absmag_g = 999.999
        # appending data to lists
        if ( (colour_br < 100.0) and (absmag_g < 100.0) ):
            list_ms_colour.append (colour_br)
            list_ms_absmag.append (absmag_g)

# making numpy arrays
data_ms_colour = numpy.array (list_ms_colour)
data_ms_absmag = numpy.array (list_ms_absmag)

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# axes
ax.set_xlabel ('(b-r) colour index')
ax.set_ylabel ('g absolute magnitude [mag]')
ax.invert_yaxis ()
ax.grid ()
ax.set_title (title)

# plotting vectors
ax.plot (data_br, data_g_abs, \
         linestyle='None', marker='o', markersize=3, color='blue', \
         zorder=0.2, \
         label='Gaia DR3 stars')
ax.plot (data_ms_colour, data_ms_absmag, \
         linestyle='-', linewidth=10, color='orange', alpha=0.5, \
         zorder=0.1, \
         label='Typical main-sequence stars')
ax.legend ()

# saving file
fig.savefig (file_output, dpi=resolution_dpi, bbox_inches="tight")
