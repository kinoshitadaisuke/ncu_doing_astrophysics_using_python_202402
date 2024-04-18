#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/04/18 20:29:37 (UT+8) daisuke>
#

# importing pathlib module
import pathlib

# list of data files
files = pathlib.Path ('.').glob ('osc_0000_1989/*.json')

# printing file names
for file in sorted (files):
    print (file)
