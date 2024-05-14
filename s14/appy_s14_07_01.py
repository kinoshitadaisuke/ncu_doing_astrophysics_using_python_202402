#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/12/15 09:38:05 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing gzip module
import gzip

# importing datetime module
import datetime

# importing numpy module
import numpy

# importing rebound module
import rebound

# importing ssl module
import ssl

# allow insecure downloading
ssl._create_default_https_context = ssl._create_unverified_context

# MPC's orbital elements file
file_mpcorb = 'MPCORB.DAT.gz'

# simulation file to be generated
file_sim = 'iss.bin'

majorbody = {
    'Sun':     '10',
    'Mercury': '1',
    'Venus':   '2',
    'Earth':   '3',
    'Mars':    '4',
    'Jupiter': '5',
    'Saturn':  '6',
    'Uranus':  '7',
    'Neptune': '8',
    'Pluto':   '9',
}

# number of asteroids to process
n_asteroids = 5000

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
            t_epoch = f'{year:04d}-{month:02d}-{day:02d} 00:00:00'
            # epoch in packed format
            epoch_ceres = epoch_packed
            # exit from the loop
            break

# construction of a simulation
sim = rebound.Simulation ()

# adding major bodies
for name in majorbody.keys ():
    sim.add (majorbody[name], date=t_epoch)

# dictionary to store orbital elements
dic_elements = {}

# counter
n_obj = 0

# printing status
print (f'Now, reading orbits of asteroids...')

# opening file
with gzip.open (file_mpcorb, 'rb') as fh:
    # flag
    data_line = 'NO'
    # reading file
    for line in fh:
        # decoding byte data
        line = line.decode ('utf-8').strip ()
        # if line is empty, then skip
        if (line == ''):
            continue
        # reading data
        if (data_line == 'YES'):
            # number (or provisional designation)
            number = line[0:7]
            # epoch
            epoch = line[20:25]
            # mean anomaly
            M = float (line[26:35])
            M_rad = numpy.deg2rad (M)
            # argument of perihelion
            peri = float (line[37:46])
            peri_rad = numpy.deg2rad (peri)
            # longitude of ascending node
            node = float (line[48:57])
            node_rad = numpy.deg2rad (node)
            # inclination
            i = float (line[59:68])
            i_rad = numpy.deg2rad (i)
            # eccentricity
            e = float (line[70:79])
            # semimajor axis
            a = float (line[92:103])

            # if epoch is no same as (1) Ceres, then skip
            if (epoch != epoch_ceres):
                continue
            
            # adding data to the dictionary
            dic_elements[number] = {}
            dic_elements[number]['a']    = a
            dic_elements[number]['e']    = e
            dic_elements[number]['i']    = i_rad
            dic_elements[number]['peri'] = peri_rad
            dic_elements[number]['node'] = node_rad
            dic_elements[number]['M']    = M_rad

            # incrementing counter
            n_obj += 1

            # when finish reading expected number of asteroid data, then break
            if (n_obj == n_asteroids):
                break
            
        # if the line starts with '----------'
        if (line[:10] == '----------'):
            # set the flag to 'YES'
            data_line = 'YES'
            continue

# printing status
print (f'Finished reading orbits of asteroids!')

# printing status
print (f'Now, adding asteroids to the simulation...')

# processing each asteroid orbit
for number in sorted (dic_elements.keys ()):
    # adding an asteroid
    sim.add (m=0.0, \
             a=dic_elements[number]['a'], \
             e=dic_elements[number]['e'], \
             inc=dic_elements[number]['i'], \
             omega=dic_elements[number]['peri'], \
             Omega=dic_elements[number]['node'], \
             M=dic_elements[number]['M'], \
             date=t_epoch)

# printing status
print (f'Finished adding asteroids to the simulation!')
    
# printing simulation object
print (sim)

# printing status
print (f'Now, saving the simulation into a file...')

# saving simulation to a file
sim.save_to_file (file_sim)

# printing status
print (f'Finished saving the simulation into a file!')
