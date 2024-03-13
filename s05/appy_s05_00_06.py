#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/04 16:10:49 (CST) daisuke>
#

# importing scipy module
import scipy.constants

# some units for length
angstrom = scipy.constants.angstrom
au       = scipy.constants.au
ly       = scipy.constants.light_year
parsec   = scipy.constants.parsec

# printing units for length
print (f'1 angstrom = {angstrom:g} [m]')
print (f'1 au       = {au:g} [m]')
print (f'1 ly       = {ly:g} [m]')
print (f'1 parsec   = {parsec:g} [m]')
