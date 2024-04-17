#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/19 18:01:28 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing json module
import json

# file name
file_json = 'osc_0000_1989/SN1980A.json'

# opening file
with open (file_json, 'r') as fh:
    # reading JSON data from file
    data = json.load (fh)

# printing data
for obj in data:
    print ("obj =", obj)
    for key in data[obj]:
        print ("  %-16s ==> %s" % (key, data[obj][key]) )
