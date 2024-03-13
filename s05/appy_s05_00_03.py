#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/04 16:48:27 (CST) daisuke>
#

# importing scipy module
import scipy.constants

# searching constants
search_result = scipy.constants.find ('light')

# printing search result
for constant in search_result:
    print (f'{constant}')
