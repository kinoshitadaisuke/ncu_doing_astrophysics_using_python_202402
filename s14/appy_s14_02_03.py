#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/12/14 18:03:42 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing astropy module
import astropy.time

# importing astroquery module
import astroquery.jplhorizons

# date/time
t_str = '2024-01-01T12:00:00'
t     = astropy.time.Time (t_str, scale='utc', format='isot')

# target list
# Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto
list_obj = ['10', '199', '299', '399', '499', '599', '699', '799', '899', '999']

# names
names = {
    '10':  'Sun',
    '199': 'Mercury',
    '299': 'Venus',
    '399': 'Earth',
    '499': 'Mars',
    '599': 'Jupiter',
    '699': 'Saturn',
    '799': 'Uranus',
    '899': 'Neptune',
    '999': 'Pluto'
}

# printing header
print (f"Positions of the Sun and planets on {t}:")

# getting positions of the Sun and planets
for i in range ( len (list_obj) ):
    # querying JPL Horizons
    obj = astroquery.jplhorizons.Horizons (id=list_obj[i], \
                                           id_type=None, \
                                           location='@ssb', \
                                           epochs=t.jd)

    # state vector of the target object
    vec = obj.vectors ()

    # printing position
    print (f"  {names[list_obj[i]]:10s}:", \
           f"x={vec['x'][0]:+13.8f},", \
           f"y={vec['y'][0]:+13.8f},", \
           f"z={vec['z'][0]:+13.8f}")
