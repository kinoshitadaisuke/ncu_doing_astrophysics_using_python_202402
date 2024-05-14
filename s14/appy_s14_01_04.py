#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/12/13 16:21:24 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing argparse module
import argparse

# importing astropy module
import astropy.time

# importing astroquery module
import astroquery.jplhorizons

# constructing parser object
descr  = "retrieving position of a solar system object using JPL Horizons"
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-t', '--datetime', default='2024-01-01T12:00:00', \
                     help='date/time in UTC as YYYY-MM-DDThh:mm:ss format')
parser.add_argument ('-o', '--obscode', default='D35', \
                     help='observatory code (default: D35)')
parser.add_argument ('-s', '--smallbody', action='store_true', default=False, \
                     help='limiting search for small bodies (default: False)')
parser.add_argument ('target', nargs=1, default='Sun', \
                     help='target object name (default: Sun)')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
datetime  = args.datetime
obscode   = args.obscode
smallbody = args.smallbody
target    = args.target[0]

# date/time
t  = astropy.time.Time (datetime, scale='utc', format='isot')
jd = t.jd

# sending a query to NASA/JPL Horizons system
if (smallbody):
    obj = astroquery.jplhorizons.Horizons (id_type='smallbody', \
                                           id=target, \
                                           location=obscode, \
                                           epochs=jd)
else:
    obj = astroquery.jplhorizons.Horizons (id_type=None, \
                                           id=target, \
                                           location=obscode, \
                                           epochs=jd)

# getting ephemerides
ephemerides = obj.ephemerides ()

# printing ephemerides
print (f'Target body    = {ephemerides["targetname"][0]}')
print (f'Observing site = {obscode}')
print (f'Ephemerides:')
for data in ephemerides:
    # printing date/time
    print (f'  {data["datetime_str"]}')
    print (f'    RA         = {data["RA"]} [deg]')
    print (f'    Dec        = {data["DEC"]} [deg]')
    print (f'    Ecl Lon    = {data["ObsEclLon"]} [deg]')
    print (f'    Ecl Lat    = {data["ObsEclLat"]} [deg]')
    print (f'    Gal Lon    = {data["GlxLon"]} [deg]')
    print (f'    Gal Lat    = {data["GlxLat"]} [deg]')
    print (f'    Az         = {data["AZ"]} [deg]')
    print (f'    El         = {data["EL"]} [deg]')
    print (f'    V-band mag = {data["V"]} [mag]')
    print (f'    R          = {data["r"]} [au]')
    print (f'    Delta      = {data["delta"]} [au]')
