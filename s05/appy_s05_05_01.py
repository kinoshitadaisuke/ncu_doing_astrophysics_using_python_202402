#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/11 15:32:12 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy
import scipy.integrate

# function of a curve
def curve (x):
    # curve
    y = numpy.sqrt (4.0 - x**2)
    # returning a value
    return (y)

# range of integration
x0 = 0.0
x1 = 2.0

# numerical integration
result = scipy.integrate.quad (curve, x0, x1)

# printing result of numerical integration
print (f'integ. of (4-x^2)^0.5 from 0 to 2 = {result[0]} +/- {result[1]}')
