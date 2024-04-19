#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/04/19 11:45:04 (UT+8) daisuke>
#

# importing astropy module
import astropy.io.ascii

# CSV file name
file_csv = 'hyg/hyg/v3/hyg_v38.csv'

# reading a CSV file and storing data in an astropy table
table = astropy.io.ascii.read (file_csv, format='csv')

# making a mask for Vega
obj  = 'Vega'
mask = (table['proper'] == obj)

# printing information of Vega
print (f"object name = {obj}")
print (table[mask]['proper', 'con', 'ra', 'dec', \
                   'mag', 'dist', 'absmag', 'spect'])
