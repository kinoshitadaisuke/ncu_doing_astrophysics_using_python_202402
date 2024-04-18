#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/04/18 20:27:29 (UT+8) daisuke>
#

# importing json module
import json

# JSON file name
file_json = 'exoplanets/data/exoplanet.json'

# opening file
with open (file_json, 'r') as fh:
    # reading JSON file
    data = json.load (fh)

# printing type of data
print (f'type (data)    = {type (data)}')

# printing type of data[0]
print (f'type (data[0]) = {type (data[0])}')
