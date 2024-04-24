#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/22 14:51:55 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing argparse module
import argparse

# importing astropy module
import astropy.units
import astropy.coordinates

# importing astroquery module
import astroquery.simbad

# units
u_ha  = astropy.units.hourangle
u_deg = astropy.units.deg

# construction of parser object for argparse
descr  = 'name resloving using Simbad'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('target', type=str, nargs='+', help='target name')

# command-line arguments analysis
args = parser.parse_args ()

# list of target object names
list_target = args.target

# processing for each target
for target in list_target:
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
