#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/08 14:59:55 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing astropy module
import astropy.time

# importing astroquery module
import astroquery.jplhorizons

# date/time
date = astropy.time.Time ('2024-01-01 00:00:00')

# target asteroid name
asteroid = 'Ceres'

# set-up a query for JPL Horizons
query = astroquery.jplhorizons.Horizons (id=asteroid, \
                                         id_type='smallbody', \
                                         epochs=date.jd)

# fetching ephemeris of asteroid
eph = query.ephemerides ()

# printing position of asteroid
print (f"Ephemeris of asteroid '{eph['targetname'][0]}' at {date}:")
print (f"  RA  = {eph['RA'][0]:8.4f} deg")
print (f"  Dec = {eph['DEC'][0]:+8.4f} deg")
