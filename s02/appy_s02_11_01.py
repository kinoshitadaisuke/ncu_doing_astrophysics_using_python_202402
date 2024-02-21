#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/21 15:25:27 (UT+8) daisuke>
#

# importing random module
import random

# initialisation of random number generator
random.seed ()

#
# generating 10 random numbers of uniform distribution between 100 and 200
#

# parameters
a = 100.0
b = 200.0

# generating 10 random numbers
print (f'10 random numbers of uniform distribution between {a} and {b}')
for i in range (10):
    # generation of a random number of uniform distribution between 100 and 200
    r = random.uniform (a, b)
    # printing generated random number
    print (f'  {r:15.11f}')
