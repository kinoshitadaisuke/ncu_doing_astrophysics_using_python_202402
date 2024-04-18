#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/04/18 20:26:58 (UT+8) daisuke>
#

# importing astropy module
import astropy.io.ascii

# CSV file name
file_csv = 'honey-badger/examples/planets/planets.csv'

# reading a CSV file and storing data in an astropy table
table = astropy.io.ascii.read (file_csv, format='csv')

# printing the column for mean temperature
print (f'{table["Planet", "Mean Temperature (C)"]}')
