#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/04/18 20:27:34 (UT+8) daisuke>
#

# importing json module
import json

# JSON file name
file_json = 'exoplanets/data/exoplanet.json'

# opening file
with open (file_json, 'r') as fh:
    # reading JSON file
    data = json.load (fh)

# printing keys of the data
for key in data[0].keys ():
    print (f"{key}")
