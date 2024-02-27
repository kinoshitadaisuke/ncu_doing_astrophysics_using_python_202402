#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/27 16:06:58 (UT+8) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array (ndarray) using numpy.linspace ()
array_r = numpy.linspace (0, 10, 11)

# printing Numpy array
print (f'array_r:\n{array_r}')

# printing information
print (f'information:')
print (f'  ndim     = {array_r.ndim}')
print (f'  size     = {array_r.size}')
print (f'  shape    = {array_r.shape}')
print (f'  dtype    = {array_r.dtype}')
print (f'  itemsize = {array_r.itemsize} byte')

# appending one more data to "array_r"
array_r = numpy.append (array_r, 11.0)

# printing Numpy array
print (f'array_r:\n{array_r}')

# printing information
print (f'information:')
print (f'  ndim     = {array_r.ndim}')
print (f'  size     = {array_r.size}')
print (f'  shape    = {array_r.shape}')
print (f'  dtype    = {array_r.dtype}')
print (f'  itemsize = {array_r.itemsize} byte')
