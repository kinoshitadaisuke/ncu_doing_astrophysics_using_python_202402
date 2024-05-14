#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/12/14 19:09:28 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing rebound module
import rebound

# name of simulation file
file_sim = 'star_planet.bin'

# reading a simulation from a file
sim = rebound.Simulation (file_sim)

# printing simulation object
print (sim)
