#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/04/04 20:21:54 (UT+8) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.modeling.models
import astropy.units

# units
unit_K  = astropy.units.K
unit_Hz = astropy.units.Hz

# temperature of blackbody
T = 8000.0 * unit_K

# printing temperature of blackbody
print (f'Temperature:')
print (f'  T = {T}')

# range of frequency (from 10**9 to 10**16)
frequency_min =  9.0
frequency_max = 16.0

# frequency in Hz
frequency_Hz = numpy.logspace (frequency_min, frequency_max, \
                               num=7001, dtype=numpy.longdouble) * unit_Hz

# a function to calculate blackbody radiation for T=8000 K
bb_model = astropy.modeling.models.BlackBody (temperature=T)

# calculation of blackbody radiation
bb_data = bb_model (frequency_Hz)

# printing blackbody radiation
print (f'Frequency:')
print (f'{frequency_Hz}')
print (f'Blackbody radiation:')
print (f'{bb_data}')
