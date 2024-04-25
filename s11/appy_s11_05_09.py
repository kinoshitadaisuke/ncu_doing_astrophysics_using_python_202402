#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/04/25 20:34:21 (UT+8) daisuke>
#    

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing astropy module
import astropy.io.votable

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# construction of parser object for argparse
descr  = 'visualising distance distribution of stars'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-i', '--input', help='input VOTable file name')
parser.add_argument ('-o', '--output', help='output figure file name')
parser.add_argument ('-a', '--min', type=float, help='minimum data value')
parser.add_argument ('-b', '--max', type=float, help='maximum data value')
parser.add_argument ('-n', '--nbins', type=int, help='number of bins')
parser.add_argument ('-r', '--resolution', type=float, default=225.0, \
                     help='resolution in DPI (default: 225)')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
file_votable   = args.input
file_fig       = args.output
x_min          = args.min
x_max          = args.max
n_bins         = args.nbins
resolution_dpi = args.resolution

# reading VOTable
table = astropy.io.votable.parse_single_table (file_votable).to_table ()

# data
data_id        = numpy.array (table['source_id'])
data_ra        = numpy.array (table['ra'])
data_dec       = numpy.array (table['dec'])
data_parallax  = numpy.array (table['parallax'])
data_pmra      = numpy.array (table['pmra'])
data_pmdec     = numpy.array (table['pmdec'])
data_rv        = numpy.array (table['radial_velocity'])
data_b         = numpy.array (table['phot_bp_mean_mag'])
data_g         = numpy.array (table['phot_g_mean_mag'])
data_r         = numpy.array (table['phot_rp_mean_mag'])
data_br        = numpy.array (table['bp_rp'])
data_bg        = numpy.array (table['bp_g'])
data_gr        = numpy.array (table['g_rp'])
data_ra_err    = numpy.array (table['ra_error'])
data_dec_err   = numpy.array (table['dec_error'])
data_pmra_err  = numpy.array (table['pmra_error'])
data_pmdec_err = numpy.array (table['pmdec_error'])
data_p_snr     = numpy.array (table['parallax_over_error'])
data_b_snr     = numpy.array (table['phot_bp_mean_flux_over_error'])
data_g_snr     = numpy.array (table['phot_g_mean_flux_over_error'])
data_r_snr     = numpy.array (table['phot_rp_mean_flux_over_error'])

# distance
data_distance = numpy.array ([])
for i in range ( len (data_parallax) ):
    # rejecting stars of negative parallax, no measurement of parallax,
    # and parallax SNR less than 10.0
    if ( (data_parallax[i] <= 0.0) or (numpy.isnan (data_parallax[i]) ) \
         or (data_p_snr[i] < 10.0) ):
        data_distance = numpy.append (data_distance, -1.0)
    else:
        data_distance = numpy.append (data_distance, 1000.0 / data_parallax[i])

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# bins
bin_range = (x_min, x_max)

# axes
ax.set_xlabel ('Distance [pc]')
ax.set_ylabel ('Number of Stars')
ax.set_xlim (bin_range)
ax.grid ()

# making a histogram
ax.hist (data_distance, bins=n_bins, range=bin_range, \
         histtype='bar', align='mid')

# saving file
fig.savefig (file_fig, dpi=resolution_dpi)
