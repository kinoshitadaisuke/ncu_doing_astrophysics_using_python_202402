#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/18 16:40:09 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing astropy module
import astropy.io.ascii

# CSV file name
file_csv = 'honey-badger/examples/planets/planets.csv'

# reading a CSV file and storing data in an astropy table
table = astropy.io.ascii.read (file_csv, format='csv')

# printing the column for mean temperature
print (f'{table["Planet", "Mean Temperature (C)"]}')
