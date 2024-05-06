#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/12/06 14:33:35 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

# importing numpy module
import numpy
import numpy.ma

# importing astropy module
import astropy
import astropy.io.fits

# construction pf parser object
descr  = 'calculating statistical information of pixel values in FITS files'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
choices_rejection = ['NONE', 'sigclip']
parser.add_argument ('-r', '--rejection', default='NONE', \
                     choices=choices_rejection, \
                     help='rejection algorithm (default: NONE)')
parser.add_argument ('-t', '--threshold', type=float, default=4.0, \
                     help='threshold for sigma clipping (default: 4.0)')
parser.add_argument ('-n', '--maxiters', type=int, default=10, \
                     help='maximum number of iterations (default: 10)')
parser.add_argument ('files', nargs='+', help='FITS files')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
rejection  = args.rejection
threshold  = args.threshold
maxiters   = args.maxiters
list_files = args.files

# printing information
print ("# Input parameters")
print ("#   rejection algorithm = %s" % rejection)
if not (rejection == 'NONE'):
    print ("#   threshold of sigma-clipping = %f" % threshold)
    print ("#   maximum number of iterations = %d" % maxiters)

# printing header
print ("#")
print ("# %-25s %8s %8s %8s %7s %8s %8s" \
       % ('file name', 'npix', 'mean', 'median', 'stddev', 'min', 'max') )
print ("#")

# scanning files
for file_fits in list_files:
    # making pathlib object
    path_fits = pathlib.Path (file_fits)
    
    # if the file is not a FITS file, then skip
    if not (path_fits.suffix == '.fits'):
        # printing message
        print ("# skipping file '%s'..." % file_fits)
        # skipping
        continue

    # opening FITS file
    with astropy.io.fits.open (file_fits) as hdu_list:
        # reading header of primary HDU
        header = hdu_list[0].header
        # reading image of primary HDU
        data0 = hdu_list[0].data
    
    # calculations

    # for no rejection algorithm
    if (rejection == 'NONE'):
        # making a masked array
        data1 = numpy.ma.array (data0, mask=False)
    # for sigma clipping algorithm
    elif (rejection == 'sigclip'):
        data1 = numpy.ma.array (data0, mask=False)
        # iterations
        for j in range (maxiters):
            # number of usable pixels of previous iterations
            npix_prev = len (numpy.ma.compressed (data1) )
            # calculation of median
            median = numpy.ma.median (data1)
            # calculation of standard deviation
            stddev = numpy.ma.std (data1)
            # lower threshold
            low = median - threshold * stddev
            # higher threshold
            high = median + threshold * stddev
            # making a mask
            mask = (data1 < low) | (data1 > high)
            # making a masked array
            data1 = numpy.ma.array (data0, mask=mask)
            # number of usable pixels
            npix_now = len (numpy.ma.compressed (data1) )
            # leaving the loop, if number of usable pixels do not change
            if (npix_now == npix_prev):
                break
        
    # calculation of mean, median, stddev, min, and max
    mean   = numpy.ma.mean (data1)
    median = numpy.ma.median (data1)
    stddev = numpy.ma.std (data1)
    vmin   = numpy.ma.min (data1)
    vmax   = numpy.ma.max (data1)

    # number of pixels
    npix = len (data1.compressed () )

    # file name
    filename = path_fits.name

    # printing result
    print ("%-27s %8d %8.2f %8.2f %7.2f %8.2f %8.2f" \
           % (filename, npix, mean, median, stddev, vmin, vmax) )
