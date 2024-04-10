#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/08 15:28:44 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing astropy module
import astropy.time

# importing astroquery module
import astroquery.jplhorizons

# date/time
date = astropy.time.Time ('2024-01-01 00:00:00')

# number of asteroids to get position
n_asteroids = 10

# printing header
print (f"Positions of asteroids on {date}:")

# processing for each asteroid
for i in range (1, n_asteroids + 1):
    # set-up a query for JPL Horizons
    query = astroquery.jplhorizons.Horizons (id=f"{i}", \
                                             id_type='smallbody', \
                                             epochs=date.jd)

    # fetching ephemeris of asteroid
    eph = query.ephemerides ()

    # priting RA and Dec of asteroid
    print (f" {eph['targetname'][0]:32s}:" \
           + f" (RA, Dec) = ({eph['RA'][0]:8.4f} deg," \
           + f" {eph['DEC'][0]:+8.4f} deg)")
