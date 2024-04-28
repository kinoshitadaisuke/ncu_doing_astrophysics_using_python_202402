#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/04/28 19:25:09 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# construction of parser object for argparse
descr  = 'candidate selection by proper motion of stars'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-i', '--input', help='input file name')
parser.add_argument ('-o', '--output', help='output file name')
parser.add_argument ('-a1', type=float, default=0.0, \
                     help='minimum proper motion in RA to plot (default: 0)')
parser.add_argument ('-a2', type=float, default=0.0, \
                     help='maximum proper motion in RA to plot (default: 0)')
parser.add_argument ('-d1', type=float, default=0.0, \
                     help='minimum proper motion in Dec to plot (default: 0)')
parser.add_argument ('-d2', type=float, default=0.0, \
                     help='maximum proper motion in Dec to plot (default: 0)')
parser.add_argument ('-r', '--radius', type=float, default=1.0, \
                     help='radius for candidate selection in mas/yr (default: 1)')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
file_input     = args.input
file_output    = args.output
pmra_min       = args.a1
pmra_max       = args.a2
pmdec_min      = args.d1
pmdec_max      = args.d2
radius         = args.radius

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

# making empty lists
list_pmra_selected  = []
list_pmdec_selected = []

# finding candidate stars
for i in range (len (data_pmra)):
    # rejecting star if pmra is smaller than pmra_min
    if (data_pmra[i] < pmra_min):
        continue
    # rejecting star if pmra is larger than pmra_max
    if (data_pmra[i] > pmra_max):
        continue
    # rejecting star if pmdec is smaller than pmdec_min
    if (data_pmdec[i] < pmdec_min):
        continue
    # rejecting star if pmdec is larger than pmdec_max
    if (data_pmdec[i] > pmdec_max):
        continue
    # appending data to lists
    list_pmra_selected.append (data_pmra[i])
    list_pmdec_selected.append (data_pmdec[i])

# calculating mean proper motion of candidate stars
data_pmra_selected  = numpy.array (list_pmra_selected)
data_pmdec_selected = numpy.array (list_pmdec_selected)
mean_pmra           = numpy.mean (data_pmra_selected)
mean_pmdec          = numpy.mean (data_pmdec_selected)

# printing results
print (f'mean pmra and pmdec of star cluster member candidates:')
print (f'  mean pmra  = {mean_pmra:+6.2f} [mas/yr]')
print (f'  mean pmdec = {mean_pmdec:+6.2f} [mas/yr]')

# opening file for writing
with open (file_output, 'w') as fh:
    # writing header
    header = f'# star ID, RA, Dec, parallax, pmra, pmdec, radial velocity' \
        + f' b mag, g mag, r mag, b-r, b-g, g-r\n'
    fh.write (header)
    # candidate selection
    for i in range (len (data_id)):
        # calculation of distance from mean pmra and pmdec
        offset = numpy.sqrt ( (data_pmra[i] - mean_pmra)**2 \
                              + (data_pmdec[i] - mean_pmdec)**2 )
        # if offset is larger than radius, then skip
        if (offset > radius):
            continue
        # writing candidate information into new file
        record = f"{data_id[i]:19s}" \
            + f" {data_ra[i]:10.6f} {data_dec[i]:+10.6f}" \
            + f" {data_parallax[i]:10.6f}" \
            + f" {data_pmra[i]:10.6f} {data_pmdec[i]:10.6f}" \
            + f" {data_rv[i]:+10.6f}" \
            + f" {data_b[i]:9.6f} {data_g[i]:9.6f} {data_r[i]:9.6f}" \
            + f" {data_br[i]:9.6f} {data_bg[i]:9.6f} {data_gr[i]:9.6f}\n"
        fh.write (record)
