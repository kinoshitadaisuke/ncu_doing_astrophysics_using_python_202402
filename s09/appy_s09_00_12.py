#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/04/15 20:16:08 (UT+8) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.coordinates
import astropy.time
import astropy.units

# importing astroquery module
import astroquery.jplhorizons

# output file name
file_output = 'asteroids_001000.data'

# date/time
date = astropy.time.Time ('2024-05-01 00:00:00')

# number of asteroids to get position
n_asteroids = 1000

# opening file for writing
with open (file_output, 'w') as fh:
    # writing a header into output file
    fh.write (f'#\n')
    fh.write (f'# Asteroid positions\n')
    fh.write (f'#\n')
    fh.write (f'#  Date/Time           : {date}\n')
    fh.write (f'#  Number of asteroids : {n_asteroids}\n')
    fh.write (f'#  Output data file    : {file_output}\n')
    fh.write (f'#\n')
    fh.write (f'#  Data file format\n')
    fh.write (f'#   1st column : RA in deg\n')
    fh.write (f'#   2nd column : Dec in deg\n')
    fh.write (f'#   3th column : Ecliptic Longitude in deg\n')
    fh.write (f'#   4th column : Ecliptic Latitude in deg\n')
    fh.write (f'#   5th column : Galactic Longitude in deg\n')
    fh.write (f'#   6th column : Galactic Latitude in deg\n')
    fh.write (f'#   7th column : absolute magnitude in mag\n')
    fh.write (f'#   8th column : apparent V-band magnitude in mag\n')
    fh.write (f'#   after "#"  : asteroid name\n')
    fh.write (f'#\n')
    
    # processing for each asteroid
    for i in range (1, n_asteroids + 1):
        # set-up a query for JPL Horizons
        query = astroquery.jplhorizons.Horizons (id=f"{i}", \
                                                 id_type='smallbody', \
                                                 epochs=date.jd)

        # fetching ephemeris of asteroid
        eph = query.ephemerides ()

        # writing RA and Dec of asteroid into output file
        data = f'{eph["RA"][0]:9.5f}  {eph["DEC"][0]:+9.5f}' \
            + f' {eph["EclLon"][0]:9.5f}  {eph["EclLat"][0]:+9.5f}' \
            + f' {eph["GlxLon"][0]:9.5f}  {eph["GlxLat"][0]:+9.5f}' \
            + f' {eph["H"][0]:9.5f}  {eph["V"][0]:9.5f}' \
            + f' # {eph["targetname"][0]:32s}\n'
        fh.write (data)

        # printing progress
        if (i % 50 == 0):
            print (f' progress : {i / n_asteroids * 100.0:5.1f} percent')
