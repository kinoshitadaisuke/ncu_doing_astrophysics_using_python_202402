#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/21 15:26:44 (UT+8) daisuke>
#

# importing decimal module
import decimal

# calculation of sqrt (2.0)
a = decimal.Decimal ('2.0')
b = a.sqrt ()

# result of calculation
print (f'a = {a}')
print (f'b = sqrt (a) = sqrt ({a}) = {b}')

# calculation of log10 (12.3)
c = decimal.Decimal ('12.3')
d = c.log10 ()

# result of calculation
print (f'c = {c}')
print (f'd = log10 (c) = log10 ({c}) = {d}')
