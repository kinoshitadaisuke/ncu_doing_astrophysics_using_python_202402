#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/21 23:12:47 (Taiwan_Standard_Time_UT+8) daisuke>
#

# check of availability of rebound module
try:
    # importing astroquery module
    import astroquery
except:
    # if astroquery module is not installed, print an error message
    print (f"The module 'astroquery' is not installed on your computer.")
    print (f"The module 'astroquery' is required for this session.")
    print (f"Visit following web page and install the package 'astroquery'.")
    print (f"  https://astroquery.readthedocs.io/")
    print (f"After the installation, try to run this script again.")
else:
    # if astroquery module is found, print following message
    print (f"The module 'astroquery' is found on your computer.")
finally:
    # print that the check of availability of astroquery module is finished
    print (f"An availability check of 'astroquery' module is now finished.")
