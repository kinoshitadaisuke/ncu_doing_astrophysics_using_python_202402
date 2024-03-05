#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/01 14:51:39 (CST) daisuke>
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

# units
u_au = astropy.units.au

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
print (f'  Sun:')
print (f'    X = {sun.x:+15.3f} = {sun.x.to (u_au).value:+8.5f} au')
print (f'    Y = {sun.y:+15.3f} = {sun.y.to (u_au).value:+8.5f} au')
print (f'    Z = {sun.z:+15.3f} = {sun.z.to (u_au).value:+8.5f} au')
print (f'  Mercury:')
print (f'    X = {mercury.x:+15.3f} = {mercury.x.to (u_au).value:+8.5f} au')
print (f'    Y = {mercury.y:+15.3f} = {mercury.y.to (u_au).value:+8.5f} au')
print (f'    Z = {mercury.z:+15.3f} = {mercury.z.to (u_au).value:+8.5f} au')
print (f'  Venus:')
print (f'    X = {venus.x:+15.3f} = {venus.x.to (u_au).value:+8.5f} au')
print (f'    Y = {venus.y:+15.3f} = {venus.y.to (u_au).value:+8.5f} au')
print (f'    Z = {venus.z:+15.3f} = {venus.z.to (u_au).value:+8.5f} au')
print (f'  Earth:')
print (f'    X = {earth.x:+15.3f} = {earth.x.to (u_au).value:+8.5f} au')
print (f'    Y = {earth.y:+15.3f} = {earth.y.to (u_au).value:+8.5f} au')
print (f'    Z = {earth.z:+15.3f} = {earth.z.to (u_au).value:+8.5f} au')
print (f'  Mars:')
print (f'    X = {mars.x:+15.3f} = {mars.x.to (u_au).value:+8.5f} au')
print (f'    Y = {mars.y:+15.3f} = {mars.y.to (u_au).value:+8.5f} au')
print (f'    Z = {mars.z:+15.3f} = {mars.z.to (u_au).value:+8.5f} au')
