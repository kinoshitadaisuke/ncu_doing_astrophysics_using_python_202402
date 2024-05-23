#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/12/22 15:18:44 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing numpy module
import numpy

# making a random number generator
rng = numpy.random.default_rng ()

# generating random numbers
a_x     = 15.0
a_y     = 10.0
a_z     = 10.0
b_x     = 10.0
b_y     = 10.0
b_z     = 28.0
n_0     = 400
n_1     = 400
data_0x = rng.normal (loc=0.0, scale=2.0, size=n_0) + a_x
data_0y = rng.normal (loc=0.0, scale=2.0, size=n_0) + a_y
data_0z = rng.normal (loc=0.0, scale=2.0, size=n_0) + a_z
data_1x = rng.normal (loc=0.0, scale=2.0, size=n_1) + b_x
data_1y = rng.normal (loc=0.0, scale=2.0, size=n_1) + b_y
data_1z = rng.normal (loc=0.0, scale=2.0, size=n_1) + b_z

# printing data
print (f'# feature X, feature Y, feature Z, classification')
for i in range (data_0x.size):
    print (f'{data_0x[i]:8.4f} {data_0y[i]:8.4f} {data_0z[i]:8.4f} A')
for i in range (data_1x.size):
    print (f'{data_1x[i]:8.4f} {data_1y[i]:8.4f} {data_1z[i]:8.4f} B')
