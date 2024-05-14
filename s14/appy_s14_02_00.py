#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/12/14 13:29:57 (Taiwan_Standard_Time_UT+8) daisuke>
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
file_fig = 'ai2023_s14_02_00.png'

# target list
# Earth, Mars
list_obj = ['399', '499']

# start date
date_start = '2015-01-01'

# end date
date_end   = '2040-01-01'

# step
step = '10d'

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Time [year]')
ax.set_ylabel ('Distance between Earth and Mars [au]')

# axes
ax.set_ylim (0, 3.5)
ax.grid ()

# getting positions of Earth
earth = astroquery.jplhorizons.Horizons (id=list_obj[0], id_type=None, \
                                         location='@ssb', \
                                         epochs={'start': date_start, \
                                                 'stop': date_end, \
                                                 'step': step})
vec_earth = earth.vectors ()

# getting positions of Mars
mars = astroquery.jplhorizons.Horizons (id=list_obj[1], id_type=None, \
                                        location='@ssb', \
                                        epochs={'start': date_start, \
                                                'stop': date_end, \
                                                'step': step})
vec_mars = mars.vectors ()

# date/time
datetime   = astropy.time.Time (vec_earth['datetime_jd'], format='jd')
datetime64 = numpy.array (datetime.isot, dtype='datetime64')

# distance between Earth and Mars
delta_x = vec_earth['x'] - vec_mars['x']
delta_y = vec_earth['y'] - vec_mars['y']
delta_z = vec_earth['z'] - vec_mars['z']
dist    = numpy.sqrt (delta_x**2 + delta_y**2 + delta_z**2)

# plotting data
ax.plot (datetime64, dist, \
         linestyle='-', linewidth=3, color='red', \
         label='Distance between Earth and Mars')

# showing legend
ax.legend ()

# saving the plot into a file
fig.savefig (file_fig, dpi=100)
