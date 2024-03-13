#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/09 22:44:55 (CST) daisuke>
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
