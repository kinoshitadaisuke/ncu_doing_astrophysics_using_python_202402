#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/12 21:50:36 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing astropy module
import astropy.io.votable

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

# reading VOTable
table = astropy.io.votable.parse_single_table (file_votable).to_table ()

# writing data into file
with open (file_output, 'w') as fh:
    # writing header
    header = f'# obs. ID, exposure, instrument, obs. type, data type, filter, date\n'
    fh.write (header)
    # writing data
    for i in range (len (table)):
        record = f'{table["observation_id"][i]}' \
            + f' {table["exposure_duration"][i]:6.1f}' \
            + f' {table["instrument_name"][i]}' \
            + f' {table["obs_type"][i]}' \
            + f' {table["data_product_type"][i]}' \
            + f' {table["filter"][i]}' \
            + f' {table["start_time"][i]}\n'
        fh.write (record)
