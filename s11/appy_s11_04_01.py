#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/23 09:05:49 (Taiwan_Standard_Time_UT+8) daisuke>
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
data_id        = numpy.array (table['source_id'])
data_ra        = numpy.array (table['ra'])
data_dec       = numpy.array (table['dec'])
data_parallax  = numpy.array (table['parallax'])
data_pmra      = numpy.array (table['pmra'])
data_pmdec     = numpy.array (table['pmdec'])
data_g         = numpy.array (table['phot_g_mean_mag'])
data_gr        = numpy.array (table['g_rp'])

# printing status
if (verbose):
    print (f'Now, writing data into file "{file_output}"...')

# opening file for writing
with open (file_output, 'w') as fh:
    # writing header
    header = "# ID, RA, Dec, parallax, pm in RA, pm in Dec, g mag, g-r colour\n"
    fh.write (header)
    
    # writing data
    for i in range ( len (data_id) ):
        if ( numpy.isnan (data_parallax[i]) ):
            continue
        if (data_parallax[i] < 0.0):
            continue
        record = f"{data_id[i]:19d} {data_ra[i]:8.4f} {data_dec[i]:+8.4f}" \
            + f" {data_parallax[i]:8.4f}" \
            + f" {data_pmra[i]:+8.3f} {data_pmdec[i]:+8.3f}" \
            + f" {data_g[i]:+6.3f} {data_gr[i]:+6.3f}\n"
        fh.write (record)

# printing status
if (verbose):
    print (f'Finished writing data into file "{file_output}"!')
