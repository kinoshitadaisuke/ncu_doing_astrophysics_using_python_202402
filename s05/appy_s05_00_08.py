#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/03/13 14:56:24 (UT+8) daisuke>
#

# importing scipy module
import scipy.constants

# nano
nano = scipy.constants.nano

# wavelength of electromagnetic radiation
wavelength = 500.0 * nano

# frequency of electromagnetic radiation
frequency = scipy.constants.lambda2nu (wavelength)

# printing the result of conversion
print (f'{wavelength:g} [m] ==> {frequency:g} [Hz]')
