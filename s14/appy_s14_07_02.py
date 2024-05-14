#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/12/15 09:48:16 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing gzip module
import gzip

# importing datetime module
import datetime

# importing numpy module
import numpy

# importing astropy module
import astropy.time
import astropy.units

# importing rebound module
import rebound

# date/time now
now = datetime.datetime.now ()

# units
u_day = astropy.units.day

# MPC's orbital elements file
file_mpcorb = 'MPCORB.DAT.gz'

# simulation file
file_sim = 'iss.bin'

# output file
file_output = 'iss.data'

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
n_output   = 1000

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

# opening file for writing
with open (file_output, 'w') as fh:
    # writing header
    fh.write (f"#\n")
    fh.write (f"# results of orbital integration using rebound\n")
    fh.write (f"#\n")
    fh.write (f"#   start of integration: {now}\n")
    fh.write (f"#\n")
    fh.write (f"#   list of objects:\n")
    for name in majorbody:
        fh.write (f"#     {name}\n")
    fh.write (f"#     and {n_minorbody} minor bodies\n")
    fh.write (f"#\n")
    fh.write (f"#   format of the data:\n")
    fh.write (f"#     JD, date/time, x,y,z,vx,vy,vz of obj1, ")
    fh.write (f"x,y,z,vx,vy,vz of obj2, ...\n")
    fh.write (f"#\n")

    # epoch
    t_epoch = astropy.time.Time (time_epoch, scale='utc', format='isot')

    # orbital integration
    for i in range (n_output):
        # target time
        time = t_interval * i
        # integration
        sim.integrate (time)
        # time after a step of integration
        t_current = t_epoch + 365.25 * sim.t / year * u_day
        jd_current = t_current.jd

        # writing data to file
        fh.write (f"{jd_current:.8f}|{t_current}")
        for j in range ( len (majorbody) + n_minorbody):
            fh.write (f"|{ps[j].x:+.15f},{ps[j].y:+.15f},{ps[j].z:+.15f},")
            fh.write (f"{ps[j].vx:+.15f},{ps[j].vy:+.15f},{ps[j].vz:+.15f}")
        fh.write (f"\n")

        # printing status
        if ( (i + 1) % 100 == 0 ):
            print (f"  status: {i + 1:8d} / {n_output:8d}")
