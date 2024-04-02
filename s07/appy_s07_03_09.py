#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/04/02 10:49:03 (UT+8) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.time
import astropy.units

# units
u_hr = astropy.units.hr

# t_utc
t_utc = astropy.time.Time ('2024-04-02 08:00:00', format='iso', scale='utc')

# timezone
timezone_taiwan = astropy.time.TimezoneInfo (utc_offset=+8.0 * u_hr)
timezone_hawaii = astropy.time.TimezoneInfo (utc_offset=-10.0 * u_hr)

# date/time in Taiwan
t_taiwan = t_utc.to_datetime (timezone=timezone_taiwan)

# date/time in Hawaii
t_hawaii = t_utc.to_datetime (timezone=timezone_hawaii)

# printing results
print (f'date/time in UTC    = {t_utc}')
print (f'date/time in Taiwan = {t_taiwan}')
print (f'date/time in Hawaii = {t_hawaii}')
