#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/29 13:59:49 (CST) daisuke>
#

# importing astropy module
import astropy.time

# time t1
t1 = astropy.time.Time ('2020-01-01 00:00:00', format='iso', scale='utc')

# time t2
t2 = astropy.time.Time ('2021-01-01 00:00:00', format='iso', scale='utc')

# time between t1 and t2
delta_t = t2 - t1

# printing date/time
print (f't1      = {t1}')
print (f't2      = {t2}')
print (f't2 - t1 = {delta_t} day = {delta_t.sec:g} sec')
