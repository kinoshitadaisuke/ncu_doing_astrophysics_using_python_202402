#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/12/13 15:49:51 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing astropy module
import astropy.time

# importing astroquery module
import astroquery.jplhorizons

# target name
target = 'Sun'

# observatory (D35 ==> Lulin Observatory)
#
# To get a list of available observatory codes, visit following web page.
#   https://www.minorplanetcenter.net/iau/lists/ObsCodes.html
#
obs_site = 'D35'

# date/time
t  = astropy.time.Time ('2024-01-01T04:00:00', scale='utc', format='isot')
jd = t.jd

# sending a query to NASA/JPL Horizons system
obj = astroquery.jplhorizons.Horizons (id_type=None, id=target, \
                                       location=obs_site, epochs=jd)

# getting ephemerides
ephemerides = obj.ephemerides ()

# printing ephemerides
print (f'Target body    = {ephemerides["targetname"][0]}')
print (f'Observing site = {obs_site}')
print (f'Ephemerides:')
for data in ephemerides:
    # printing date/time
    print (f'  {data["datetime_str"]}')
    print (f'    RA         = {data["RA"]} [deg]')
    print (f'    Dec        = {data["DEC"]} [deg]')
    print (f'    Ecl Lon    = {data["ObsEclLon"]} [deg]')
    print (f'    Ecl Lat    = {data["ObsEclLat"]} [deg]')
    print (f'    Gal Lon    = {data["GlxLon"]} [deg]')
    print (f'    Gal Lat    = {data["GlxLat"]} [deg]')
    print (f'    Az         = {data["AZ"]} [deg]')
    print (f'    El         = {data["EL"]} [deg]')
    print (f'    V-band mag = {data["V"]} [mag]')
    print (f'    R          = {data["r"]} [au]')
    print (f'    Delta      = {data["delta"]} [au]')
