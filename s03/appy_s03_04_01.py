#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/27 16:07:03 (UT+8) daisuke>
#

# importing numpy module
import numpy

# making Numpy arrays using numpy.linspace ()
array_s = numpy.linspace (0, 10, 11)
array_t = numpy.linspace (11, 15, 9)

# printing Numpy array
print (f'array_s:\n{array_s}')

# printing information
print (f'information:')
print (f'  ndim     = {array_s.ndim}')
print (f'  size     = {array_s.size}')
print (f'  shape    = {array_s.shape}')
print (f'  dtype    = {array_s.dtype}')
print (f'  itemsize = {array_s.itemsize} byte')

# printing Numpy array
print (f'array_t:\n{array_t}')

# printing information
print (f'information:')
print (f'  ndim     = {array_t.ndim}')
print (f'  size     = {array_t.size}')
print (f'  shape    = {array_t.shape}')
print (f'  dtype    = {array_t.dtype}')
print (f'  itemsize = {array_t.itemsize} byte')

# concatenating array_s and array_t, and creating array_u
array_u = numpy.concatenate ([array_s, array_t])

# printing Numpy array
print (f'array_u:\n{array_u}')

# printing information
print (f'information:')
print (f'  ndim     = {array_u.ndim}')
print (f'  size     = {array_u.size}')
print (f'  shape    = {array_u.shape}')
print (f'  dtype    = {array_u.dtype}')
print (f'  itemsize = {array_u.itemsize} byte')
