#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/19 17:13:04 (UT+8) daisuke>
#

# reading an integer number from keyboard typing
a_str = input ('Type one integer number: ')

# converting a string into integer
a = int (a_str)

# if and else statements
if (a > 0):
    print ("The number you type is a positive number.")
elif (a < 0):
    print ("The number you type is a negative number.")
else:
    print ("The number you type is zero.")
