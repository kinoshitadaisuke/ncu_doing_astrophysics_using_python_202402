#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/29 13:55:29 (CST) daisuke>
#

# importing datetime module
import datetime

# importing astropy module
import astropy.time

# getting current date/time using datetime module
now_datetime = datetime.datetime.utcnow ()

# constructing Astropy's Time object from a string
now = astropy.time.Time (now_datetime, scale='utc')

# printing date/time
print (f'now  = {now}')
print (f'     = JD  {now.jd:14.6f}')
print (f'     = MJD {now.mjd:14.6f}')
