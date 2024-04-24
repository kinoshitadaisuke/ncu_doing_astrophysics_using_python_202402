#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/23 15:49:15 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# construction of parser object for argparse
descr  = 'selection stars by proper motion'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-i', '--input', help='input file name')
parser.add_argument ('-o', '--output', help='output file name')
parser.add_argument ('-a', '--angle', type=float, default=45.0, \
                     help='angle criterion in deg (default: 45)')
parser.add_argument ('-l', '--length', type=float, default=2.0, \
                     help='length criterion (default: 2.0)')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
file_input       = args.input
file_output      = args.output
criterion_angle  = args.angle
criterion_length = args.length

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
with open (file_input, 'r') as fh_in:
    # reading file
    for line in fh_in:
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

# normalised proper motion vectors
data_pmra_norm  = numpy.array ([])
data_pmdec_norm = numpy.array ([])
data_pm_length  = numpy.array ([])
for i in range (len (data_pmra) ):
    # length of a vector (data_pmra[i], data_pmdec[i])
    length = numpy.sqrt (data_pmra[i]**2 + data_pmdec[i]**2)
    # normalised vector
    pmra_norm  = data_pmra[i] / length
    pmdec_norm = data_pmdec[i] / length
    # appending vector components to numpy arrays
    data_pmra_norm  = numpy.append (data_pmra_norm, pmra_norm)
    data_pmdec_norm = numpy.append (data_pmdec_norm, pmdec_norm)
    data_pm_length  = numpy.append (data_pm_length, length)

# average direction of proper motion
pmra_mean  = numpy.mean (data_pmra_norm)
pmdec_mean = numpy.mean (data_pmdec_norm)
pmra_mean_norm  = pmra_mean / numpy.sqrt (pmra_mean**2 + pmdec_mean**2)
pmdec_mean_norm = pmdec_mean / numpy.sqrt (pmra_mean**2 + pmdec_mean**2)
pm_length_mean = numpy.mean (data_pm_length)

# opening file for writing
with open (file_output, 'w') as fh_out:
    # angle between a proper motion vector and mean proper motion vector
    for i in range ( len (data_pmra) ):
        # angle
        cos_a = data_pmra_norm[i] * pmra_mean_norm \
            + data_pmdec_norm[i] * pmdec_mean_norm
        a = numpy.arccos (cos_a) / numpy.pi * 180.0
        # length of a vector (data_pmra[i], data_pmdec[i])
        length = numpy.sqrt (data_pmra[i]**2 + data_pmdec[i]**2)
        # rejecting stars with proper motions quite different from
        # the average motion of stars
        if ( (a <= criterion_angle) \
             and (length < criterion_length * pm_length_mean) ):
            # writing data into file
            record = f"{data_id[i]:19d}" \
                + f" {data_ra[i]:10.6f} {data_dec[i]:+10.6f}" \
                + f" {data_parallax[i]:10.6f}" \
                + f" {data_pmra[i]:10.6f} {data_pmdec[i]:10.6f}" \
                + f" {data_rv[i]:+10.6f}" \
                + f" {data_b[i]:9.6f} {data_g[i]:9.6f} {data_r[i]:9.6f}" \
                + f" {data_br[i]:9.6f} {data_bg[i]:9.6f} {data_gr[i]:9.6f}\n"
            fh_out.write (record)
