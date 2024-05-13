#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/13 19:30:25 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing astropy module
import astropy.coordinates

# importing astroquery module
import astroquery.esa.hubble

# construction of parser object for argparse
descr  = 'searching for HST data'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-r', '--radius', type=float, default=1.0, \
                     help='search radius in arcmin (default: 1)')
parser.add_argument ('-o', '--output', default='', \
                     help='output file name')
parser.add_argument ('ra', nargs=1, help='RA of centre of search field')
parser.add_argument ('dec', nargs=1, help='Dec of centre of search field')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
radius_arcmin = args.radius
file_output   = args.output
ra            = args.ra[0]
dec           = args.dec[0]

# units
u_ha     = astropy.units.hourangle
u_deg    = astropy.units.deg
u_arcmin = astropy.units.arcmin

# radius of search
radius = radius_arcmin * u_arcmin

# making esahubble object
esahubble = astroquery.esa.hubble.ESAHubble ()

# coordinate
coord = astropy.coordinates.SkyCoord (ra, dec, \
                                      unit=(u_ha, u_deg), frame='icrs')

# search
search_result = esahubble.cone_search (coordinates=coord, radius=radius, \
                                       filename=file_output)
