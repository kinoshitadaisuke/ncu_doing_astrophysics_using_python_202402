#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/26 18:55:51 (UT+8) daisuke>
#

# importing numpy module
import numpy

# output file name
file_output = 'appy_s15_02_00.data'

# making a random number generator
rng = numpy.random.default_rng ()

# generating random numbers
mean_0a = numpy.array ([20.0, 10.0])
mean_0b = numpy.array ([30.0, 10.0])
mean_0c = numpy.array ([40.0, 10.0])
mean_1a = numpy.array ([20.0, 20.0])
mean_1b = numpy.array ([30.0, 20.0])
mean_1c = numpy.array ([40.0, 20.0])
covar_a = numpy.array ([ [5.5, 4.0], [4.0, 3.5] ])
covar_b = numpy.array ([ [5.5, -4.0], [-4.0, 3.5] ])
covar_c = numpy.array ([ [5.5, 4.0], [4.0, 3.5] ])
n_0     = 200
n_1     = 200
data_0a = rng.multivariate_normal (mean=mean_0a, cov=covar_a, size=n_0)
data_0b = rng.multivariate_normal (mean=mean_0b, cov=covar_b, size=n_0)
data_0c = rng.multivariate_normal (mean=mean_0c, cov=covar_c, size=n_0)
data_1a = rng.multivariate_normal (mean=mean_1a, cov=covar_a, size=n_1)
data_1b = rng.multivariate_normal (mean=mean_1b, cov=covar_b, size=n_1)
data_1c = rng.multivariate_normal (mean=mean_1c, cov=covar_c, size=n_1)
data_0  = numpy.concatenate ([data_0a, data_0b, data_0c])
data_1  = numpy.concatenate ([data_1a, data_1b, data_1c])

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
