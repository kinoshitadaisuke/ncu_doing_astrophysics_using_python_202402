#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/27 16:03:54 (UT+8) daisuke>
#

# importing numpy
import numpy

# making a Numpy array (ndarray)
array_b = numpy.array ([10, 20, 30, 40, 50])

# type of "array_b"
type_array_b = type (array_b)

# dimension of "array_b"
ndim_array_b = array_b.ndim

# size of "array_b"
size_array_b = array_b.size

# shape of "array_b"
shape_array_b = array_b.shape

# data type of elements in "array_b"
dtype_array_b = array_b.dtype

# size of one element in "array_b"
itemsize_array_b = array_b.itemsize

# printing information
print (f'array_b:')
print (f'  values = {array_b}')
print (f'  type   = {type_array_b}')
print (f'information of "array_b":')
print (f'  ndim     = {ndim_array_b}')
print (f'  size     = {size_array_b}')
print (f'  shape    = {shape_array_b}')
print (f'  dtype    = {dtype_array_b}')
print (f'  itemsize = {itemsize_array_b} byte')
