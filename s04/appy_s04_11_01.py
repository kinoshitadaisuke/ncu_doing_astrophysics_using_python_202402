#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/01 16:58:18 (CST) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

# importing sys module
import sys

# importing numpy module
import numpy

# importing astropy module
import astropy
import astropy.coordinates
import astropy.time
import astropy.units

# importing astroquery module
import astroquery.jplhorizons

# importing matplotlib module
import matplotlib.animation
import matplotlib.backends.backend_agg
import matplotlib.figure

# constructing a parser object
descr  = f'3D structure of inner solar system #2'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-t', '--time', default='2000-01-01T12:00:00', \
                     help='start date/time in YYYY-MM-DDThh:mm:ss format')
parser.add_argument ('-a', '--asteroid', type=int, default=1000, \
                     help='number of asteroids to plot (default: 1000)')
parser.add_argument ('-n', '--nframe', type=int, default=600, \
                     help='number of frames (default: 600)')
parser.add_argument ('-s', '--step', type=int, default=6, \
                     help='step size of animation in hr (default: 6)')
parser.add_argument ('-d', '--dir', default='solsys_3d2', \
                     help='directory to put output files (default: solsys_3d2)')

# parsing arguments
args = parser.parse_args ()

# parameters
datetime_start = args.time
n_asteroids    = args.asteroid
nframe         = args.nframe
step_hr        = args.step
dir_image      = args.dir

# making a pathlib object for image directory
path_image = pathlib.Path (dir_image)

# check of existence of image directory
if not (path_image.exists ()):
    # making a directory
    path_image.mkdir ()
else:
    # if dir_image is not a directory
    if not (path_image.is_dir ()):
        # printing a message
        print (f'"{dir_image}" exists, but it is not a directory!')
        # stop the script
        sys.exit (0)

# units
u_au = astropy.units.au
u_hr = astropy.units.hour

# step size in hr
step_str = f'{step_hr:d}h'
step     = step_hr * u_hr

# an empty list for storing asteroids positions
list_asteroids = []

# time to start the simulation in astropy.time object
t_start = astropy.time.Time (datetime_start, format='isot', scale='utc')

# time to stop the simulation in astropy.time object
t_stop  = t_start + step * nframe

# an empty list for storing major planets positions
list_major = []

# major body names (Sun, Mercury, Venus, Earth, Mars, Jupiter)
list_names = ['10', '199', '299', '399', '499', '599']

# getting positions of the Sun, Mercury, Venus, Earth, Mars, and Jupiter
# from JPL/Horizons
print (f'Now, getting positions of the Sun and planets...')
for i in list_names:
    print (i)
    query = astroquery.jplhorizons.Horizons (id_type=None, id=f'{i}', \
                                             location='@0', \
                                             epochs={'start': t_start.iso, \
                                                     'stop': t_stop.iso, \
                                                     'step': step_str})
    vec = query.vectors ()
    print (vec)
    x = vec['x']
    y = vec['y']
    z = vec['z']
    list_major.append ( [x, y, z] )
print (f'Finished getting positions of the Sun and planets!')

# getting asteroids positions from JPL/Horizons
print (f'Now, getting asteroids positions...')
for i in range (1, n_asteroids + 1):
    if (i % 10 == 0):
        print (f'  now, getting positions of asteroid ({i})...')
    ast_query = astroquery.jplhorizons.Horizons (id_type='smallbody', \
                                                 id=f'{i}', \
                                                 location='@0', \
                                                 epochs={'start': t_start.iso, \
                                                         'stop': t_stop.iso, \
                                                         'step': step_str})
    ast_vec = ast_query.vectors ()
    x = ast_vec['x']
    y = ast_vec['y']
    z = ast_vec['z']
    list_asteroids.append ( [x, y, z] )
print (f'Finished getting asteroids positions...')

# making a fig object using object-oriented interface
fig = matplotlib.figure.Figure ()
fig.subplots_adjust (left=0.0, right=1.0, bottom=0.0, top=1.0)

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111, projection='3d')

# an empty list of frames for animation
list_frame = []

# definition of a function for making a sphere
def make_sphere (x_c, y_c, z_c, radius, colour):
    u = numpy.linspace (0, 2 * numpy.pi, 1000)
    v = numpy.linspace (0, numpy.pi, 1000)
    x = radius * numpy.outer (numpy.cos(u), numpy.sin(v)) + x_c
    y = radius * numpy.outer (numpy.sin(u), numpy.sin(v)) + y_c
    z = radius * numpy.outer (numpy.ones(numpy.size(u)), numpy.cos(v)) + z_c
    # plotting the surface
    sphere = ax.plot_surface (x, y, z, color=colour, antialiased=False, \
                               shade=True, rcount=100, ccount=100)
    return (sphere)

# initial value of 'elev' angle
el = 30.0

# initial value of 'azim' angle
az = 0.0

for i in range (nframe):
    # clearing previous axes
    ax.cla ()
    
    # time t
    t = t_start + i * step

    # printing positions of the Sun, planets, and asteroids
    if (i % 10 == 0):
        print (f'Now, making a plot for {t}...')

    # settings for plot
    ax.set_xlim (-6.0, +6.0)
    ax.set_ylim (-6.0, +6.0)
    ax.set_zlim (-2.0, +2.0)
    ax.set_box_aspect ( (6.0, 6.0, 2.0) )

    # viewing angles of camera
    ax.view_init (elev=el, azim=az)

    # using black background colour
    fig.set_facecolor ('black')
    ax.set_facecolor ('black')
    ax.grid (False)
    ax.xaxis.set_pane_color ((0.0, 0.0, 0.0, 0.0))
    ax.yaxis.set_pane_color ((0.0, 0.0, 0.0, 0.0))
    ax.zaxis.set_pane_color ((0.0, 0.0, 0.0, 0.0))

    # plotting the Sun
    sun = make_sphere (list_major[0][0][i], \
                       list_major[0][1][i], \
                       list_major[0][2][i], \
                       0.25, 'yellow')

    # plotting Mercury
    mercury = make_sphere (list_major[1][0][i], \
                           list_major[1][1][i], \
                           list_major[1][2][i], \
                           0.05, 'cyan')
    
    # plotting Venus
    venus = make_sphere (list_major[2][0][i], \
                         list_major[2][1][i], \
                         list_major[2][2][i], \
                         0.15, 'gold')

    # plotting Earth
    earth = make_sphere (list_major[3][0][i], \
                         list_major[3][1][i], \
                         list_major[3][2][i], \
                         0.15, 'blue')

    # plotting Mars
    mars = make_sphere (list_major[4][0][i], \
                        list_major[4][1][i], \
                        list_major[4][2][i], \
                        0.15, 'red')

    # plotting Jupiter
    jupiter = make_sphere (list_major[5][0][i], \
                           list_major[5][1][i], \
                           list_major[5][2][i], \
                           0.15, 'bisque')

    # plotting asteroids
    for j in range (0, n_asteroids):
        asteroid = ax.scatter (list_asteroids[j][0][i], \
                               list_asteroids[j][1][i], \
                               list_asteroids[j][2][i], \
                               s=0.1, \
                               color='saddlebrown')
    
    # title
    title = ax.text2D (0.5, 0.95, f'Inner Solar System', \
                       color='white', \
                       horizontalalignment='center', \
                       transform=ax.transAxes)

    # plotting the time
    time = ax.text2D (0.5, 0.05, f'Date/Time: {t} (UTC)', \
                      color='white', \
                      horizontalalignment='center', \
                      transform=ax.transAxes)

    # image file
    file_image = f'{dir_image}/{i:06d}.png'
    fig.savefig (file_image, dpi=255)
