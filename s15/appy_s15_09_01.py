#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/28 09:25:56 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing astropy module
import astropy.io.votable

# construction of parser object for argparse
descr  = f'reading a VOTable file and writing data into a file'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-i', '--input', help='input VOTable file name')
parser.add_argument ('-o', '--output', help='output file name')
parser.add_argument ('-v', '--verbose', action='store_true', default=False, \
                     help='verbose mode (default: False)')

# command-line argument analysis
args = parser.parse_args ()

# VOTable file name
file_votable = args.input

# output file name
file_output  = args.output

# verbosity
verbose = args.verbose

# printing status
if (verbose):
    print (f'Now, reading VOTable file "{file_votable}"...')
    
# reading VOTable
table = astropy.io.votable.parse_single_table (file_votable).to_table ()

# printing status
if (verbose):
    print (f'Finished reading VOTable file "{file_votable}"!')

# data
data_id           = numpy.array (table['SOURCE_ID'])
data_ra           = numpy.array (table['ra'])
data_ra_err       = numpy.array (table['ra_error'])
data_dec          = numpy.array (table['dec'])
data_dec_err      = numpy.array (table['dec_error'])
data_parallax     = numpy.array (table['parallax'])
data_parallax_err = numpy.array (table['parallax_error'])
data_parallax_snr = numpy.array (table['parallax_over_error'])
data_pmra         = numpy.array (table['pmra'])
data_pmra_err     = numpy.array (table['pmra_error'])
data_pmdec        = numpy.array (table['pmdec'])
data_pmdec_err    = numpy.array (table['pmdec_error'])
data_rv           = numpy.array (table['radial_velocity'])
data_rv_err       = numpy.array (table['radial_velocity_error'])
data_b            = numpy.array (table['phot_bp_mean_mag'])
data_g            = numpy.array (table['phot_g_mean_mag'])
data_r            = numpy.array (table['phot_rp_mean_mag'])
data_b_snr        = numpy.array (table['phot_bp_mean_flux_over_error'])
data_g_snr        = numpy.array (table['phot_g_mean_flux_over_error'])
data_r_snr        = numpy.array (table['phot_rp_mean_flux_over_error'])
data_br           = numpy.array (table['bp_rp'])
data_bg           = numpy.array (table['bp_g'])
data_gr           = numpy.array (table['g_rp'])

# printing status
if (verbose):
    print (f'Now, writing data into file "{file_output}"...')

# opening file for writing
with open (file_output, 'w') as fh:
    # writing header
    header = f'#\n' \
        + f'# Gaia DR3 data\n' \
        + f'#\n' \
        + f'#  data format of this file\n' \
        + f'#\n' \
        + f'#   column 01 : source ID\n' \
        + f'#   column 02 : RA in deg\n' \
        + f'#   column 03 : RA error in mas\n' \
        + f'#   column 04 : Dec in deg\n' \
        + f'#   column 05 : Dec error in mas\n' \
        + f'#   column 06 : parallax in mas\n' \
        + f'#   column 07 : parallax error in mas\n' \
        + f'#   column 08 : parallax signal-to-noise ratio\n' \
        + f'#   column 09 : proper motion in RA direction in mas/yr\n' \
        + f'#   column 10 : error of proper motion in RA direction in mas/yr\n' \
        + f'#   column 11 : proper motion in Dec direction in mas/yr\n' \
        + f'#   column 12 : error of proper motion in Dec direction in mas/yr\n' \
        + f'#   column 13 : radial velocity in km/s\n' \
        + f'#   column 14 : radial velocity error in km/s\n' \
        + f'#   column 15 : b-band magnitude\n' \
        + f'#   column 16 : signal-to-noise ratio of b-band magnitude\n' \
        + f'#   column 17 : g-band magnitude\n' \
        + f'#   column 18 : signal-to-noise ratio of g-band magnitude\n' \
        + f'#   column 19 : r-band magnitude\n' \
        + f'#   column 20 : signal-to-noise ratio of r-band magnitude\n' \
        + f'#   column 21 : b-r colour index\n' \
        + f'#   column 22 : b-g colour index\n' \
        + f'#   column 23 : g-r colour index\n' \
        + f'#\n'
    fh.write (header)
    
    # writing data
    for i in range ( len (data_id) ):
        # rejecting data without parallax measurement
        if ( numpy.isnan (data_parallax[i]) ):
            continue
        # rejecting data with negative parallax
        if (data_parallax[i] < 0.0):
            continue
        # rejecting data with poor S/N ratio of parallax measurement
        if (data_parallax_snr[i] < 10.0):
            continue
        # rejecting data if b or g or r band magnitude is NaN
        if ( (numpy.isnan (data_b[i])) \
             or (numpy.isnan (data_g[i])) \
             or (numpy.isnan (data_r[i])) ):
            continue
        # data to be written to file
        record = f"{data_id[i]:19d}" \
            + f" {data_ra[i]:12.8f} {data_ra_err[i]:12.8f}" \
            + f" {data_dec[i]:12.8f} {data_dec_err[i]:12.8f}" \
            + f" {data_parallax[i]:8.3f} {data_parallax_err[i]:8.3f}" \
            + f" {data_parallax_snr[i]:8.3f}" \
            + f" {data_pmra[i]:8.3f} {data_pmra_err[i]:8.3f}" \
            + f" {data_pmdec[i]:8.3f} {data_pmdec_err[i]:8.3f}" \
            + f" {data_rv[i]:12.6f} {data_rv_err[i]:12.6f}" \
            + f" {data_b[i]:8.3f} {data_b_snr[i]:10.3f}" \
            + f" {data_g[i]:8.3f} {data_g_snr[i]:10.3f}" \
            + f" {data_r[i]:8.3f} {data_r_snr[i]:10.3f}" \
            + f" {data_br[i]:6.3f} {data_bg[i]:6.3f} {data_gr[i]:6.3f}\n"
        fh.write (record)

# printing status
if (verbose):
    print (f'Finished writing data into file "{file_output}"!')
