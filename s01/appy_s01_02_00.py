#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/19 17:12:54 (UT+8) daisuke>
#

# reading an integer number from keyboard typing
a_str = input ('Type one integer number: ')

# converting a string into integer
a = int (a_str)

# if and else statements
if (a % 2 == 0):
    print ("The number you type is an even number.")
else:
    print ("The number you type is an odd number.")
