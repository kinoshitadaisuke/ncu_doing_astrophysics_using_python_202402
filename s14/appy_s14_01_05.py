#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/12/14 11:57:43 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing argparse module
import argparse

# importing astropy module
import astropy.time
import astropy.units

# importing astroquery module
import astroquery.jplhorizons

# constructing parser object
descr  = "retrieving position of a solar system object using JPL Horizons"
parser = argparse.ArgumentParser (description=descr)

# choices
list_method = [None, 'smallbody', 'designation', \
               'name', 'asteroid_name', 'comet_name']

# adding arguments
parser.add_argument ('-t', '--datetime', default='2024-01-01T12:00:00', \
                     help='date/time in UTC as YYYY-MM-DDThh:mm:ss format')
parser.add_argument ('-l', '--length', type=float, default=10.0, \
                     help='length of ephemeris retrieval in day (default: 10)')
parser.add_argument ('-d', '--dt', type=int, default=1, \
                     help='time step of ephemeris retrieval in hr (default: 1)')
parser.add_argument ('-o', '--obscode', default='D35', \
                     help='observatory code (default: D35)')
parser.add_argument ('-m', '--search-method', default=None, \
                     choices=list_method, \
                     help='target search method (default: None)')
parser.add_argument ('target', nargs=1, default='Sun', \
                     help='target object name (default: Sun)')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
datetime      = args.datetime
duration_day  = args.length
timestep_hr   = args.dt
obscode       = args.obscode
search_method = args.search_method
target        = args.target[0]

# units
u_hr  = astropy.units.hr
u_day = astropy.units.day

# date/time
t_start = astropy.time.Time (datetime, scale='utc', format='isot')
t_end   = t_start + duration_day * u_day

# time step
timestep_str = f'{timestep_hr}h'

# sending a query to NASA/JPL Horizons system
obj = astroquery.jplhorizons.Horizons (id_type=search_method, \
                                       id=target, \
                                       location=obscode, \
                                       epochs={'start': t_start.isot, \
                                               'stop': t_end.isot, \
                                               'step': timestep_str})

# getting ephemerides
ephemerides = obj.ephemerides ()

# printing ephemerides
print (f'Target body    = {ephemerides["targetname"][0]}')
print (f'Observing site = {obscode}')
print (f'Ephemerides:')
for data in ephemerides:
    # V-band apparent magnitude
    try:
        Vmag = data["V"]
    except:
        Vmag = data["Tmag"]
    # printing date/time
    print (f' {data["datetime_str"]} (V = {Vmag} mag)')
    # printing positions
    print (f'  Equatorial:  (RA,Dec)=({data["RA"]:10.6f}, {data["DEC"]:+10.6f}) [deg]')
    print (f'  Ecliptic:   (Lon,Lat)=({data["ObsEclLon"]:10.6f}, {data["ObsEclLat"]:+10.6f}) [deg]')
    print (f'  Galactic:   (Lon,Lat)=({data["GlxLon"]:10.6f}, {data["GlxLat"]:+10.6f}) [deg]')
    print (f'  Horizontal: (Lon,Lat)=({data["AZ"]:10.6f}, {data["EL"]:+10.6f}) [deg]')
