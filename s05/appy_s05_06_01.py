#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/13 10:34:16 (CST) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

# importing sys module
import sys

# importing numpy module
import numpy

# importing scipy module
import scipy.integrate

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg
import matplotlib.animation

#
# command-line argument analysis
#

# initialising a parser
desc   = 'solving equation of motion for a planet around a star'
parser = argparse.ArgumentParser (description=desc)

# adding arguments
parser.add_argument ('-x0', '--x0', type=float, default=0.0,
                     help='initial position in X in au (default: 0)')
parser.add_argument ('-y0', '--y0', type=float, default=1.0,
                     help='initial position in Y in au (default: 1)')
parser.add_argument ('-vx0', '--vx0', type=float, default=-1.0,
                     help='initial velocity in X in 2pi au/yr (default: -1)')
parser.add_argument ('-vy0', '--vy0', type=float, default=0.0,
                     help='initial velocity in Y in 2pi au/yr (default: 0)')
parser.add_argument ('-M', '--M', type=float, default=1.0,
                     help='mass of star (default: 1 solar mass)')
parser.add_argument ('-d', '--duration', type=float, default=10.0,
                     help='duration of simulation (default: 10 yr)')
parser.add_argument ('-i', '--interval', type=float, default=0.01,
                     help='time interval of data output (default: 0.01 yr)')
parser.add_argument ('-o', '--output', default='output.data', \
                     help='output file name (default: output.data)')

# parsing arguments
args = parser.parse_args ()

# parameters
qx0         = args.x0
qy0         = args.y0
vx0         = args.vx0
vy0         = args.vy0
Mstar       = args.M
duration    = args.duration
dt          = args.interval
file_output = args.output

#
# check of existence of output file
#

# making pathlib object
path_output = pathlib.Path (file_output)
if (path_output.exists ()):
    # printing message
    print (f'ERROR: output file "{file_output}" exists!')
    # stopping script
    sys.exit (0)

#
# constants
#

# unit of time: year
# unit of distance: au

# gravitational constant
GM = 4.0 * numpy.pi * numpy.pi * Mstar

#
# solving equation of motion
#

# function for solving equation of motion
def eqmo (t, y):
    r_cubed = ( y[0]**2 + y[2]**2 )**1.5
    dy      = numpy.zeros_like (y)
    dy[0]   = y[1]
    dy[1]   = -GM * y[0] / r_cubed
    dy[2]   = y[3]
    dy[3]   = -GM * y[2] / r_cubed
    return dy

# time to write position and velocity
n_step = int (duration / dt) + 1
t_eval = numpy.linspace (0.0, duration, n_step)

# initial values
y_init = (qx0, vx0 * numpy.sqrt (GM), qy0, vy0 * numpy.sqrt (GM))

# orbital integration
sol = scipy.integrate.solve_ivp (eqmo, [0.0, duration], y_init, \
                                 t_eval=t_eval, dense_output=True, \
                                 rtol=10**-6, atol=10**-9)

# results of orbital integration (positions and velocities)
qx = sol.y[0]
qy = sol.y[2]
vx = sol.y[1]
vy = sol.y[3]

#
# making output data file
#

# writing data to output file
with open (file_output, 'w') as fh_out:
    # writing header
    fh_out.write (f'#\n')
    fh_out.write (f'# Orbital motion of a planet around a star\n')
    fh_out.write (f'#\n')
    fh_out.write (f'#  parameters:\n')
    fh_out.write (f'#   mass of a star           : {Mstar}\n')
    fh_out.write (f'#   initial pos. of a planet : x0 = {qx0} au\n')
    fh_out.write (f'#   initial pos. of a planet : y0 = {qy0} au\n')
    fh_out.write (f'#   initial vel. of a planet : vx0 = {vx0} * 2pi au/yr\n')
    fh_out.write (f'#   initial vel. of a planet : vy0 = {vy0} * 2pi au/yr\n')
    fh_out.write (f'#   duration of simulation   : {duration} yr\n')
    fh_out.write (f'#   time step of simulation  : {dt}\n')
    fh_out.write (f'#   output file name         : {file_output}\n')
    fh_out.write (f'#\n')
    fh_out.write (f'#  format of data file\n')
    fh_out.write (f'#   time in yr\n')
    fh_out.write (f'#   x-coordinate on orbital plane in au\n')
    fh_out.write (f'#   y-coordinate on orbital plane in au\n')
    fh_out.write (f'#\n')
    # for each time step
    for i in range ( len (qx) ):
        # time
        t = i * dt
        # writing data
        fh_out.write (f'{t:15.9f}    {qx[i]:+15.9f} {qy[i]:+15.9f}\n')
