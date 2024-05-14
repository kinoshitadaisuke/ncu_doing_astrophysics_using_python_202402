#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/12/16 15:33:50 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing gzip module
import gzip

# importing pathlib module
import pathlib

# importing datetime module
import datetime

# importing numpy module
import numpy

# importing astropy module
import astropy.time
import astropy.units

# importing rebound module
import rebound

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# date/time now
now = datetime.datetime.now ()

# units
u_au   = astropy.units.au
u_hr   = astropy.units.hour
u_day  = astropy.units.day
u_year = astropy.units.year

# MPC's orbital elements file
file_mpcorb = 'MPCORB.DAT.gz'

# simulation file
file_sim = 'iss3d.bin'

# directory to store PNG files
dir_png = 'iss3d'

# making directory if it does not exist
path_png = pathlib.Path (dir_png)
if not (path_png.exists ()):
    path_png.mkdir (mode=0o755)

# output file name prefix
file_prefix = 'iss3d'

# output file extension
file_ext = 'png'
 
# opening file
with gzip.open (file_mpcorb, 'rb') as fh:
    # reading file
    for line in fh:
        # decoding byte data
        line = line.decode ('utf-8')
        if (line[0:5] == '00001'):
            # epoch (packed format)
            epoch_packed = line[20:25]
            # year
            if (epoch_packed[0] == 'I'):
                year0 = 1800
            elif (epoch_packed[0] == 'J'):
                year0 = 1900
            elif (epoch_packed[0] == 'K'):
                year0 = 2000
            year1 = int (epoch_packed[1:3])
            year = year0 + year1
            # month
            try:
                month = int (epoch_packed[3])
            except:
                if (epoch_packed[3] == 'A'):
                    month = 10
                elif (epoch_packed[3] == 'B'):
                    month = 11
                elif (epoch_packed[3] == 'C'):
                    month = 12
            # day
            try:
                day = int (epoch_packed[4])
            except:
                if (epoch_packed[4] == 'A'):
                    day = 10
                elif (epoch_packed[4] == 'B'):
                    day = 11
                elif (epoch_packed[4] == 'C'):
                    day = 12
                elif (epoch_packed[4] == 'D'):
                    day = 13
                elif (epoch_packed[4] == 'E'):
                    day = 14
                elif (epoch_packed[4] == 'F'):
                    day = 15
                elif (epoch_packed[4] == 'G'):
                    day = 16
                elif (epoch_packed[4] == 'H'):
                    day = 17
                elif (epoch_packed[4] == 'I'):
                    day = 18
                elif (epoch_packed[4] == 'J'):
                    day = 19
                elif (epoch_packed[4] == 'K'):
                    day = 20
                elif (epoch_packed[4] == 'L'):
                    day = 21
                elif (epoch_packed[4] == 'M'):
                    day = 22
                elif (epoch_packed[4] == 'N'):
                    day = 23
                elif (epoch_packed[4] == 'O'):
                    day = 24
                elif (epoch_packed[4] == 'P'):
                    day = 25
                elif (epoch_packed[4] == 'Q'):
                    day = 26
                elif (epoch_packed[4] == 'R'):
                    day = 27
                elif (epoch_packed[4] == 'S'):
                    day = 28
                elif (epoch_packed[4] == 'T'):
                    day = 29
                elif (epoch_packed[4] == 'U'):
                    day = 30
                elif (epoch_packed[4] == 'V'):
                    day = 31
            # epoch in YYYY-MM-DD hh:mm:ss format
            t_epoch = f'{year:04d}-{month:02d}-{day:02d}T00:00:00'
            # epoch in packed format
            epoch_ceres = epoch_packed
            # exit from the loop
            break

# parameters
year       = 2.0 * numpy.pi
time_epoch = t_epoch
t_interval = 0.1 # 0.1 ==> 365.25/(2.0*pi) * 0.1 = 5.81 days
n_output   = 3600

# major bodies
majorbody = [
    'Sun',
    'Mercury',
    'Venus',
    'Earth',
    'Mars',
    'Jupiter',
    'Saturn',
    'Uranus',
    'Neptune',
    'Pluto',
]

# number of minor bodies
n_minorbody = 5000

# reading simulation from file
sim = rebound.Simulation (file_sim)
sim.integrator = 'mercurius'
sim.dt = +0.01
sim.move_to_com ()

# particles
ps = sim.particles

# epoch
t_epoch = astropy.time.Time (time_epoch, scale='utc', format='isot')

# making a fig object using object-oriented interface
fig = matplotlib.figure.Figure (figsize=[15.36, 8.64])
fig.subplots_adjust (left=0.0, right=1.0, bottom=0.0, top=1.0, \
                     wspace=0.0, hspace=0.0)

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_axes ( (0, 0, 1, 1), projection='3d')

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
el0 = 90.0

# initial value of 'azim' angle
az0 = -90.0

# initial value of 'zoom'
zoom0 = 1.0

# orbital integration
for i in range (n_output):
    # target time
    time = t_interval * i
    # integration
    sim.integrate (time)
    # time after a step of integration
    t_current  = t_epoch + sim.t / year * u_year

    # clearing previous axes
    ax.cla ()
    
    # printing status
    print (f'Now, making a plot for t={t_current}...')

    # settings for plot
    ax.set_xlim3d (-7.5, +7.5)
    ax.set_ylim3d (-7.5, +7.5)
    ax.set_zlim3d (-2.0, +2.0)
    ax.set_box_aspect ( (15.0, 15.0, 4.0), zoom=1.0 )

    # projection
    ax.set_proj_type ('persp')

    # using black background colour
    fig.set_facecolor ('white')
    ax.set_facecolor ('black')
    ax.grid (False)
    ax.xaxis.set_pane_color ((0.0, 0.0, 0.0, 0.0))
    ax.yaxis.set_pane_color ((0.0, 0.0, 0.0, 0.0))
    ax.zaxis.set_pane_color ((0.0, 0.0, 0.0, 0.0))

    # camera viewing angle
    if (i < 300):
        el   = el0
        az   = az0
        zoom = zoom0
    elif ( (i >= 300) and (i < 1200) ):
        el   = el0 - (i - 300) * 0.1
        az   = az0
        zoom = zoom0
    elif ( (i >= 1200) and (i < 1500) ):
        el   = 0.0
        az   = az0
        zoom = zoom0
    elif ( (i >= 1500) and (i < 1800) ):
        el   = (i - 1500) * 0.1
        az   = az0
        zoom = zoom0
    elif ( (i >= 1800) and (i < 2100) ):
        el   = 30.0
        az   = az0
        zoom = zoom0
    elif ( (i >= 2100) and (i < 2400) ):
        el   = 30.0
        az   = az0
        zoom = zoom0 + (i - 2100) * 0.005
    elif ( (i >= 2400) and (i < 2700) ):
        el   = 30.0
        az   = az0
        zoom = zoom0 + 1.5 - (i - 2400) * 0.005
    elif ( (i >= 2700) and (i < 3300) ):
        el   = 30.0 + (i - 2700) * 0.1
        az   = az0
        zoom = zoom0
    else:
        el   = el0
        az   = az0
        zoom = zoom0

    # plotting the Sun
    sun = make_sphere (ps[0].x, ps[0].y, ps[0].z, 0.25, 'orange')

    # plotting Mercury
    mercury = make_sphere (ps[1].x, ps[1].y, ps[1].z, 0.05, 'cyan')

    # plotting Venus
    venus = make_sphere (ps[2].x, ps[2].y, ps[2].z, 0.15, 'gold')

    # plotting Earth
    earth = make_sphere (ps[3].x, ps[3].y, ps[3].z, 0.15, 'blue')

    # plotting Mars
    mars = make_sphere (ps[4].x, ps[4].y, ps[4].z, 0.15, 'red')

    # plotting Jupiter
    jupiter = make_sphere (ps[5].x, ps[5].y, ps[5].z, 0.20, 'bisque')

    # plotting Saturn
    saturn = make_sphere (ps[6].x, ps[6].y, ps[6].z, 0.18, 'wheat')

    # plotting Uranus
    uranus = make_sphere (ps[7].x, ps[7].y, ps[7].z, 0.16, 'aquamarine')

    # plotting Neptun
    neptune = make_sphere (ps[8].x, ps[8].y, ps[8].z, 0.17, 'lightskyblue')

    # plotting Pluto
    pluto = make_sphere (ps[9].x, ps[9].y, ps[9].z, 0.05, 'cadetblue')

    # plotting asteroids
    for j in range (n_minorbody):
        ax.scatter (ps[j+10].x, ps[j+10].y, ps[j+10].z, \
                    s=1.0, color='saddlebrown', alpha=0.5)

    # title
    title = ax.text2D (0.5, 0.75, f'Inner Solar System', \
                       color='white', \
                       horizontalalignment='center', \
                       transform=ax.transAxes)
    
    # plotting the time
    time = ax.text2D (0.20, 0.23, f'Date/Time: {t_current.isot} (UTC)', \
                      color='white', \
                      horizontalalignment='center', \
                      transform=ax.transAxes)

    # plotting the author name
    author = ax.text2D (0.85, 0.23, f'animation generated by Daisuke', \
                        color='white', \
                        horizontalalignment='center', \
                        transform=ax.transAxes)

    # viewing angles of camera
    ax.view_init (elev=el, azim=az)
    ax.set_box_aspect ( (15.0, 15.0, 4.0), zoom=zoom)

    # image file
    file_image = f'{dir_png}/{file_prefix}_{i:06d}.{file_ext}'
    fig.savefig (file_image, dpi=225)

    # printing status
    if ( (i + 1) % 100 == 0 ):
        print (f"  status: {i + 1:8d} / {n_output:8d}")
