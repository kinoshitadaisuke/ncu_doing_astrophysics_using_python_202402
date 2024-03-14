#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/03/13 14:55:58 (UT+8) daisuke>
#

# importing scipy module
import scipy.constants

# searching constants
search_result = scipy.constants.find ('light')

# printing search result
for constant in search_result:
    print (f'{constant}')
