#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/15 08:34:04 (UT+8) daisuke>
#

# importing rebound module
import rebound

# name of simulation file
file_sim = 'star_planet.bin'

# reading a simulation from a file
sim = rebound.Simulation (file_sim)

# printing simulation object
print (sim)
