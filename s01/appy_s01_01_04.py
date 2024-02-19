#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/19 17:11:57 (UT+8) daisuke>
#

# two numbers
a = 23
b = 7

# calculation
quotient  = a // b
remainder = a % b

# printing result of calculation
print (f'a = {a}')
print (f'b = {b}')
print (f'quotient  = {quotient}')
print (f'remainder = {remainder}')
print (f'{b} * {quotient} + {remainder} = {b * quotient + remainder}')
