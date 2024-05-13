#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/13 20:21:32 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing astropy module
import astropy.io.votable
import astropy.coordinates
import astropy.units

# construction of parser object for argparse
descr  = 'reading VOTable file'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-i', '--input', help='input VOTable file name')
parser.add_argument ('-o', '--output', help='output file name')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
file_votable = args.input
file_output  = args.output

# units
u_deg = astropy.units.deg

# reading VOTable
table = astropy.io.votable.parse_single_table (file_votable).to_table ()

# writing data into file
with open (file_output, 'w') as fh:
    # writing header
    header = f'# obs. ID, exposure, instrument, obs. type, data type, filter, date\n'
    fh.write (header)
    # writing data
    for i in range (len (table)):
        # coordinate
        coord = astropy.coordinates.SkyCoord (table["ra"][i], table["dec"][i], \
                                              unit=(u_deg, u_deg), frame='icrs')
        # writing data to file
        record = f'{table["observation_id"][i]:36s}' \
            + f' {table["exposure_duration"][i]:6.1f}' \
            + f' {table["instrument_name"][i]:8s}' \
            + f' {table["obs_type"][i]:28s}' \
            + f' {table["data_product_type"][i]:8s}' \
            + f' {table["filter"][i]:12s}' \
            + f' {coord.ra.deg:8.3f}' \
            + f' {coord.dec.deg:8.3f}\n'
        fh.write (record)
