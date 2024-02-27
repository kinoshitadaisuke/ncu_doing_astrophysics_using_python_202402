#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/27 16:10:30 (UT+8) daisuke>
#

# importing numpy module
import numpy

# random number generator
rng = numpy.random.Generator (numpy.random.Philox ())

# generating 100 random numbers of Gaussian distribution
# of mean of 100.0 and standard deviation of 10.0
array_x = rng.normal (100.0, 10.0, 100)

# printing generated random numbers
print (f'{array_x}')
