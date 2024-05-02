#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/02 08:22:09 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing astropy module
import astropy.timeseries
import astropy.units

#
# command-line argument analysis
#

# constructing parser object
descr  = 'reading FITS files'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-o', type=str, default='out.data', \
                     help='output file name')
parser.add_argument ('files', type=str, nargs='+', help='input FITS files')

# parsing arguments
args = parser.parse_args ()

#
# input parameters
#

# output file name
file_output = args.o

# FITS files
files_fits = args.files

#
# reading file
#

# units
u_sec      = astropy.units.second
u_electron = astropy.units.electron

# opening file for writing
with open (file_output, 'w') as fh:
    # processing FITS files
    for file_fits in files_fits:
        # data stored in FITS file
        ts = astropy.timeseries.TimeSeries.read (file_fits, \
                                                 format='kepler.fits')

        # data
        data_datetime = ts['time']
        data_mjd      = ts.time.mjd
        data_flux     = ts['sap_flux'] * u_sec / u_electron
        data_err      = ts['sap_flux_err'] * u_sec / u_electron

        # printing data
        for i in range ( len (data_datetime) ):
            line = f"{data_datetime[i]} {data_mjd[i]:15.8f}" \
                + f" {data_flux[i]:15.6f} {data_err[i]:15.6f}\n"
            fh.write (line)
