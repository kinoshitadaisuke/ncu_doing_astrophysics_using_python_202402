#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/21 15:23:39 (UT+8) daisuke>
#

# importing datetime module
import datetime

# time offset from UTC
dt = datetime.timedelta (hours=8)

# current time in local time
time_now_local = datetime.datetime.now (tz=datetime.timezone (dt))

# printing result
print (f'current local time: {time_now_local}')
