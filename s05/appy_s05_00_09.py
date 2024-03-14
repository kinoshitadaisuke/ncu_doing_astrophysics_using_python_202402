#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/03/13 14:56:27 (UT+8) daisuke>
#

# importing scipy module
import scipy.constants

# giga
giga = scipy.constants.giga

# frequency of electromagnetic radiation
frequency = 115.0 * giga

# wavelength of electromagnetic radiation
wavelength = scipy.constants.nu2lambda (frequency)

# printing the result of conversion
print (f'{frequency:g} [Hz] ==> {wavelength:g} [m]')
