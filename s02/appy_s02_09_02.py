#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/21 15:24:25 (UT+8) daisuke>
#

# importing gzip module
import gzip

# file of Yale Bright Star Catalogue
file_bsc = 'catalog.gz'

# output file
file_output = 'bsc.data'

# opening a compressed file
with gzip.open (file_bsc, 'rb') as fh_read:
    # reading file
    data_byte = fh_read.read ()

# converting byte data into string
data_str = data_byte.decode ('utf-8')

# opening new file
with open (file_output, 'w') as fh_write:
    # writing catalogue into a new file
    fh_write.write (data_str)
