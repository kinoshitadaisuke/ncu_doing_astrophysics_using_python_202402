#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/27 16:07:55 (UT+8) daisuke>
#

# importing numpy module
import numpy

# making Numpy arrays
a = numpy.array ([1.0, 2.0])
b = numpy.array ([3.0, 4.0])

# printing a and b
print (f'a = {a}')
print (f'b = {b}')

# dot product of two vectors
dot = numpy.dot (a, b)

# printing dot product
print (f'dot = {dot}')

# inner product of two vectors
inner = numpy.inner (a, b)

# printing inner product
print (f'inner = {inner}')
