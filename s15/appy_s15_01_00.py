#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/12/21 19:41:10 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing numpy module
import numpy

# making a random number generator
rng = numpy.random.default_rng ()

# generating random numbers
mean_0 = numpy.array ([20.0, 10.0])
mean_1 = numpy.array ([15.0, 15.0])
covar  = numpy.array ([ [6.0, 4.0], [4.0, 4.0] ])
n_0    = 200
n_1    = 200
data_0 = rng.multivariate_normal (mean=mean_0, cov=covar, size=n_0)
data_1 = rng.multivariate_normal (mean=mean_1, cov=covar, size=n_1)

# printing data
print (f'# value of feature X, value of feature Y, classification')
for i in range (data_0.shape[0]):
    print (f'{data_0[i,0]:8.4f} {data_0[i,1]:8.4f} A')
for i in range (data_1.shape[0]):
    print (f'{data_1[i,0]:8.4f} {data_1[i,1]:8.4f} B')
