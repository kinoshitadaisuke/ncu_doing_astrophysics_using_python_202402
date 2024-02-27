#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/27 16:04:11 (UT+8) daisuke>
#

# importing numpy
import numpy

# making a Numpy array (ndarray)
array_d = numpy.array ([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
    [7.0, 8.0, 9.0],
])

# type of "array_d"
type_array_d = type (array_d)

# dimension of "array_d"
ndim_array_d = array_d.ndim

# size of "array_d"
size_array_d = array_d.size

# shape of "array_d"
shape_array_d = array_d.shape

# data type of elements in "array_d"
dtype_array_d = array_d.dtype

# size of one element in "array_d"
itemsize_array_d = array_d.itemsize

# printing information
print (f'array_d:')
print (f'  values:\n{array_d}')
print (f'  type   = {type_array_d}')
print (f'information of "array_d":')
print (f'  ndim     = {ndim_array_d}')
print (f'  size     = {size_array_d}')
print (f'  shape    = {shape_array_d}')
print (f'  dtype    = {dtype_array_d}')
print (f'  itemsize = {itemsize_array_d} byte')
