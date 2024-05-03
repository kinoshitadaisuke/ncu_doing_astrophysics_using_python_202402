#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/03 10:39:44 (UT+8) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.time
import astropy.units

# output data file
file_output = 'appy_s12_00_00.data'

# constant
pi = numpy.pi

# units
u_sec = astropy.units.s
u_hr  = astropy.units.hr
u_day = astropy.units.day

#
# parameters for synthetic data generation
#

# amplitude (mag)
A = 0.5

# period (hr)
P = 2.0 * u_hr

# phase
delta = 2.0 * pi * 0.25

# average magnitude
mag_mean = 20.0

# start of observation
date_start = '2024-07-01T12:00:00'
t_start    = astropy.time.Time (date_start, scale='utc', format='isot')
mjd_start  = t_start.mjd

# end of observation
date_end = '2024-07-01T20:00:00'
t_end    = astropy.time.Time (date_end, scale='utc', format='isot')
mjd_end  = t_end.mjd

# exposure time (sec)
exptime = 120.0 * u_sec

# overhead time (sec)
overhead = 10.0 * u_sec

# interval between exposures (sec)
interval = exptime + overhead

# function for sine curve
def sine_curve (datetime, A, P, delta, mag_mean):
    # date/time
    t = astropy.time.Time (datetime)
    # calculation of magnitude at given time t
    mag = A * numpy.sin (2.0 * pi * t.mjd / P.to (u_day).value + delta) \
        + mag_mean
    # returning magnitude
    return (mag)

#
# generation of synthetic data
#

# time between start date/time and end date/time
n_data = int ( (mjd_end - mjd_start) * u_day / interval) + 1

# generating a numpy array for date/time
data_t = t_start + numpy.linspace (0.0, interval * (n_data - 1), n_data)

# generating a numpy array for magnitude
data_mag = sine_curve (data_t, A, P, delta, mag_mean)

# opening file for writing
with open (file_output, 'w') as fh:
    # head of data file
    header = f'#\n' \
        + f'#\n' \
        + f'# Synthetic data for period search\n' \
        + f'#\n' \
        + f'#\n' \
        + f'#  input parameters\n' \
        + f'#\n' \
        + f'#   start of obs. = {t_start} = MJD {t_start.mjd}\n' \
        + f'#   end of obs.   = {t_end} = MJD {t_end.mjd}\n' \
        + f'#   amplitude     = {A} mag\n' \
        + f'#   period        = {P}\n' \
        + f'#   delta         = {delta}\n' \
        + f'#   average mag.  = {mag_mean} mag\n' \
        + f'#   exposure time = {exptime}\n' \
        + f'#   overhead      = {overhead}\n' \
        + f'#\n' \
        + f'#  data format\n' \
        + f'#\n' \
        + f'#   date/time, MJD, magnitude\n' \
        + f'#\n'
    # writing input parameters to file
    fh.write (header)

    # writing generated synthetic data
    for i in range (len (data_t)):
        record = f'{data_t[i]} {data_t[i].mjd:15.9f} {data_mag[i]:9.6f}\n'
        fh.write (record)
