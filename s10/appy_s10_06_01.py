#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/19 17:51:36 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing pathlib module
import pathlib

# list of data files
files = pathlib.Path ('.').glob ('osc_0000_1989/*.json')

# printing file names
for file in sorted (files):
    print (file)
