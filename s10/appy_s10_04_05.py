#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/04/23 14:33:29 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing astropy module
import astropy.units

# command-line argument analysis
desc   = 'Calculation of Hubble time from Hubble constant'
parser = argparse.ArgumentParser (description=desc)
parser.add_argument ('HubbleConstant', nargs=1, type=float, default=70.0, \
                     help='Hubble constant in km/sec/Mpc')

# command-line arguments analysis
args = parser.parse_args ()

# input parameters
hubble_constant = args.HubbleConstant[0]

# units
u_km  = astropy.units.km
u_Mpc = astropy.units.Mpc
u_sec = astropy.units.s
u_yr  = astropy.units.yr

# Hubble constant with units
hubble_constant_with_units = hubble_constant * u_km / u_sec / u_Mpc

# calculation of Hubble time
hubble_time = 1.0 / hubble_constant_with_units

# printing result of calculation
print (f'Hubble constant = {hubble_constant_with_units}')
print (f'Hubble time     = {hubble_time.to (u_sec):g}')
print (f'                = {hubble_time.to (u_yr):g}')
