#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/26 18:02:16 (UT+8) daisuke>
#

# importing numpy module
import numpy

# output file name
file_output = 'appy_s15_00_00.data'

# mean value of feature X for group A
mean_A_X = 1.0

# mean value of feature X for group B
mean_B_X = 3.0

# standard deviation of feature X for group A
stddev_A_X = 0.3

# standard deviation of feature X for group B
stddev_B_X = 0.3

# mean value of feature Y for group A
mean_A_Y = 9.0

# mean value of feature Y for group B
mean_B_Y = 7.0

# standard deviation of feature Y for group A
stddev_A_Y = 0.3

# standard deviation of feature Y for group B
stddev_B_Y = 0.3

# size of group A
n_A = 100

# size of group B
n_B = 100

# making a random number generator
rng = numpy.random.default_rng ()

# generating synthetic data
data_A_X = rng.normal (loc=mean_A_X, scale=stddev_A_X, size=n_A)
data_A_Y = rng.normal (loc=mean_A_Y, scale=stddev_A_Y, size=n_A)
data_B_X = rng.normal (loc=mean_B_X, scale=stddev_B_X, size=n_B)
data_B_Y = rng.normal (loc=mean_B_Y, scale=stddev_B_Y, size=n_B)

# modifying distribution
a = 0.03
b = 0.02
for i in range (n_A):
    data_A_X[i] = data_A_X[i] + a * i
    data_A_Y[i] = data_A_Y[i] + b * i
for i in range (n_B):
    data_B_X[i] = data_B_X[i] + a * i
    data_B_Y[i] = data_B_Y[i] + b * i

# opening file for writing
with open (file_output, 'w') as fh:
    # header of output file
    header = f'# value of feature X, value of feature Y, group\n'
    # writing header to output file
    fh.write (header)
    # writing synthetic data
    for i in range (n_A):
        record = f'{data_A_X[i]:8.4f}, {data_A_Y[i]:8.4f}, A\n'
        fh.write (record)
    for i in range (n_B):
        record = f'{data_B_X[i]:8.4f}, {data_B_Y[i]:8.4f}, B\n'
        fh.write (record)
