#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/12 12:57:09 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing gzip module
import gzip

# importing numpy module
import numpy

# importing astropy module
import astropy.units
import astropy.coordinates

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# units
u_ha  = astropy.units.hourangle
u_deg = astropy.units.deg
u_rad = astropy.units.rad

# input catalogue file
file_cat    = 'hip2.data.gz'

# output image file
file_output = 'ai2023_s09_02_02.png'

# resolution in DPI
resolution_dpi = 225

# list to store data
list_ra_rad  = []
list_dec_rad = []

# counting number of data
n = 0

# opening file for counting number of data
with gzip.open (file_cat, 'rb') as fh:
    # reading data
    for line in fh:
        n += 1

# opening file for reading data
with gzip.open (file_cat, 'rb') as fh:
    # reading data
    i = 0
    for line in fh:
        # decoding raw byte data
        line = line.decode ('utf-8')
        
        # extracting data
        ra_str  = line[15:28].strip ()
        dec_str = line[29:42].strip ()
        mag_str = line[129:136].strip ()
        BV_str  = line[152:158].strip ()

        # skipping, if any of data is missing.
        if ( (ra_str == '') or (dec_str == '') or (mag_str == '') \
             or (BV_str == '') ):
            continue
        # conversion from string to float
        ra_rad  = float (ra_str)
        dec_rad = float (dec_str)
        mag     = float (mag_str)
        BV      = float (BV_str)
    
        # coordinate
        coord = astropy.coordinates.SkyCoord (ra_rad, dec_rad, \
                                              frame=astropy.coordinates.ICRS, \
                                              unit=u_rad)

        # appending data to lists
        ra_rad_wrap = coord.ra.wrap_at (180 * u_deg).radian
        list_ra_rad.append (ra_rad_wrap)
        list_dec_rad.append (coord.dec.radian)

        # progress
        i += 1
        if (i % 5000 == 0):
            print ("progress: %6d / %6d" % (i, n) )

# making numpy arrays
data_ra_rad = numpy.array (list_ra_rad)
list_ra_rad.clear ()
data_dec_rad = numpy.array (list_dec_rad)
list_dec_rad.clear ()

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111, projection="aitoff")

# setting for chunk size
matplotlib.rcParams['agg.path.chunksize'] = 10000

# axes
ax.grid ()
ax.set_title ('Hipparcos Catalogue', loc='right')
ax.set_xlabel ('Right Ascension')
ax.set_ylabel ('Declination')

# plotting data
ax.plot (data_ra_rad, data_dec_rad, \
         linestyle='None', marker='.', markersize=1, \
         color='blue', fillstyle='full', alpha=0.1)

# saving file
fig.savefig (file_output, dpi=resolution_dpi, bbox_inches="tight")
