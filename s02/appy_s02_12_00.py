#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/27 08:57:54 (UT+8) daisuke>
#

# importing statistics module
import statistics

# generation of a synthetic data set
dataset1 = [ 6.0, 7.0, 8.0, 9.0, 9.0, \
             10.0, 10.0, 11.0, 11.0, 11.0, \
             12.0, 13.0, 14.0]

# printing data set
print (f'dataset1:\n{dataset1}')

# calculation of mean
mean = statistics.fmean (dataset1)

# printing calculated mean
print (f'mean of dataset1                          = {mean:6.3f}')

# calculation of median
median = statistics.median (dataset1)

# printing calculated median
print (f'median of dataset1                        = {median:6.3f}')

# calculation of mode
mode = statistics.mode (dataset1)

# printing calculated mode
print (f'mode of dataset1                          = {mode:6.3f}')

# calculation of sample variance
var = statistics.variance (dataset1)

# printing calculated sample variance
print (f'sample variance of dataset1               = {var:6.3f}')

# calculation of population variance
pvar = statistics.pvariance (dataset1)

# printing calculated population variance
print (f'population variance of dataset1           = {pvar:6.3f}')

# calculation of sample standard deviation
stddev = statistics.stdev (dataset1)

# printing calculated sample variance
print (f'sample standard deviation of dataset1     = {stddev:6.3f}')

# calculation of population standard deviation
pstddev = statistics.pstdev (dataset1)

# printing calculated population standard deviation
print (f'population standard deviation of dataset1 = {pstddev:6.3f}')
