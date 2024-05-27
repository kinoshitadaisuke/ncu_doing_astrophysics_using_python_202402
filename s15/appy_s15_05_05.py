#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/27 15:36:37 (UT+8) daisuke>
#

# importing numpy module
import numpy

# output file name
file_output = 'appy_s15_05_05.data'

# making a random number generator
rng = numpy.random.default_rng ()

# generating random numbers
a_x     = 15.0
a_y     = 10.0
a_z     = 10.0
b_x     = 10.0
b_y     = 10.0
b_z     = 16.0
n_0     = 400
n_1     = 400
data_0x = rng.normal (loc=0.0, scale=2.0, size=n_0) + a_x
data_0y = rng.normal (loc=0.0, scale=2.0, size=n_0) + a_y
data_0z = rng.normal (loc=0.0, scale=2.0, size=n_0) + a_z
data_1x = rng.normal (loc=0.0, scale=2.0, size=n_1) + b_x
data_1y = rng.normal (loc=0.0, scale=2.0, size=n_1) + b_y
data_1z = rng.normal (loc=0.0, scale=2.0, size=n_1) + b_z

# opening file for writing
with open (file_output, 'w') as fh:
    # header of output file
    header = f'# feature X, feature Y, feature Z, classification\n'
    # writing header to output file
    fh.write (header)
    # writing data to output file
    for i in range (data_0x.size):
        record = f'{data_0x[i]:8.4f} {data_0y[i]:8.4f} {data_0z[i]:8.4f} A\n'
        fh.write (record)
    for i in range (data_1x.size):
        record = f'{data_1x[i]:8.4f} {data_1y[i]:8.4f} {data_1z[i]:8.4f} B\n'
        fh.write (record)
