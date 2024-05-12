#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/12 10:22:36 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing sys module
import sys

# importing pathlib module
import pathlib

# importing datetime module
import datetime

# importing astropy module
import astropy.units
import astropy.coordinates

# importing astroquery module
import astroquery.esa.jwst

# date/time
now = datetime.datetime.now ().isoformat ()

# command name
command = sys.argv[0]

# constructing parser object
descr  = "searching JWST images available for download"
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-r', '--ra', default='00h00m00.000s', \
                     help='RA of target object (default: 00h00m00.000s)')
parser.add_argument ('-d', '--dec', default='00d00m00.00s', \
                     help='Dec of target object (default: 00d00m00.000s)')
parser.add_argument ('-s', '--radius', type=float, default=1.0, \
                     help='search radius in arcmin (default: 1)')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
ra            = args.ra
dec           = args.dec
radius_arcmin = args.radius

# units
u_ha     = astropy.units.hourangle
u_deg    = astropy.units.deg
u_arcmin = astropy.units.arcmin

# search radius
radius = radius_arcmin * u_arcmin

# coordinate
coord = astropy.coordinates.SkyCoord (ra, dec, unit=(u_ha, u_deg), frame='icrs')

# coordinate in hh:mm:ss.ss and dd:mm:ss.s format
coord_str                     = coord.to_string (style='hmsdms')
(coord_ra_str, coord_dec_str) = coord_str.split ()
coord_ra_deg                  = coord.ra.deg
coord_dec_deg                 = coord.dec.deg
    
# printing coordinate
print (f'# Coordinate:')
print (f'#  RA:  {coord_ra_str} = {coord_ra_deg} deg')
print (f'#  Dec: {coord_dec_str} = {coord_dec_deg} deg')

# query
jwst = astroquery.esa.jwst.Jwst.cone_search (coordinate=coord, radius=radius, \
                                             async_job=True)

# query result
query_result = jwst.get_results ()

# printing query result
print (f'# obs. ID, calib. level, data type, instrument, energy band')
for i in range (len (query_result)):
    # if the data product is not image, then skip
    if (query_result["dataproducttype"][i] != 'image'):
        continue
    print (f'{query_result["observationid"][i]:40s} {query_result["calibrationlevel"][i]:2d} {query_result["dataproducttype"][i]:5s} {query_result["instrument_name"][i]:12s} {query_result["energy_bandpassname"][i]:16s}')
