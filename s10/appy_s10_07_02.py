#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/04/22 19:54:59 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

# import tarfile module
import tarfile

# choices
choices_compression = ['none', 'gz', 'bz2', 'xz']

# command-line argument analysis
desc   = 'extracting files in gzipped tar files'
parser = argparse.ArgumentParser (description=desc)
parser.add_argument ('-c', '--compression', default='', \
                     choices=choices_compression, \
                     help='compression type (default: none)')
parser.add_argument ('files', nargs='+', help='files')

# command-line arguments analysis
args = parser.parse_args ()

# input parameters
compression = args.compression
list_files  = args.files

# mode for opening tar file
if (compression == 'gz'):
    mode = 'r:gz'
elif (compression == 'bz2'):
    mode = 'r:bz2'
elif (compression == 'xz'):
    mode = 'r:xz'
else:
    mode = 'r:'

# processing each file
for file_tar in list_files:
    # making pathlib object
    path_tar = pathlib.Path (file_tar)
    # existence check
    if not (path_tar.exists ()):
        # printing message
        print (f'ERROR:')
        print (f'ERROR: file "{file_tar}" does not exists!')
        print (f'ERROR:')
        # skipping
        continue
    # opening tar file
    with tarfile.open (name=file_tar, mode=mode) as tar:
        # getting a list of files in tar file
        list_members = tar.getmembers ()
        # printing a list of files in tar file
        for member in list_members:
            print (f'{member.name}    ({member.size} byte)')
        # extracting files in tar file
        tar.extractall ()
