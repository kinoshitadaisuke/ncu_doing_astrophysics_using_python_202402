#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/03/13 14:57:42 (UT+8) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy
import scipy.linalg

# matrix A
A = numpy.array ( [ [4.0, 11.0], [2.0, 5.0] ] )

# printing matrix A
print (f'matrix A:\n{A}')

# determinant of matrix A
A_det = scipy.linalg.det (A)

# printing the determinant of matrix A
print (f'determinant of matrix A = {A_det}')
