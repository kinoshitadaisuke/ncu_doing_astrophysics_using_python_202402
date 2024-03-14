#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/03/13 14:56:09 (UT+8) daisuke>
#

# importing scipy module
import scipy.constants

# searching constants
search_result = scipy.constants.find ('light')

# printing search result
for constant in search_result:
    print (f'{constant}:')
    print (f'  value = {scipy.constants.value (constant)}')
    print (f'  error = {scipy.constants.precision (constant)}')
    print (f'  unit  = {scipy.constants.unit (constant)}')
