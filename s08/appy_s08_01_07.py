#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/02 10:51:35 (CST) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.modeling.models
import astropy.units

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# output file name
file_output = 'ai2023_s08_01_07.png'

# resolution in DPI
resolution_dpi = 225

# units
unit_K              = astropy.units.K
unit_Hz             = astropy.units.Hz
unit_W              = astropy.units.W
unit_m              = astropy.units.m
unit_sr             = astropy.units.sr
unit_W_per_m2_Hz_sr = unit_W / unit_m**2 / unit_Hz / unit_sr

# temperature of blackbody
T = 8000.0 * unit_K

# printing temperature of blackbody
print (f'Temperature:')
print (f'  T = {T}')

# range of frequency (from 10**9 to 10**16)
frequency_min =  9.0
frequency_max = 16.0

# frequency in Hz
frequency_Hz = numpy.logspace (frequency_min, frequency_max, \
                               num=7001, dtype=numpy.longdouble) * unit_Hz

# a function to calculate blackbody radiation for T=8000 K
bb_model = astropy.modeling.models.BlackBody (temperature=T, \
                                              scale=1.0 * unit_W_per_m2_Hz_sr)

# calculation of blackbody radiation
bb_data = bb_model (frequency_Hz)

# printing blackbody radiation
print (f'Frequency:')
print (f'{frequency_Hz}')
print (f'Blackbody radiation:')
print (f'{bb_data}')

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel (f'Frequency [{frequency_Hz.unit}]')
ax.set_ylabel (f'Specific Intensity [{bb_data.unit}]')

# axes
ax.set_xscale ('log')
ax.set_yscale ('log')
ax.set_xlim (10**12, 10**16)
ax.set_ylim (10**-12, 10**-6)

# plotting data
ax.plot (frequency_Hz, bb_data, \
         linestyle='-', linewidth=3, color='red', \
         label=f'{T} blackbody')

# grid
ax.grid ()

# legend
ax.legend ()

# saving the plot into a file
fig.savefig (file_output, dpi=resolution_dpi)
