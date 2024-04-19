#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/04/19 11:43:59 (UT+8) daisuke>
#

# importing astropy module
import astropy.io.ascii

# CSV file name
file_csv = 'hyg/hyg/v3/hyg_v38.csv'

# reading a CSV file and storing data in an astropy table
table = astropy.io.ascii.read (file_csv, format='csv')

# printing astropy table
print (table)
