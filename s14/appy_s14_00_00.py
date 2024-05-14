#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/12/13 12:25:11 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing argparse module
import argparse

#
# command-line argument analysis
#

# constructing parser object
descr  = f"availability check of Python modules"
parser = argparse.ArgumentParser (description=descr)

# adding options
parser.add_argument ('module', type=str, nargs='+', \
                     help=f"module name (e.g. astropy)")

# analysis of command-line arguments
args = parser.parse_args ()

#
# input parameters
#

# list of module names for availability check
list_modules = args.module

#
# availability check of modules
#

for module in list_modules:
    # check of availability of rebound module
    try:
        # importing module
        imported = __import__ (module)
    except:
        # if module is not found, print an error message
        print (f"The module '{module}' is NOT installed on your computer.")
    else:
        # if module is found, print following message
        print (f"The module '{module}' is found on your computer.")
        print (f"{imported}")
    finally:
        # print that the check of availability of rebound module is finished
        print (f"A test of availability check of '{module}' module is now finished.")
        print (f"")
