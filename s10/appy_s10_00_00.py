#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/16 20:00:29 (Taiwan_Standard_Time_UT+8) daisuke>
#

# check of availability of astropy module
try:
    # importing astropy module
    import astropy
except:
    # if astropy module is not installed, print following message
    print (f"The module 'astropy' is not installed on your computer.")
    print (f"The module 'astropy' is required for this session.")
    print (f"Visit following web page and install the package 'astropy'.")
    print (f"  https://docs.astropy.org/")
    print (f"After the installation, try to run this script again.")
else:
    # if astropy module is found, print following message
    print (f"The module 'astropy' is found on your computer.")
finally:
    # print that the check of availability of astropy module is finished
    print (f"An availability check of 'astropy' module is now finished.")
