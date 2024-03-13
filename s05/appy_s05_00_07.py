#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/04 16:11:32 (CST) daisuke>
#

# importing scipy module
import scipy.constants

# some units of time
day  = scipy.constants.day
year = scipy.constants.year

# printing units of time
print (f'1 day  = {day:g} [sec]')
print (f'1 year = {year:g} [sec]')

# some units of energy
eV  = scipy.constants.eV
erg = scipy.constants.erg

# printing units of energy
print (f'1 eV   = {eV:g} [J]')
print (f'1 erg  = {erg:g} [J]')

# some units of pressure
atm  = scipy.constants.atm
bar  = scipy.constants.bar
torr = scipy.constants.torr
mmHg = scipy.constants.mmHg

# printing units of pressure
print (f'1 atm  = {atm:g} [Pa]')
print (f'1 bar  = {bar:g} [Pa]')
print (f'1 torr = {torr:g} [Pa]')
print (f'1 mmHg = {mmHg:g} [Pa]')
