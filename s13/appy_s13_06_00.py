#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/12 17:33:04 (UT+8) daisuke>
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
list_survey   = [
    'DSS1 Blue', 'DSS1 Red', 'DSS2 Blue', 'DSS2 Red', 'DSS2 IR', \
    'SDSSu', 'SDSSg', 'SDSSr', 'SDSSi', 'SDSSz', \
    'GOODS: Chandra ACIS FB', 'GOODS: Chandra ACIS HB', \
    'GOODS: Chandra ACIS SB', \
    'GOODS: HST ACS B', 'GOODS: HST ACS V', \
    'GOODS: HST ACS I', 'GOODS: HST ACS Z'
                 ]
parser.add_argument ('-s', '--survey', choices=list_survey, \
                     default='SDSSr', help='choice of survey')
parser.add_argument ('-f', '--fov', type=int, default=1024, \
                     help='field-of-view in pixel')
parser.add_argument ('-o', '--output', default='', help='output file name')
parser.add_argument ('-r', '--ra', default='00h00m00.000s', \
                     help='RA of target object (default: 00h00m00.000s)')
parser.add_argument ('-d', '--dec', default='00d00m00.00s', \
                     help='Dec of target object (default: 00d00m00.000s)')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
survey        = args.survey
fov_pix       = args.fov
file_output   = args.output
ra            = args.ra
dec           = args.dec

# making pathlib object
path_output = pathlib.Path (file_output)
    
# checking output file name
if (file_output == ''):
    # printing error message
    print ("No output file name is given!")
    # exit
    sys.exit ()
elif not (path_output.suffix == '.fits'):
    # printing error message
    print ("Output file must be FITS file!")
    # exit
    sys.exit ()
if (path_output.exists ()):
    # printing error message
    print ("Output file '%s' exists!" % file_output)
    # exit
    sys.exit ()
    
# coordinate
coord = astropy.coordinates.SkyCoord (ra, dec, unit=(u_ha, u_deg))

coord_str = coord.to_string (style='hmsdms')
(coord_ra_str, coord_dec_str) = coord_str.split ()
coord_ra_deg  = coord.ra.deg
coord_dec_deg = coord.dec.deg
    
# printing coordinate
print (f'Coordinate:')
print (f'  RA:  {coord_ra_str} = {coord_ra_deg} deg')
print (f'  Dec: {coord_dec_str} = {coord_dec_deg} deg')

# searching image
list_image = astroquery.skyview.SkyView.get_image_list (position=coord, \
                                                        survey=survey)

# printing image list
print (f'Available images:')
print (f' {list_image}')

# getting image
image = astroquery.skyview.SkyView.get_images (position=coord, survey=survey, \
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
