#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/04/28 00:44:10 (UT+8) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.io.votable

# VOTable file name
file_votable = "m3.vot.gz"

# output file name
file_output = 'm3.list'

# reading VOTable
data_vot = astropy.io.votable.parse_single_table (file_votable)

# printing data type
print (f'data type of "data_vot" = {type (data_vot)}')
