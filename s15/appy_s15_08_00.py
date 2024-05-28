#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/28 07:54:49 (UT+8) daisuke>
#

# importing numpy module
import numpy

# output file name
file_output = 'appy_s15_08_00.data'

# size of group A
n_A = 100

# size of group B
n_B = 200

# size of group C
n_C = 250

# number of background
n_bg = 300

# locations of groups A, B, C and background
x_mean_A =  30.0
y_mean_A =  40.0
x_mean_B =  70.0
y_mean_B =  60.0
x_mean_C = 120.0
y_mean_C = 120.0
x_min_bg =   0.0
x_max_bg = 150.0
y_min_bg =   0.0
y_max_bg = 150.0

# standard deviation of clustering data
stddev = 5.0

# creating a random number generator
rng = numpy.random.default_rng ()

# generating random numbers
data_A_x  = rng.normal (loc=x_mean_A, scale=stddev, size=n_A)
data_A_y  = rng.normal (loc=y_mean_A, scale=stddev, size=n_A)
data_B_x  = rng.normal (loc=x_mean_B, scale=stddev, size=n_B)
data_B_y  = rng.normal (loc=y_mean_B, scale=stddev, size=n_B)
data_C_x  = rng.normal (loc=x_mean_C, scale=stddev, size=n_C)
data_C_y  = rng.normal (loc=y_mean_C, scale=stddev, size=n_C)
data_bg_x = rng.uniform (low=x_min_bg, high=x_max_bg, size=n_bg)
data_bg_y = rng.uniform (low=y_min_bg, high=y_max_bg, size=n_bg)

# opening file for writing
with open (file_output, 'w') as fh:
    # header of output file
    header = f'# feature x, feature y, group\n'
    # writing header to output file
    fh.write (header)
    # writing data to output file
    for i in range (data_A_x.size):
        record = f'{data_A_x[i]:8.3f} {data_A_y[i]:8.3f} A\n'
        fh.write (record)
    for i in range (data_B_x.size):
        record = f'{data_B_x[i]:8.3f} {data_B_y[i]:8.3f} B\n'
        fh.write (record)
    for i in range (data_C_x.size):
        record = f'{data_C_x[i]:8.3f} {data_C_y[i]:8.3f} C\n'
        fh.write (record)
    for i in range (data_bg_x.size):
        record = f'{data_bg_x[i]:8.3f} {data_bg_y[i]:8.3f} background\n'
        fh.write (record)
