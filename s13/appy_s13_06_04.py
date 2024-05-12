#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/12 18:39:13 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing pathlib object
import pathlib

# importing gzip module
import gzip

# constructing parser object
descr  = "un-compressing gzip compressed file"
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('files', nargs='+', default='', \
                     help='files')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
list_files = args.files

# processing file one-by-one
for file_input in list_files:
    # printing status
    print (f'Now, processing file "{file_input}"...')

    # making pathlib object
    path_input = pathlib.Path (file_input)

    # if extension of file is not ".gz", then skip
    if not (path_input.suffix == '.gz'):
        # printing message
        print (f'WARNING:')
        print (f'WARNING: suffix of file "{file_input}" is not ".gz"!')
        print (f'WARNING: skipping...')
        print (f'WARNING:')
        # skipping
        continue

    # if the file does not exist, then skip
    if not (path_input.exists ()):
        # printing message
        print (f'WARNING:')
        print (f'WARNING: file "{file_input}" does not exist!')
        print (f'WARNING: skipping...')
        print (f'WARNING:')
        # skipping
        continue

    # output file name
    file_output = path_input.stem

    # printing status
    print (f'  Now, creating file "{file_output}"...')
    
    # opening file for reading
    with gzip.open (file_input, 'rb') as fh_in:
        # reading data
        data = fh_in.read ()
        # opening file for writing
        with open (file_output, 'wb') as fh_out:
            # writing data into file
            fh_out.write (data)

    # printing status
    print (f'  Finished creating file "{file_output}"!')

    # printing status
    print (f'Finished processing file "{file_input}"!')
