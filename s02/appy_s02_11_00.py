#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/21 15:25:22 (UT+8) daisuke>
#

# importing random module
import random

# initialisation of random number generator
random.seed ()

#
# generating 10 random numbers of uniform distribution between 0 and 1
#

# generating 10 random numbers
print (f'10 random numbers of uniform distribution between 0 and 1')
for i in range (10):
    # generation of a random number of uniform distribution between 0 and 1
    r = random.random ()
    # printing generated random number
    print (f'  {r:15.13f}')
