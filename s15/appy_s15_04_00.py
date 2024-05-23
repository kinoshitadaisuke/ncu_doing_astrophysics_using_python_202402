#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/12/22 13:11:19 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing numpy module
import numpy

# making a random number generator
rng = numpy.random.default_rng ()

# generating random numbers
a_0     = 1.1
b_0     = 4.0
a_1     = 0.3
b_1     = 27.0
c_x     = 18.0
c_y     = 42.0
n_0     = 400
n_1     = 300
n_2     = 200
noise0  = rng.normal (loc=0.0, scale=2.0, size=n_0)
noise1  = rng.normal (loc=0.0, scale=2.0, size=n_1)
data_0x = rng.uniform (low=1.0, high=25.0, size=n_0)
data_0y = a_0 * data_0x + b_0 + noise0
data_1x = rng.uniform (low=2.0, high=12.0, size=n_1)
data_1y = a_1 * data_1x + b_1 + noise1
data_2x = rng.normal (loc=0.0, scale=2.0, size=n_2) + c_x
data_2y = rng.normal (loc=0.0, scale=4.0, size=n_2) + c_y

# printing data
print (f'# feature X, feature Y, classification')
for i in range (data_0x.size):
    print (f'{data_0x[i]:8.4f} {data_0y[i]:8.4f} A')
for i in range (data_1x.size):
    print (f'{data_1x[i]:8.4f} {data_1y[i]:8.4f} B')
for i in range (data_2x.size):
    print (f'{data_2x[i]:8.4f} {data_2y[i]:8.4f} C')
