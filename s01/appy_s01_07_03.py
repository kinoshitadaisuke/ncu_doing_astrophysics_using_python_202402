#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/19 17:15:24 (UT+8) daisuke>
#

# importing sys module
import sys

# printing a message
print (f'This Python script adds two integers and print result of calculation.')

# receiving two numbers
a = input ('input first integer: ')
b = input ('input second integer: ')

# conversion of string "a" into integer
try:
    # conversion
    a = int (a)
except:
    # printing a message
    print (f'Error: string "{a}" cannot be converted into an integer.')
    # exit the script
    sys.exit (1)
else:
    print (f'string "{a}" is successfully converted into an integer.')

# conversion of string "b" into integer
try:
    # conversion
    b = int (b)
except:
    # printing a message
    print (f'Error: string "{b}" cannot be converted into an integer.')
    # exit the script
    sys.exit (1)
else:
    print (f'string "{b}" is successfully converted into an integer.')

# calculation
c = a + b

# printing result of calculation
print (f'{a} + {b} = {c}')
