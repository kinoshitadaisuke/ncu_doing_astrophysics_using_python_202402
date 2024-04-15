#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/04/15 21:17:49 (UT+8) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.coordinates
import astropy.time
import astropy.units

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# date/time
date = astropy.time.Time ('2024-05-01 00:00:00')

# input data file name
file_input = 'asteroids_010000.data'

# output file name
file_output = 'appy_s09_00_15.png'

# resolution in DPI
resolution_dpi = 150

# making empty lists for storing data
list_ra_hr   = []
list_dec_deg = []

# units
u_deg = astropy.units.degree

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

# ecliptic plane
ecl_lon = numpy.linspace (0.001, 359.999, 1000) * u_deg
ecl_lat = numpy.zeros (1000) * u_deg
ecl_coord = astropy.coordinates.GeocentricMeanEcliptic (lon=ecl_lon, \
                                                        lat=ecl_lat, \
                                                        obstime=date)
ecl_ra  = ecl_coord.transform_to (astropy.coordinates.ICRS ()).ra.deg / 15.0
ecl_dec = ecl_coord.transform_to (astropy.coordinates.ICRS ()).dec.deg

# galactic plane
gal_lon = numpy.linspace (0.001, 359.999, 1000) * u_deg
gal_lat = numpy.zeros (1000) * u_deg
gal_coord = astropy.coordinates.Galactic (l=gal_lon, \
                                          b=gal_lat)
gal_ra  = gal_coord.transform_to (astropy.coordinates.ICRS ()).ra.deg / 15.0
gal_dec = gal_coord.transform_to (astropy.coordinates.ICRS ()).dec.deg


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
         linestyle='None', marker='o', markersize=2, \
         color='blue', alpha=0.2, \
         label='Asteroids')
ax.plot (ecl_ra, ecl_dec, \
         linestyle='None', marker='o', markersize=5, \
         color='yellow', alpha=0.5, \
         label='Ecliptic plane')
ax.plot (gal_ra, gal_dec, \
         linestyle='None', marker='o', markersize=5, \
         color='silver', alpha=0.5, \
         label='Galactic plane')
ax.legend ()

# saving file
fig.savefig (file_output, dpi=resolution_dpi)

# printing status
print (f"Finished generating a plot of asteroid distribution on the sky!")
