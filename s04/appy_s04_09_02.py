#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/01 14:36:28 (CST) daisuke>
#

# importing argparse module
import argparse

# importing astropy module
import astropy
import astropy.coordinates
import astropy.time
import astropy.units

# constructing a parser object
parser = argparse.ArgumentParser (description='Positions of Sun and planets')

# adding arguments
parser.add_argument ('-t', '--time', default='2000-01-01T12:00:00', \
                     help='date/time in YYYY-MM-DDThh:mm:ss format')

# parsing arguments
args = parser.parse_args ()

# parameters
datetime = args.time

# setting for solar system ephemeris
astropy.coordinates.solar_system_ephemeris.set ('jpl')

# time t = 2023-10-02T00:00:00 (UTC)
t = astropy.time.Time (datetime, format='isot', scale='utc')

# getting positions of Sun, Mercury, Venus, Earth, and Mars
sun     = astropy.coordinates.get_body_barycentric ('sun', t)
mercury = astropy.coordinates.get_body_barycentric ('mercury', t)
venus   = astropy.coordinates.get_body_barycentric ('venus', t)
earth   = astropy.coordinates.get_body_barycentric ('earth', t)
mars    = astropy.coordinates.get_body_barycentric ('mars', t)

# printing positions of the Sun and planets
print (f'Positions of the Sun and the planets at t = {t}')
print (f'  Sun     : {sun}')
print (f'  Mercury : {mercury}')
print (f'  Venus   : {venus}')
print (f'  Earth   : {earth}')
print (f'  Mars    : {mars}')
