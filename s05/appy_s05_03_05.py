#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/09 22:49:47 (CST) daisuke>
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

# eigenvalues and eigenvectors of matrix A
eigenvalvec = scipy.linalg.eig (A)

# printing eigenvalues and eigenvectors of matrix A
print (f'eigenvalues of matrix A:\n{eigenvalvec[0]}')
print (f'eigenvectors of matrix A:\n{eigenvalvec[1]}')

# making matrix P
P = numpy.array ( [ eigenvalvec[1][0], eigenvalvec[1][1] ] )
print (f'P:\n{P}')

# making matrix P^-1
P_inv = scipy.linalg.inv (P)

# printing matrix P^-1
print (f'P_inv:\n{P_inv}')

# calculation of P^-1 A P
D = P_inv @ A @ P

# printing diagonalised matrix D
print (f'D = P_inv @ A @ P:\n{D}')
