#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/04 16:36:08 (CST) daisuke>
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
