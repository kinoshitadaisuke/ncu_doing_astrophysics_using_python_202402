#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/30 23:11:20 (CST) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

# importing sys module
import sys

# importing datetime
import datetime

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# constructing a parser object
parser = argparse.ArgumentParser (description='Plotting date/time')

# adding arguments
parser.add_argument ('-o', '--output', default='output.png', \
                     help='output file name (default: output.png)')
parser.add_argument ('-r', '--resolution', type=float, default=225.0, \
                     help='resolution of plot in DPI (default: 225.0)')
parser.add_argument ('file', help='input data file name')

# parsing arguments
args = parser.parse_args ()

# parameters
file_input     = args.file
file_output    = args.output
resolution_dpi = args.resolution

# making a pathlib object for output file
path_output = pathlib.Path (file_output)

# check of existence of output file
if (path_output.exists ()):
    # printing a message
    print (f'ERROR: output file "{file_output}" exists!')
    # stopping the script
    sys.exit (0)

# check of extension of output file
if not ( (path_output.suffix == '.eps') \
         or (path_output.suffix == '.pdf') \
         or (path_output.suffix == '.png') \
         or (path_output.suffix == '.ps') ):
    # printing a message
    print (f'ERROR: output file must be either EPS or PDF or PNG or PS file.')
    # stopping the script
    sys.exit (0)

# making empty list and Numpy arrays
data_date  = numpy.array ([], dtype='datetime64[ms]')
data_mag   = numpy.array ([], dtype='float64')
data_error = numpy.array ([], dtype='float64')
    
# opening input file
with open (file_input, 'r') as fh_in:
    # reading data line-by-line
    for line in fh_in:
        # splitting data
        (date_str, mag_str, error_str, band, observer) = line.split ()
        # conversion from string to datetime, and then to datetime64
        date1 = datetime.datetime.strptime (date_str[:-4], '%Y-%m-%d')
        day   = float (date_str[-3:]) / 1000
        date2 = datetime.timedelta (days=day)
        date_datetime   = date1 + date2
        date_datetime64 = numpy.datetime64 (date_datetime, 'ms')
        # conversion from string to float
        mag   = float (mag_str)
        error = float (error_str)
        # appending data to list and Numpy arrays
        data_date  = numpy.append (data_date, date_datetime64)
        data_mag   = numpy.append (data_mag, mag)
        data_error = numpy.append (data_error, error)

# making a fig object
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# labels
ax.set_xlabel ('Date [YYYY-MM-DD]')
ax.set_ylabel ('V-band Magnitude [mag]')

# axis settings
ax.set_xlim (numpy.datetime64 ('2019-12-20'), numpy.datetime64 ('2020-04-01'))
ax.set_ylim (+1.9, +0.9)

# plotting data
ax.errorbar (data_date, data_mag, yerr=data_error, \
             linestyle='None', marker='o', markersize=5.0, color='red', \
             ecolor='black', elinewidth=2.0, capsize=5.0, \
             label='Apparent magnitude of Betelgeuse')

# legend
ax.legend (loc='upper right')

# formatting labels
fig.autofmt_xdate()

# saving the figure to a file
fig.savefig (file_output, dpi=resolution_dpi)
