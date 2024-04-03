#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/02 12:31:19 (CST) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.constants
import astropy.modeling.models
import astropy.units

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# output file name
file_output = 'ai2023_s08_01_09.png'

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
T = [1000.0, 2000.0, 4000.0, 8000.0, 16000.0, 32000.0, 64000.0] * unit_K

# printing temperature of blackbody
print (f'Temperature:')
print (f'  T = {T}')

# range of frequency (from 10**9 to 10**16)
frequency_min =  9.0
frequency_max = 17.0

# frequency in Hz
frequency_Hz = numpy.logspace (frequency_min, frequency_max, \
                               num=7001, dtype=numpy.longdouble) * unit_Hz

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# axes
ax.set_xscale ('log')
ax.set_yscale ('log')
ax.set_xlim (10**11, 10**17)
ax.set_ylim (10**-12, 10**-4)

# make secondary X-axis
c   = astropy.constants.c
c_v = c.value
ax2 = ax.secondary_xaxis (location='top', \
                          functions=(lambda x: c_v/x * 10**6, \
                                     lambda x: c_v/x * 10**-6) )
ax2.set_xlabel ('Wavelength [$\mu$m]')

for i in range (len (T)):
    # blackbody radiation model
    bb_model = astropy.modeling.models.BlackBody (temperature=T[i], \
                                                  scale=1.0*unit_W_per_m2_Hz_sr)
    # blackbody radiation
    bb_data  = bb_model (frequency_Hz)

    # label
    text_label = f'T = {T[i]}'
    
    # plotting data
    ax.plot (frequency_Hz, bb_data, \
             linestyle='-', linewidth=3, \
             label=text_label)

# labels
ax.set_xlabel (f'Frequency [{frequency_Hz.unit}]')
ax.set_ylabel (f'Specific Intensity [{bb_data.unit}]')

# grid
ax.grid ()
    
# legend
ax.legend ()

# saving the plot into a file
fig.savefig (file_output, dpi=resolution_dpi)
