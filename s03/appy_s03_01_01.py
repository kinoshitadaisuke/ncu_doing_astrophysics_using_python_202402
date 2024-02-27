#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/27 16:04:02 (UT+8) daisuke>
#

# importing numpy
import numpy

# making a Numpy array (ndarray)
array_c = numpy.array ([10.0, 20.1, 30.2, 40.3, 50.4])

# type of "array_c"
type_array_c = type (array_c)

# dimension of "array_c"
ndim_array_c = array_c.ndim

# size of "array_c"
size_array_c = array_c.size

# shape of "array_c"
shape_array_c = array_c.shape

# data type of elements in "array_c"
dtype_array_c = array_c.dtype

# size of one element in "array_c"
itemsize_array_c = array_c.itemsize

# printing information
print (f'array_c:')
print (f'  values = {array_c}')
print (f'  type   = {type_array_c}')
print (f'information of "array_c":')
print (f'  ndim     = {ndim_array_c}')
print (f'  size     = {size_array_c}')
print (f'  shape    = {shape_array_c}')
print (f'  dtype    = {dtype_array_c}')
print (f'  itemsize = {itemsize_array_c} byte')
