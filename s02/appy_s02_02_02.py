#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/21 15:21:25 (UT+8) daisuke>
#

# importing argparse module
import argparse

# list of available operators
list_operators = ['+', '-', 'x', '/']

# making a parser object for command-line arguments analysis
parser = argparse.ArgumentParser (description='arithmetic calculations')

# adding arguments
parser.add_argument ('number1', type=float, help='number1')
parser.add_argument ('operator', choices=list_operators, help='operator')
parser.add_argument ('number2', type=float, help='number2')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
n1 = args.number1
n2 = args.number2
op = args.operator

# calculation
if (op == '+'):
    n3 = n1 + n2
elif (op == '-'):
    n3 = n1 - n2
elif (op == 'x'):
    n3 = n1 * n2
elif (op == '/'):
    n3 = n1 / n2

# printing result
print (f'{n1} {op} {n2} = {n3}')
