#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/21 15:23:14 (UT+8) daisuke>
#

# output file name
file_output = 'prime_numbers_1.data'

# start and end numbers
n_start = 2
n_end   = 10**5

# a list containing prime numbers
results = []

# function to check whether or not the number is a prime number
def is_prime_number (x):
    # resetting parameter "pn"
    pn = 1
    # examining if the number is divisible by numbers between 2 and (x-1)
    for k in range (2, x):
        # if the number is divisible by k
        if (x % k == 0):
            # then subtract 1 from "pn"
            pn -= 1
            # leaving from the loop
            break
    # returning number and a flag "pn"
    return (x, pn)

# numbers to be checked
for i in range (n_start, n_end + 1):
    # examining whether the number is a prime number
    result = is_prime_number (i)
    # appending result to the list "results"
    results.append (result)

# opening file for writing
with open (file_output, 'w') as fh_out:
    # for each number in the list "list_pn"
    for x, pn in results:
        # writing number to the file
        if (pn):
            fh_out.write (f'{x}\n')
