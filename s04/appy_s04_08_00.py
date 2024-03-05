#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/01 12:32:23 (CST) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

# importing sys module
import sys

# importing urllib module
import urllib.request

# importing ssl module
import ssl

# constructing a parser object
parser = argparse.ArgumentParser (description='Downloading online material')

# adding arguments
parser.add_argument ('-o', '--output', default='output.png', \
                     help='output file name (default: output.data)')
parser.add_argument ('-b', '--binary', action='store_true', \
                     help='binary mode')
parser.add_argument ('-v', '--verbose', action='store_true', \
                     help='verbose mode')
parser.add_argument ('url', default='', \
                     help='URL of online material')

# parsing arguments
args = parser.parse_args ()

# parameters
file_output = args.output
binary_mode = args.binary
url_data    = args.url
verbose     = args.verbose

# making a pathlib object for output file
path_output = pathlib.Path (file_output)

# check of existence of output file
if (path_output.exists ()):
    # printing a message
    print (f'ERROR: output file "{file_output}" exists!')
    # stopping the script
    sys.exit (0)

# allow insecure downloading
ssl._create_default_https_context = ssl._create_unverified_context

# printing status
if (verbose):
    print (f'# Now, fetching "{url_data}"...')

# opening URL
with urllib.request.urlopen (url_data) as fh_read:
    # reading data
    data_byte = fh_read.read ()

# printing status
if (verbose):
    print (f'# Finished fetching "{url_data}"!')

# printing status
if (verbose):
    print (f'# Now, writing data into file "{file_output}"...')

# opening file for writing
if (binary_mode):
    # opening file
    with open (file_output, 'wb') as fh_write:
        # writing data into file
        fh_write.write (data_byte)
else:
    # converting raw byte data into string
    data_str = data_byte.decode ('utf-8')
    # opening file
    with open (file_output, 'w') as fh_write:
        # writing data into file
        fh_write.write (data_str)

# printing status
if (verbose):
    print (f'# Finished writing data into file "{file_output}"!')

# check of existence of output file
if (path_output.exists ()):
    # file size
    size = path_output.stat ().st_size
else:
    # printing a message
    print (f'ERROR: output file "{file_output}" does not exist!')
    # stopping the script
    sys.exit (0)
    
# printing summary information
print (f'#')
print (f'# Download summary')
print (f'#')
print (f'#  URL              : "{url_data}"')
print (f'#  output file      : "{file_output}"')
print (f'#  data transferred : {size} bytes')
print (f'#')
