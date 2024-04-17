#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/19 15:52:55 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing astropy module
import astropy.io.ascii

# file
file_data = 'ned1d_new.csv'

# reading CSV data
rawdata = astropy.io.ascii.read (file_data, format='csv')

# printing astropy table summary information
print (rawdata.info ())
