#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/12/14 20:28:17 (Taiwan_Standard_Time_UT+8) daisuke>
#

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

# simulation file to be generated
file_sim = 'comets.bin'

# major bodies
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

# minor bodies
minorbody = {
    '1P/Halley':                 'DES=1P; CAP',
    '2P/Encke':                  'DES=2P; CAP',
    '8P/Tuttle':                 'DES=8P; CAP',
    '9P/Tempel':                 'DES=9P; CAP',
    '17P/Holmes':                'DES=17P; CAP',
    '21P/Giacobini-Zinner':      'DES=21P; CAP',
    '22P/Kopff':                 'DES=22P; CAP',
    '23P/Brorsen-Metcalf':       'DES=23P; CAP',
    '29P/Schwassmann-Wachmann':  'DES=29P; CAP',
    '55P/Tempel-Tuttle':         'DES=55P; CAP',
    '63P/Wild':                  'DES=63P; CAP',
    '67P/Churyumov-Gerasimenko': 'DES=67P; CAP',
    '109P/Swift-Tuttle':         'DES=109P; CAP',
    '122P/de Vico':              'DES=122P; CAP',
    '153P/Ikeya-Zhang':          'DES=153P; CAP',
}

# epoch of orbital elements
t_epoch = '2000-01-01 12:00:00'

# construction of a simulation
sim = rebound.Simulation ()

# adding major bodies
for name in majorbody.keys ():
    sim.add (majorbody[name], date=t_epoch, hash=name)

# adding minor bodies
for name in minorbody.keys ():
    sim.add (minorbody[name], date=t_epoch, hash=name)

# printing simulation
print (sim)
    
# saving simulation to a file
sim.save_to_file (file_sim)
