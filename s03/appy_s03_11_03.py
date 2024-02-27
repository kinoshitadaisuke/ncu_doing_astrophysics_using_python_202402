#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/27 16:11:20 (UT+8) daisuke>
#

# importing numpy module
import numpy

# importing statistics module
import statistics

# random number generator
rng = numpy.random.Generator (numpy.random.PCG64DXSM ())

# generating 50 random numbers of Gaussian distribution 
# of mean = 1000.0 and stddev = 100.0
array_raw = rng.normal (1000.0, 100.0, 50)

# adding outliers
array_raw[20] += 3000.0
array_raw[30] += 5000.0

# printing generated random numbers
print (f'{array_raw}')

# printing number of data
print (f'number of data = {len (array_raw):g}')

# statistical values calculated by numpy module
mean_n     = numpy.mean (array_raw)
median_n   = numpy.median (array_raw)
variance_n = numpy.var (array_raw)
stddev_n   = numpy.std (array_raw)

# printing statistical values
print (f'statistical values of raw data:')
print (f'  mean     = {mean_n:10.3f}')
print (f'  median   = {median_n:10.3f}')
print (f'  variance = {variance_n:10.3f}')
print (f'  stddev   = {stddev_n:10.3f}')

# finding data outside of [ mean - 3.0 * stddev, mean + 3.0 * stddev ]
limit_low  = median_n - 3.0 * stddev_n
limit_high = median_n + 3.0 * stddev_n

# making an empty array for a mask
mask = numpy.array ([])

# examining data
for i in range (len (array_raw)):
    if ( (array_raw[i] < limit_low) or (array_raw[i] > limit_high) ):
        mask = numpy.append (mask, True)
    else:
        mask = numpy.append (mask, False)

# printing mask
print (f'mask:\n{mask}')

# making masked array
array_masked = numpy.ma.array (array_raw, mask=mask)

# printing masked array
print (f'array_masked:\n{array_masked}')

# calculation of statistical values
mean_m     = numpy.ma.mean (array_masked)
median_m   = numpy.ma.median (array_masked)
variance_m = numpy.ma.var (array_masked)
stddev_m   = numpy.ma.std (array_masked)

# printing statistical values
print (f'statistical values of masked data:')
print (f'  mean     = {mean_m:10.3f}')
print (f'  median   = {median_m:10.3f}')
print (f'  variance = {variance_m:10.3f}')
print (f'  stddev   = {stddev_m:10.3f}')
