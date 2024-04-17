#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/18 17:54:27 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing astropy module
import astropy.io.ascii

# CSV file name
file_csv = 'hyg/hyg/v3/hyg_v37.csv'

# reading a CSV file and storing data in an astropy table
table = astropy.io.ascii.read (file_csv, format='csv')

# printing astropy table
print (table)
