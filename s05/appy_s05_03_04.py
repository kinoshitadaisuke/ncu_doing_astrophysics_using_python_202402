#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/03/13 14:57:58 (UT+8) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy
import scipy.linalg

# matrix A
A = numpy.array ( [ [3.0, 1.0], [2.0, 2.0] ] )

# printing matrix A
print (f'matrix A:\n{A}')

# the other way to get eigenvalues of matrix A
eigenvalues = scipy.linalg.eigvals (A)

# printing eigenvalues of matrix A
print (f'eigenvalues of matrix A:\n{eigenvalues}')
