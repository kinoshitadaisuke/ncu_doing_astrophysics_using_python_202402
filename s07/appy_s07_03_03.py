#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/03/28 08:55:07 (UT+8) daisuke>
#

# importing astropy module
import astropy.time

# getting current date/time
now = astropy.time.Time.now ()

# printing date/time
print (f'now  = {now}')
print (f'     = JD  {now.jd:14.6f}')
print (f'     = MJD {now.mjd:14.6f}')
