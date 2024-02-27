#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/27 16:10:45 (UT+8) daisuke>
#

# importing numpy module
import numpy

# importing statistics module
import statistics

# random number generator
rng = numpy.random.Generator (numpy.random.PCG64DXSM ())

# generating 10^7 random numbers of Gaussian distribution 
# of mean = 10000.0 and stddev = 500.0
array_x = rng.normal (10000.0, 300.0, 10**7)

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

# statistical values calculated by statistics module
mean_s     = statistics.fmean (array_x)
median_s   = statistics.median (array_x)
variance_s = statistics.pvariance (array_x)
stddev_s   = statistics.pstdev (array_x)

# printing statistical values
print (f'statistical values by statistics module:')
print (f'  mean     = {mean_s:10.3f}')
print (f'  median   = {median_s:10.3f}')
print (f'  variance = {variance_s:10.3f}')
print (f'  stddev   = {stddev_s:10.3f}')
