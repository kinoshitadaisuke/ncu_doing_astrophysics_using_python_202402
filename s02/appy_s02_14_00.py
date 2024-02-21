#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/21 15:27:10 (UT+8) daisuke>
#

# importing uncertainties module
import uncertainties

# quantity "a": 6.0 +/- 0.3
a = uncertainties.ufloat (6.0, 0.3)

# quantity "b": 9.0 +/- 0.4
b = uncertainties.ufloat (9.0, 0.4)

# calculation of a + b
c = a + b

# printing value of "c"
print (f'c = a + b = {a} + {b} = {c}')
