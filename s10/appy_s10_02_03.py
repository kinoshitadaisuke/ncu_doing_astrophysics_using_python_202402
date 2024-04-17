#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/18 19:01:12 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing json module
import json

# JSON file name
file_json = 'exoplanets/data/exoplanet.json'

# opening file
with open (file_json, 'r') as fh:
    # reading JSON file
    data = json.load (fh)

# host star name
star = '51 Peg'

# printing header
print (f'List of known exoplanets around star "{star}":')

# printing the information of exoplanet hosted by 51 Peg
for i in range (len (data)):
    if (data[i]['star_name'] == '51 Peg'):
        print (f"  Exoplanet name: {data[i]['# name']:32s}")
        print (f"    M      = {data[i]['mass']} [M_jupiter]")
        print (f"    a      = {data[i]['semi_major_axis']} [au]")
        print (f"    P      = {data[i]['orbital_period']} [day]")
        print (f"    method = {data[i]['detection_type']}")
