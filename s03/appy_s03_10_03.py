#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/27 16:10:56 (UT+8) daisuke>
#

# importing numpy module
import numpy

# importing statistics module
import statistics

# random number generator
rng = numpy.random.Generator (numpy.random.PCG64DXSM ())

# generating 10^8 random numbers of Gaussian distribution 
# of mean = 10000.0 and stddev = 300.0
array_x = rng.normal (10000.0, 300.0, 10**8)

# printing generated random numbers
print (f'{array_x}')

# printing number of data
print (f'number of data = {len (array_x):g}')

# statistical values calculated by numpy module
mean_n     = numpy.mean (array_x)
median_n   = numpy.median (array_x)
variance_n = numpy.var (array_x)
stddev_n   = numpy.std (array_x)

# printing statistical values
print (f'statistical values by Numpy:')
print (f'  mean     = {mean_n:10.3f}')
print (f'  median   = {median_n:10.3f}')
print (f'  variance = {variance_n:10.3f}')
print (f'  stddev   = {stddev_n:10.3f}')

# finding maximum value
maximum = numpy.amax (array_x)

# finding minimum value
minimum = numpy.amin (array_x)

# printing maximum and minimum
print (f'maximum and minimum:')
print (f'  maximum = {maximum:10.3f}')
print (f'  minimum = {minimum:10.3f}')
