#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/27 16:10:52 (UT+8) daisuke>
#

# importing numpy module
import numpy

# importing statistics module
import statistics

# random number generator
rng = numpy.random.Generator (numpy.random.PCG64DXSM ())

# generating 10^8 random numbers of Gaussian distribution 
# of mean = 1000.0 and stddev = 25.0
array_x = rng.normal (1000.0, 25.0, 10**8)

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

# constructing a histogram
hist = numpy.histogram (array_x, bins=40, range=(900.0, 1100.0))

# printing histogram
print (f'histogram:')
for i in range (40):
    print (f'  {hist[1][i]:6.1f}-{hist[1][i]+10:6.1f} : {hist[0][i]:8d}')
