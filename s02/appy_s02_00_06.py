#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/21 15:20:05 (UT+8) daisuke>
#

# importing os module
import os

# obtaining the value of environmental variable "SHELL"
env_shell = os.environ['SHELL']

# printing the value of environmental variable "SHELL"
print (f'SHELL = {env_shell}')
