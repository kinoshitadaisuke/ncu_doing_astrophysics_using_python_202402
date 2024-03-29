#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/03/28 08:57:10 (UT+8) daisuke>
#

# importing astropy module
import astropy.units
import astropy.coordinates

# importing astroquery module
import astroquery.simbad

# object name
object_name = 'Antares'

# units
u_ha  = astropy.units.hourangle
u_deg = astropy.units.deg

# name resolver
query_result = astroquery.simbad.Simbad.query_object (object_name)

# coordinate from Simbad
ra_str  = query_result['RA'][0]
dec_str = query_result['DEC'][0]

# making SkyCoord object of astropy
coord = astropy.coordinates.SkyCoord (ra_str, dec_str, frame='icrs', \
                                      unit=(u_ha, u_deg) )
(ra, dec) = coord.to_string (style='hmsdms').split ()

# printing result
print (f'Target name: "{object_name}"')
print (f'  RA  = {ra}')
print (f'  Dec = {dec}')
