#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/12/14 13:36:54 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.time

# importing astroquery module
import astroquery.jplhorizons

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# file name
file_fig = 'ai2023_s14_02_01.png'

# target list
# Jupiter and (624) Hektor
list_obj = ['599', 'Hektor']

# start date
date_start = '1800-01-01'

# end date
date_end   = '2200-01-01'

# step
step = '10d'

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Time [year]')
ax.set_ylabel ('Distance between Jupiter and (624) Hektor [au]')

# axes
ax.set_ylim (0.0, 10.0)
ax.grid ()

# getting positions of Jupiter
jupiter = astroquery.jplhorizons.Horizons (id=list_obj[0], id_type=None, \
                                           location='@ssb', \
                                           epochs={'start': date_start, \
                                                   'stop': date_end, \
                                                   'step': step})
vec_jupiter = jupiter.vectors ()

# getting positions of Hektor
hektor = astroquery.jplhorizons.Horizons (id=list_obj[1], id_type=None, \
                                          location='@ssb', \
                                          epochs={'start': date_start, \
                                                  'stop': date_end, \
                                                  'step': step})
vec_hektor = hektor.vectors ()

# date/time
datetime   = astropy.time.Time (vec_jupiter['datetime_jd'], format='jd')
datetime64 = numpy.array (datetime.isot, dtype='datetime64')

# distance between Jupiter and Hektor
delta_x = vec_jupiter['x'] - vec_hektor['x']
delta_y = vec_jupiter['y'] - vec_hektor['y']
delta_z = vec_jupiter['z'] - vec_hektor['z']
dist    = numpy.sqrt (delta_x**2 + delta_y**2 + delta_z**2)

# plotting data
ax.plot (datetime64, dist, \
         linestyle='-', linewidth=3, color='red', \
         label='Distance between Jupiter and Hektor')

# showing legend
ax.legend ()

# saving the plot into a file
fig.savefig (file_fig, dpi=100)
