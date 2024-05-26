#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/26 18:36:19 (UT+8) daisuke>
#

# importing numpy module
import numpy

# output file name
file_output = 'appy_s15_01_00.data'

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

# opening file for writing
with open (file_output, 'w') as fh:
    # header of output file
    header = f'# value of feature X, value of feature Y, classification\n'
    # writing header to output file
    fh.write (header)
    # writing data to output file
    for i in range (data_0.shape[0]):
        record = f'{data_0[i,0]:8.4f} {data_0[i,1]:8.4f} A\n'
        fh.write (record)
    for i in range (data_1.shape[0]):
        record = f'{data_1[i,0]:8.4f} {data_1[i,1]:8.4f} B\n'
        fh.write (record)
