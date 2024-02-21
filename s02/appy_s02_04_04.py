#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/21 15:22:27 (UT+8) daisuke>
#

# importing pathlib module
import pathlib

# file
file_pi1000 = 'pi_1000.txt'

# making a pathlib object
path_pi1000 = pathlib.Path (file_pi1000)

# opening file
with path_pi1000.open () as fh:
    # reading file
    data_pi = fh.read ()

# printing file content
print (f'---------- {file_pi1000} ----------')
print (f'{data_pi}')
print (f'---------- {file_pi1000} ----------')
