#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/04 16:27:43 (CST) daisuke>
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
