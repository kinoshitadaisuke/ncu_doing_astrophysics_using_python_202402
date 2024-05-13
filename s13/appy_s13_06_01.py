#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/13 20:03:40 (UT+8) daisuke>
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
parser.add_argument ('-o', '--output', default='', \
                     help='output file name')
parser.add_argument ('-r', '--radius', type=float, default=1.0, \
                     help='search radius in arcmin (default: 1)')
parser.add_argument ('ra', nargs=1, default='00h00m00.000s', \
                     help='RA of target object (default: 00h00m00.000s)')
parser.add_argument ('dec', nargs=1, default='00d00m00.00s', \
                     help='Dec of target object (default: 00d00m00.000s)')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
file_output   = args.output
radius_arcmin = args.radius
ra            = args.ra[0]
dec           = args.dec[0]

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

# writing query result
with open (file_output, 'w') as fh:
    # writing header
    header = f'# obs. ID, calib. level, data type, instrument, energy band\n'
    fh.write (header)
    for i in range (len (query_result)):
        # if the data product is not image, then skip
        if (query_result["dataproducttype"][i] != 'image'):
            continue
        # coordinate
        coord = astropy.coordinates.SkyCoord (query_result["target_ra"][i], \
                                              query_result["target_dec"][i], \
                                              unit=(u_deg, u_deg), frame='icrs')
        # writing data into file
        record = f'{query_result["observationid"][i]:36s}' \
            + f' {query_result["calibrationlevel"][i]:2d}' \
            + f' {query_result["dataproducttype"][i]:5s}' \
            + f' {query_result["instrument_name"][i]:12s}' \
            + f' {query_result["energy_bandpassname"][i]:12s}' \
            + f' {coord.ra.deg:8.3f} {coord.dec.deg:8.3f}\n'
        fh.write (record)
