#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/27 15:59:05 (UT+8) daisuke>
#

# data file
file_data = 'ast_taxonomy/data/taxonomy10.tab'

# opening data file
with open (file_data, 'r') as fh:
    # reading data file line-by-line
    for line in fh:
        # extracting data
        number    = int (line[0:7])
        bus_class = line[80:83]
        # finding taxonomic class
        if (bus_class[0] == 'C'):
            taxonomy = 'C'
        elif (bus_class[0] == 'S'):
            taxonomy = 'S'
        elif (bus_class[0] == 'X'):
            taxonomy = 'X'
        elif (bus_class[0] == 'V'):
            taxonomy = 'V'
        elif (bus_class[0] == 'D'):
            taxonomy = 'D'
        else:
            taxonomy = 'others'
        # printing taxonomic classification
        if not ( (taxonomy == 'others') or (number == 0) ):
            print (f'{number:6d}  ==>  {taxonomy}-type or its variant')
