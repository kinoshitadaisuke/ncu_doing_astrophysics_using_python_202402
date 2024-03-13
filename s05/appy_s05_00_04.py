#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/04 15:38:40 (CST) daisuke>
#

# importing scipy module
import scipy.constants

# searching constants
search_result = scipy.constants.find ('light')

# printing search result
for constant in search_result:
    print (f'{constant}:')
    print (f'  value = {scipy.constants.physical_constants[constant][0]}')
    print (f'  error = {scipy.constants.physical_constants[constant][2]}')
    print (f'  unit  = {scipy.constants.physical_constants[constant][1]}')
