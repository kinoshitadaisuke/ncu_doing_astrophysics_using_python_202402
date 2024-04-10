#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/12 14:03:50 (Taiwan_Standard_Time_UT+8) daisuke>
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
file_output = 'ai2023_s09_02_04.png'

# resolution in DPI
resolution_dpi = 225

# list to store data
list_ra_deg  = []
list_dec_deg = []

# counting number of data
n = 0

# opening file
with gzip.open (file_cat, 'rb') as fh:
    # reading data
    for line in fh:
        n += 1

# opening file
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
        list_ra_deg.append (coord.ra.degree)
        list_dec_deg.append (coord.dec.degree)

        # progress
        i += 1
        if (i % 5000 == 0):
            print ("progress: %6d / %6d" % (i, n) )

# making numpy arrays
data_ra_deg  = numpy.array (list_ra_deg)
data_dec_deg = numpy.array (list_dec_deg)

# deleting lists
list_ra_deg.clear ()
list_dec_deg.clear ()

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# setting for chunk size
matplotlib.rcParams['agg.path.chunksize'] = 10000

# axes
ax.grid ()
ax.set_title ('Hipparcos Catalogue', loc='right')
ax.set_xlabel ('Right Ascension')
ax.set_ylabel ('Declination')
ax.set_xlim (360.0, 0.0)
ax.set_ylim (-90.0, +90.0)
ax.set_xticks (numpy.linspace (0.0, 360.0, 13))
ax.set_yticks (numpy.linspace (-90.0, +90.0, 7))

# plotting data
hist = ax.hist2d (data_ra_deg, data_dec_deg, bins=(180, 90), \
                  cmap=matplotlib.cm.inferno)
fig.colorbar (hist[3], ax=ax)

# saving file
fig.savefig (file_output, dpi=resolution_dpi, bbox_inches="tight")
