#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/22 15:10:43 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing argparse module
import argparse

# importing astropy module
import astropy.units
import astropy.coordinates
import astropy.io.fits

# importing astroquery module
import astroquery.simbad
import astroquery.skyview

# importing ssl module
import ssl

# allow insecure downloading
ssl._create_default_https_context = ssl._create_unverified_context

# units
u_ha  = astropy.units.hourangle
u_deg = astropy.units.deg

# target object name
target      = 'M1'

# choice of survey data
survey      = 'DSS2 Red'

# field-of-view of image in arcmin
fov_arcmin  = 15.0

# field-of-view in arcmin
fov_arcsec = fov_arcmin * 60.0

# number of pixels of image
fov_pixel  = int (fov_arcsec)

# output file name
file_output = 'm1.fits'

# name resolver
query_result = astroquery.simbad.Simbad.query_object (target)

# coordinate from Simbad
ra_str  = query_result['RA'][0]
dec_str = query_result['DEC'][0]

# using skycoord of astropy
coord = astropy.coordinates.SkyCoord (ra_str, dec_str, frame='icrs', \
                                      unit=(u_ha, u_deg) )

# coordinate in decimal degree
ra_deg  = coord.ra.deg
dec_deg = coord.dec.deg

# coordinate in hms and dms format
ra_hms  = coord.ra.to_string (u_ha)
dec_dms = coord.dec.to_string (u_deg, alwayssign=True)

# printing result
print (f"target: {target}")
print (f" RA  = {ra_hms:>14s} = {ra_deg:10.6f} deg")
print (f" Dec = {dec_dms:>14s} = {dec_deg:+10.6f} deg")

# getting a list of images
list_image = astroquery.skyview.SkyView.get_image_list (position=coord, \
                                                        survey=survey)

# printing available images
print (f"available images")
print (f" {list_image}")

# printing status
print (f"now, downloading image...")

# getting images
images = astroquery.skyview.SkyView.get_images (position=coord, \
                                                survey=survey, \
                                                pixels=fov_pixel)

# printing status
print (f"finished downloading image!")

# image
image  = images[0]
header = image[0].header
data   = image[0].data

# printing image information
print (image.info ())

# printing status
print (f"now, writing a FITS file '{file_output}'...")

# writing FITS file
hdu = astropy.io.fits.PrimaryHDU (data=data, header=header)
hdu.writeto (file_output)

# printing status
print (f"finished writing a FITS file '{file_output}'!")
