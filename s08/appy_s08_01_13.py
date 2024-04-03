#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/03 08:26:01 (CST) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.modeling.models
import astropy.units

# units
unit_K            = astropy.units.K
unit_sec          = astropy.units.s
unit_Hz           = astropy.units.Hz
unit_erg          = astropy.units.erg
unit_m            = astropy.units.m
unit_cm           = astropy.units.cm
unit_micron       = astropy.units.micron
unit_AA           = astropy.units.AA
unit_sr           = astropy.units.sr
unit_sp_intensity = unit_erg / unit_sec / unit_cm**2 / unit_AA / unit_sr

# temperature of blackbody
T = 3000.0 * unit_K

# printing temperature of blackbody
print (f'Temperature:')
print (f'  T = {T}')

# range of wavelength (from 10**-9 to 10**-3 metre)
wavelength_min = -9.0
wavelength_max = -3.0

# wavelength
wavelength_m      = numpy.logspace (wavelength_min, wavelength_max, \
                                    num=6001, dtype=numpy.longdouble) * unit_m
wavelength_aa     = wavelength_m.to (unit_AA)
wavelength_micron = wavelength_m.to (unit_micron)

# a function to calculate blackbody radiation for T=5000 K
bb_model = astropy.modeling.models.BlackBody (temperature=T, \
                                              scale=1.0 * unit_sp_intensity)

# calculation of blackbody radiation
bb_data = bb_model (wavelength_aa)

# printing blackbody radiation
print (f'Wavelength:')
print (f'{wavelength_micron}')
print (f'Blackbody radiation:')
print (f'{bb_data}')

# finding wavelength corresponding to the peak of blackbody radiation
wavelength_peak        = bb_model.lambda_max
wavelength_peak_micron = wavelength_peak.to (unit_micron)

# printing wavelength corresponding to the peak of blackbody radiation
print (f'peak of blackbody radiation of T={T}:')
print (f'  wavelength_peak = {wavelength_peak_micron:g}')
