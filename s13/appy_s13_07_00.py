#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/12 21:34:06 (UT+8) daisuke>
#

# importing astropy module
import astropy.coordinates

# importing astroquery module
import astroquery.esa.hubble

# output file name
file_output = 'hubble_search_result.vot.gz'

# units
u_ha     = astropy.units.hourangle
u_deg    = astropy.units.deg
u_arcmin = astropy.units.arcmin

# radius of search
radius = 0.5 * u_arcmin

# making esahubble object
esahubble = astroquery.esa.hubble.ESAHubble ()

# coordinate
coord = astropy.coordinates.SkyCoord ("04:16:34.49", "-24:04:58.7", \
                                      unit=(u_ha, u_deg), frame='icrs')

# search
search_result = esahubble.cone_search (coordinates=coord, radius=radius, \
                                       filename=file_output)
