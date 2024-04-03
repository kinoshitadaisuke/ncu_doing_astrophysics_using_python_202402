#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/05 13:17:21 (CST) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.units

# input file name
file_input = 'hd61005_spec.data'

# units
u_micron = astropy.units.micron
u_Jy     = astropy.units.Jy

# making empty numpy arrays
data_wl       = numpy.array ([])
data_flux     = numpy.array ([])
data_flux_err = numpy.array ([])

# opening data file
with open (file_input, 'r') as fh:
    # reading data line-by-line
    for line in fh:
        # if the word '+or-' is found, then we process the line
        if ('+or-' in line):
            # splitting data
            data = line.split ('+or-')
            # wavelength and flux
            (wl_str, flux_str) = data[0].split ()
            # error of flux
            flux_error_str = data[1].split ()[0]
            # conversion from string into float
            wl         = float (wl_str)
            flux       = float (flux_str)
            flux_error = float (flux_error_str)
            # appending data into numpy arrays
            data_wl       = numpy.append (data_wl, wl)
            data_flux     = numpy.append (data_flux, flux)
            data_flux_err = numpy.append (data_flux_err, flux_error)

# adding units
data_wl       = data_wl * u_micron
data_flux     = data_flux * u_Jy
data_flux_err = data_flux_err * u_Jy

# printing data
print (f'SED of HD 61005')
print (f'  wavelength:')
print (f'    {data_wl}')
print (f'  flux:')
print (f'    {data_flux}')
print (f'  error of flux:')
print (f'    {data_flux_err}')
