#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/27 16:10:25 (UT+8) daisuke>
#

# importing numpy module
import numpy

# SFC64 random number generator
rng = numpy.random.Generator (numpy.random.SFC64 ())

# generating 10 random numbers of uniform distribution between 100 and 200
array_x = rng.uniform (1000.0, 2000.0, 30)

# printing generated random numbers
print (f'{array_x}')
