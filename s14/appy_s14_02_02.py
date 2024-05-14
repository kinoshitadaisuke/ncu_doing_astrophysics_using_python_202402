#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/12/14 13:45:30 (Taiwan_Standard_Time_UT+8) daisuke>
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
file_fig = 'ai2023_s14_02_02.png'

# target list
# Neptune and Pluto
list_obj = ['899', '999']

# start date
date_start = '1700-02-01'

# end date
date_end   = '2099-12-01'

# step
step = '30d'

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Time [year]')
ax.set_ylabel ('Distance between Neptune and Pluto [au]')

# axes
ax.set_ylim (0.0, 100.0)
ax.grid ()

# getting positions of Neptune
neptune = astroquery.jplhorizons.Horizons (id=list_obj[0], id_type=None, \
                                           location='@ssb', \
                                           epochs={'start': date_start, \
                                                   'stop': date_end, \
                                                   'step': step})
vec_neptune = neptune.vectors ()

# getting positions of Pluto
pluto = astroquery.jplhorizons.Horizons (id=list_obj[1], id_type=None, \
                                          location='@ssb', \
                                          epochs={'start': date_start, \
                                                  'stop': date_end, \
                                                  'step': step})
vec_pluto = pluto.vectors ()

# date/time
datetime   = astropy.time.Time (vec_neptune['datetime_jd'], format='jd')
datetime64 = numpy.array (datetime.isot, dtype='datetime64')

# distance between Neptune and Pluto
delta_x = vec_neptune['x'] - vec_pluto['x']
delta_y = vec_neptune['y'] - vec_pluto['y']
delta_z = vec_neptune['z'] - vec_pluto['z']
dist    = numpy.sqrt (delta_x**2 + delta_y**2 + delta_z**2)

# plotting data
ax.plot (datetime64, dist, \
         linestyle='-', linewidth=3, color='red', \
         label='Distance between Neptune and Pluto')

# showing legend
ax.legend ()

# saving the plot into a file
fig.savefig (file_fig, dpi=100)
