#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/04/04 20:23:42 (UT+8) daisuke>
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
file_output = 'appy_s08_01_11.png'

# resolution in DPI
resolution_dpi = 150

# units
unit_K            = astropy.units.K
unit_sec          = astropy.units.s
unit_Hz           = astropy.units.Hz
unit_erg          = astropy.units.erg
unit_m            = astropy.units.m
unit_cm           = astropy.units.cm
unit_micron       = astropy.units.micron
unit_AA           = astropy.units.AA
unit_sr           = astropy.units.sr
unit_sp_intensity = unit_erg / unit_sec / unit_cm**2 / unit_AA / unit_sr

# temperature of blackbody
T = 3000.0 * unit_K

# printing temperature of blackbody
print (f'Temperature:')
print (f'  T = {T}')

# range of wavelength (from 10**-9 to 10**-3 metre)
wavelength_min = -9.0
wavelength_max = -3.0

# wavelength
wavelength_m      = numpy.logspace (wavelength_min, wavelength_max, \
                                    num=6001, dtype=numpy.longdouble) * unit_m
wavelength_aa     = wavelength_m.to (unit_AA)
wavelength_micron = wavelength_m.to (unit_micron)

# a function to calculate blackbody radiation for T=5000 K
bb_model = astropy.modeling.models.BlackBody (temperature=T, \
                                              scale=1.0 * unit_sp_intensity)

# calculation of blackbody radiation
bb_data = bb_model (wavelength_aa)

# printing blackbody radiation
print (f'Wavelength:')
print (f'{wavelength_micron}')
print (f'Blackbody radiation:')
print (f'{bb_data}')

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel (f'Wavelength [{wavelength_micron.unit}]')
ax.set_ylabel (f'Specific Intensity [{bb_data.unit}]')

# axes
ax.set_xscale ('log')
ax.set_yscale ('log')
ax.set_xlim (10**-1, 10**3)
ax.set_ylim (10**-3, 10**6)

# plotting data
ax.plot (wavelength_micron, bb_data, \
         linestyle='-', linewidth=3, color='red', \
         label=f'{T} blackbody')

# grid
ax.grid ()

# legend
ax.legend ()

# saving the plot into a file
fig.savefig (file_output, dpi=resolution_dpi)
