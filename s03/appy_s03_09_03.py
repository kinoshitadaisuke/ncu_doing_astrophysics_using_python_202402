#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/27 16:10:21 (UT+8) daisuke>
#

# importing numpy module
import numpy

# random number generator
rng = numpy.random.Generator (numpy.random.PCG64DXSM ())

# generating 10 random numbers of uniform distribution between 0 and 1
array_x = rng.random (10)

# printing generated random numbers
print (f'{array_x}')
