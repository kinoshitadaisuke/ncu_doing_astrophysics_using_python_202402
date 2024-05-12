#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/12 08:40:07 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing sys module
import sys

# importing pathlib module
import pathlib

# importing astroquery module
import astroquery.simbad
import astroquery.ipac.ned
import astroquery.skyview

# importing astropy module
import astropy.coordinates
import astropy.units

# importing datetime module
import datetime

# importing ssl module
import ssl

# allow insecure downloading
ssl._create_default_https_context = ssl._create_unverified_context

# date/time
now = datetime.datetime.now ().isoformat ()

# units
u_ha  = astropy.units.hourangle
u_deg = astropy.units.deg

# constructing parser object
descr  = "downloading DSS/SDSS image"
parser = argparse.ArgumentParser (description=descr)

# adding arguments
list_resolver = ['simbad', 'ned']
list_survey   = ['DSS1 Blue', 'DSS1 Red', 'DSS2 Blue', 'DSS2 Red', 'DSS2 IR', \
                 'SDSSu', 'SDSSg', 'SDSSr', 'SDSSi', 'SDSSz']
parser.add_argument ('-r', '--resolver', choices=list_resolver, \
                     default='simbad', help='choice of name resolver')
parser.add_argument ('-s', '--survey', choices=list_survey, \
                     default='SDSSr', help='choice of survey')
parser.add_argument ('-t', '--target', default='', help='target name')
parser.add_argument ('-f', '--fov', type=int, default=1024, \
                     help='field-of-view in pixel')
parser.add_argument ('-o', '--output', default='', help='output file name')
parser.add_argument ('-x', '--offset-ra', type=float, default=0.0, \
                     help='offset in RA direction in arcmin (default: 0)')
parser.add_argument ('-y', '--offset-dec', type=float, default=0.0, \
                     help='offset in Dec direction in arcmin (default: 0)')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
name_resolver     = args.resolver
survey            = args.survey
target_name       = args.target
fov_pix           = args.fov
file_output       = args.output
offset_ra_arcmin  = args.offset_ra
offset_dec_arcmin = args.offset_ra

# checking target name
if (target_name == ''):
    # printing error message
    print (f'ERROR:')
    print (f'ERROR: No target name is given!')
    print (f'ERROR:')
    # exit
    sys.exit ()

# making pathlib object
path_output = pathlib.Path (file_output)
    
# checking output file name
if (file_output == ''):
    # printing error message
    print (f'ERROR:')
    print (f'ERROR: No output file name is given!')
    print (f'ERROR:')
    # exit
    sys.exit ()
elif not (path_output.suffix == '.fits'):
    # printing error message
    print (f'ERROR:')
    print (f'ERROR: Output file must be FITS file!')
    print (f'ERROR:')
    # exit
    sys.exit ()
if (path_output.exists ()):
    # printing error message
    print (f'ERROR:')
    print (f'ERROR: Output file "{file_output}" exists!')
    print (f'ERROR:')
    # exit
    sys.exit ()
    
# using name resolver
if (name_resolver == 'simbad'):
    query_result = astroquery.simbad.Simbad.query_object (target_name)
elif (name_resolver == 'ned'):
    query_result = astroquery.ipac.ned.Ned.query_object (target_name)

# RA and Dec
RA  = query_result['RA']
Dec = query_result['DEC']

# coordinate
if (name_resolver == 'simbad'):
    coord = astropy.coordinates.SkyCoord (RA[0], Dec[0], unit=(u_ha, u_deg))
elif (name_resolver == 'ned'):
    coord = astropy.coordinates.SkyCoord (RA[0], Dec[0], unit=(u_deg, u_deg))

coord_str = coord.to_string (style='hmsdms')
(coord_ra_str, coord_dec_str) = coord_str.split ()
coord_ra_deg  = coord.ra.deg
coord_dec_deg = coord.dec.deg
    
# printing coordinate
print (f'Target Name: "{target_name}"')
print (f'  RA:  {coord_ra_str} = {coord_ra_deg} deg')
print (f'  Dec: {coord_dec_str} = {coord_dec_deg} deg')

# giving offsets
coord2_ra_deg  = coord_ra_deg + offset_ra_arcmin / 60.0
coord2_dec_deg = coord_dec_deg + offset_dec_arcmin / 60.0

# SkyCoord object for coordinates after giving offsets
coord2 = astropy.coordinates.SkyCoord (coord2_ra_deg, coord2_dec_deg, \
                                       unit=(u_deg, u_deg))
coord2_str = coord2.to_string (style='hmsdms')
(coord2_ra_str, coord2_dec_str) = coord_str.split ()

# printing coordinate
print (f'Coordinates after giving offsets')
print (f'  RA:  {coord2_ra_str} = {coord2_ra_deg} deg')
print (f'  Dec: {coord2_dec_str} = {coord2_dec_deg} deg')

# searching image
list_image = astroquery.skyview.SkyView.get_image_list (position=coord2, \
                                                        survey=survey)

# printing image list
print (f'Available images:')
print (f' {list_image}')

# getting image
image = astroquery.skyview.SkyView.get_images (position=coord2, survey=survey, \
                                               pixels=fov_pix)

# header and data
image0 = image[0]
header = image0[0].header
data   = image0[0].data

# adding comments in header
header['history'] = f'image downloaded from {survey}'
header['history'] = f'image saved on {now}'

# saving to a FITS file
astropy.io.fits.writeto (file_output, data, header=header)
