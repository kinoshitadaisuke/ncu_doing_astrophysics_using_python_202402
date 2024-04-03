#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/31 19:42:56 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.constants
import scipy.optimize

#
# function to calculate blackbody curve
#
def bb_lambda (wavelength, T):
    # speed of light in vacuum
    c = scipy.constants.physical_constants['speed of light in vacuum']

    # Planck constant
    h = scipy.constants.physical_constants['Planck constant']

    # Boltzmann constant
    k = scipy.constants.physical_constants['Boltzmann constant']

    # calculation of Planck function
    blackbody = 2.0 * h[0] * c[0]**2 / wavelength**5 \
        / (numpy.exp (h[0] * c[0] / (wavelength * k[0] * T) ) - 1.0 )

    # returning blackbody radiation curve
    return (blackbody)

#
# function for finding a peak of blackbody radiation curve
#
def nbb_lambda (wavelength, T):
    return (bb_lambda (wavelength, T) * -1.0)

# temperature of blackbody
T = 2500.0

# finding a peak of T=5800 K blackbody radiation spectrum
wavelength_peak = scipy.optimize.minimize_scalar (nbb_lambda, \
                                                  bracket=(10**-8, 10**-3), \
                                                  args=(T), method='Brent')

# printing peak wavelength of black body radiation
print (f'peak wavelength of T={T} K blackbody:')
print (f'  lambda = {wavelength_peak.x} [m]')
print (f'         = {wavelength_peak.x * 10**6} [micron]')
print (f'         = {wavelength_peak.x * 10**9} [nm]')
