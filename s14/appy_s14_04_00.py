#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/12/14 19:55:57 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing rebound module
import rebound

# name of simulation file
file_sim = 'binary.bin'

# constructing a simulation object
sim = rebound.Simulation ()

# adding 2 solar mass star
sim.add (m=2.0)

# adding 1 solar mass star of a=20 au and e=0.6
sim.add (m=1.0, a=20.0, e=0.6)

# printing simulation object
print (sim)

# saving simulation into a file
sim.save_to_file (file_sim)
