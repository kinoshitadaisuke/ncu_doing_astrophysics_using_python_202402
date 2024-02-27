#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/27 16:04:17 (UT+8) daisuke>
#

# importing numpy
import numpy

# making a Numpy array (ndarray)
array_e = numpy.array ([
    [
        [0.0, 1.0, 2.0],
        [-3.0, -4.0, -5.0],
        [6.0, -7.0, 8.0],
    ],
    [
        [9.1, -8.2, 7.3],
        [-6.4, 5.5, -4.6],
        [3.7, -2.8, 1.9],
    ],
])

# type of "array_e"
type_array_e = type (array_e)

# dimension of "array_e"
ndim_array_e = array_e.ndim

# size of "array_e"
size_array_e = array_e.size

# shape of "array_e"
shape_array_e = array_e.shape

# data type of elements in "array_e"
dtype_array_e = array_e.dtype

# size of one element in "array_e"
itemsize_array_e = array_e.itemsize

# printing information
print (f'array_e:')
print (f'  values:\n{array_e}')
print (f'  type   = {type_array_e}')
print (f'information of "array_e":')
print (f'  ndim     = {ndim_array_e}')
print (f'  size     = {size_array_e}')
print (f'  shape    = {shape_array_e}')
print (f'  dtype    = {dtype_array_e}')
print (f'  itemsize = {itemsize_array_e} byte')
