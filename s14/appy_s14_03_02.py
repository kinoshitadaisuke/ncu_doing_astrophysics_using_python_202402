#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/20 19:47:39 (UT+8) daisuke>
#

# importing numpy module
import numpy

# importing rebound module
import rebound

# name of simulation file
file_sim = 'star_planet.bin'

# name of output file
file_out = 'star_planet.data'

# reading a simulation from a file
sim = rebound.Simulation (file_sim)

# moving to centre of momentum frame
sim.move_to_com ()

# particles in simulation
ps = sim.particles

# parameters for simulation
#  for G=1, one year is equal to 2 pi
#  0.01 time unit = 365.25 / (2 pi) * 0.01 = 0.58 day
year       = 2.0 * numpy.pi
t_interval = 0.01
n_output   = 1000

# settings for orbital integration
sim.integrator = 'ias15'

# opening file for writing
with open (file_out, 'w') as fh:
    # header of output file
    header = f"# days from start of simulation, star's (x, y, z), planet's (x, y, z)\n"
    # writing header to file
    fh.write (header)

    # orbital integration
    for i in range (n_output):
        # time
        t     = t_interval * i
        t_day = t_interval * i * 365.25 / (2.0 * numpy.pi)
        # orbital integration for a time step
        sim.integrate (t)
        # position of star at time t
        star_x = ps[0].x
        star_y = ps[0].y
        star_z = ps[0].z
        # position of planet at time t
        planet_x = ps[1].x
        planet_y = ps[1].y
        planet_z = ps[1].z
        # position of star and planet at time t
        record = f"{t_day:12.6f}" \
            + f" {star_x:+10.6f} {star_y:+10.6f} {star_z:+10.6f}" \
            + f"{planet_x:+10.6f} {planet_y:+10.6f} {planet_z:+10.6f}\n"
        # writing position of star and planet to file
        fh.write (record)
