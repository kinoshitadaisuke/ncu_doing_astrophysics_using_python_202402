#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/12/14 12:50:58 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing argparse module
import argparse

# importing astropy module
import astropy.time
import astropy.units

# importing astroquery module
import astroquery.jplhorizons

# constructing parser object
descr  = "retrieving state vector of solar system object using JPL Horizons"
parser = argparse.ArgumentParser (description=descr)

# choices
list_method = [None, 'smallbody', 'designation', \
               'name', 'asteroid_name', 'comet_name']

# adding arguments
parser.add_argument ('-t', '--datetime', default='2024-01-01T12:00:00', \
                     help='date/time in UTC as YYYY-MM-DDThh:mm:ss format')
parser.add_argument ('-l', '--length', type=float, default=0.1, \
                     help='length of ephemeris retrieval in day (default: 0.1)')
parser.add_argument ('-d', '--dt', type=int, default=5, \
                     help='time step of ephemeris retrieval in hr (default: 5)')
parser.add_argument ('-o', '--obscode', default='@ssb', \
                     help='observatory code (default: solar system barycentre)')
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

# getting state vector
vector = obj.vectors ()

# printing state vector
print (vector)
