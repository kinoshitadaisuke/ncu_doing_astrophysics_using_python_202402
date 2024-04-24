#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/22 15:34:39 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing argparse module
import argparse

# importing astropy module
import astropy.units
import astropy.coordinates
import astropy.io.fits
import astropy.wcs
import astropy.visualization.mpl_normalize

# importing astroquery module
import astroquery.simbad
import astroquery.skyview

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# importing ssl module
import ssl

# allow insecure downloading
ssl._create_default_https_context = ssl._create_unverified_context

# units
u_ha  = astropy.units.hourangle
u_deg = astropy.units.deg

# list of surveys
list_surveys = ['DSS2 Blue', 'DSS2 Red', 'DSS2 IR', \
                'SDSSu', 'SDSSg', 'SDSSr', 'SDSSi', 'SDSSz']

# cmap
list_cmap = [
    'viridis', 'plasma', 'inferno', 'magma', 'cividis', 'gray', \
    'bone', 'pink', 'spring', 'summer', 'autumn', 'winter', \
    'cool', 'hot', 'copper', 'hsv', 'ocean', 'terrain', 'gnuplot', \
    'rainbow', 'turbo'
]

# construction of parser object for argparse
descr  = 'downloading DSS image and making a PNG file for a given target'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-t', '--target', help='target name')
parser.add_argument ('-f', '--fov', type=float, help='field-of-view in arcmin')
parser.add_argument ('-o', '--output', help='name of output file')
parser.add_argument ('-n', '--name', help='name of the object')
parser.add_argument ('-c', '--cmap', choices=list_cmap, default='gray', \
                     help='choice of cmap (default: gray)')
parser.add_argument ('-s', '--survey', choices=list_surveys, \
                     default='DSS2 Red', help='choice of survey')
parser.add_argument ('-r', '--resolution', type=float, default=225.0, \
                     help='resolution in DPI (default: 225)')

# command-line argument analysis
args = parser.parse_args ()

# target object name, and other information
target         = args.target
fov_arcmin     = args.fov
file_output    = args.output
name           = args.name
cmap           = args.cmap
survey         = args.survey
resolution_dpi = args.resolution

# field-of-view
fov_arcsec = fov_arcmin * 60.0
fov_pixel  = int (fov_arcsec)

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
wcs    = astropy.wcs.WCS (header)
data   = image[0].data

# printing image information
print (image.info ())

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111, projection=wcs)

# axes
ax.set_title (name)
ax.set_xlabel ('Right Ascension')
ax.set_ylabel ('Declination')

# plotting image
norm = astropy.visualization.mpl_normalize.ImageNormalize \
    ( stretch=astropy.visualization.HistEqStretch (data) )
im = ax.imshow (data, origin='lower', cmap=cmap, norm=norm)
fig.colorbar (im)

# saving file
fig.savefig (file_output, dpi=resolution_dpi)
