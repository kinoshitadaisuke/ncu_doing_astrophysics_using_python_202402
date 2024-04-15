#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/04/15 20:24:45 (UT+8) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.time

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# date/time
date = astropy.time.Time ('2024-05-01 00:00:00')

# input data file name
file_input = 'asteroids_000100.data'

# output file name
file_output = 'appy_s09_00_11.png'

# resolution in DPI
resolution_dpi = 150

# making empty lists for storing data
list_ra_hr   = []
list_dec_deg = []

# printing status
print (f'Now, reading data file...')

# opening data file
with open (file_input, 'r') as fh:
    # reading data file line-by-line
    for line in fh:
        # skipping line if the line starts with '#'
        if (line[0] == '#'):
            continue
        # splitting line
        (orbit, name) = line.split ('#')
        # extracting RA and Dec
        (ra_deg, dec_deg, ecl_lon_deg, ecl_lat_deg, \
         gal_lon_deg, gal_lat_deg, absmag, appmag) = orbit.split ()
        # conversion from string into float
        ra_deg  = float (ra_deg)
        dec_deg = float (dec_deg)
        # conversion from deg into hr for RA
        ra_hr = ra_deg / 15.0
        # appending data to lists
        list_ra_hr.append (ra_hr)
        list_dec_deg.append (dec_deg)

# making numpy arrays
array_ra_hr   = numpy.array (list_ra_hr)
array_dec_deg = numpy.array (list_dec_deg)

# printing status
print (f'Finished reading data file!')

# printing status
print (f"Now, generating a plot of asteroid distribution on the sky...")

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# axes
ax.grid ()
ax.set_xlim (24.0, 0.0)
ax.set_ylim (-90.0, +90.0)
ax.set_xticks (numpy.linspace (0, 24, 9))
ax.set_yticks (numpy.linspace (-90, 90, 7))
ax.set_xlabel ('Right Ascension [hr]')
ax.set_ylabel ('Declination [deg]')

# title
text_title = f"Distribution of asteroids on the sky on {date}"
ax.set_title (text_title)

# plotting data
ax.plot (array_ra_hr, array_dec_deg, \
         linestyle='None', marker='o', markersize=3, \
         color='blue', alpha=0.3, \
         label='Asteroids')
ax.legend ()

# saving file
fig.savefig (file_output, dpi=resolution_dpi)

# printing status
print (f"Finished generating a plot of asteroid distribution on the sky!")
