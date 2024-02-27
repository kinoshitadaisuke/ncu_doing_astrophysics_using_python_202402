#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/27 16:06:44 (UT+8) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array (ndarray) using numpy.linspace ()
array_p = numpy.linspace (1000, 2000, 21)

# printing Numpy array
print (f'array_p:\n{array_p}')

# printing information
print (f'information:')
print (f'  ndim     = {array_p.ndim}')
print (f'  size     = {array_p.size}')
print (f'  shape    = {array_p.shape}')
print (f'  dtype    = {array_p.dtype}')
print (f'  itemsize = {array_p.itemsize} byte')
