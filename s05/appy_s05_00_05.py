#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/04 16:51:15 (CST) daisuke>
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
