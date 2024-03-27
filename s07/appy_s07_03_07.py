#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/29 14:03:17 (CST) daisuke>
#

# importing astropy module
import astropy.time
import astropy.units

# hour
u_hr = astropy.units.hr

# time t1
t1 = astropy.time.Time ('2023-12-31 18:00:00', format='iso', scale='utc')

# calculation of t1 + 12-hr
t2 = t1 + 12.0 * u_hr

# printing date/time
print (f't1              = {t1}')
print (f't2 = t1 + 12-hr = {t2}')
