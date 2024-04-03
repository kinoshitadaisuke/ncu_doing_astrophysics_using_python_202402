#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/06 12:57:24 (CST) daisuke>
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
file_output = 'ai2023_s08_01_05.png'

# resolution in DPI
resolution_dpi = 225

# units
unit_K  = astropy.units.K
unit_Hz = astropy.units.Hz

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
bb_model = astropy.modeling.models.BlackBody (temperature=T)

# calculation of blackbody radiation
bb_data = bb_model (frequency_Hz)

# printing blackbody radiation
print (f'Frequency:')
print (f'{frequency_Hz}')
print (f'Blackbody radiation:')
print (f'{bb_data}')

# finding frequency corresponding to the peak of blackbody spectrum
frequency_peak    = bb_model.nu_max
frequency_peak_Hz = frequency_peak.to (unit_Hz)

# printing frequency corresponding to the peak of blackbody spectrum
print (f'peak of blackbody radiation of T={T}:')
print (f'  frequency_peak = {frequency_peak_Hz:g}')

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
ax.set_ylim (10**-9, 10**-3)

# make secondary X-axis
c   = astropy.constants.c
c_v = c.value
ax2 = ax.secondary_xaxis (location='top', \
                          functions=(lambda x: c_v/x * 10**6, \
                                     lambda x: c_v/x * 10**-6) )
ax2.set_xlabel ('Wavelength [$\mu$m]')

# plotting data
ax.plot (frequency_Hz, bb_data, \
         linestyle='-', linewidth=3, color='red', \
         zorder=0.2, \
         label=f'{T} blackbody')

# drawing a vertical line showing the peak of the spectrum
ax.axvline (x=frequency_peak_Hz.value, ymin=0, ymax=1, \
            linestyle='--', linewidth=3, color='blue', \
            zorder=0.1, \
            label='peak frequency')

# grid
ax.grid ()

# legend
ax.legend ()

# saving the plot into a file
fig.savefig (file_output, dpi=resolution_dpi)
