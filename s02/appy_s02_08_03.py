#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/23 12:45:05 (UT+8) daisuke>
#

# importing datetime module
import datetime

# timezone information (UT+0)
tzinfo = datetime.timezone (datetime.timedelta (0.0), name='UT+0')

# current time in UTC
time_now_utc = datetime.datetime.now (tz=tzinfo)

# printing result
print (f'current time in UTC = {time_now_utc}')
