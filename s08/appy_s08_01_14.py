#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/03 08:55:03 (CST) daisuke>
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
file_output = 'ai2023_s08_01_14.png'

# resolution in DPI
resolution_dpi = 225

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

# finding wavelength corresponding to the peak of blackbody radiation
wavelength_peak        = bb_model.lambda_max
wavelength_peak_micron = wavelength_peak.to (unit_micron)

# printing wavelength corresponding to the peak of blackbody radiation
print (f'peak of blackbody radiation of T={T}:')
print (f'  wavelength_peak = {wavelength_peak_micron:g}')

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

# make secondary X-axis
c   = astropy.constants.c
c_v = c.value
ax2 = ax.secondary_xaxis (location='top', \
                          functions=(lambda x: c_v/x * 10**6, \
                                     lambda x: c_v/x * 10**-6) )
ax2.set_xlabel ('Frequency [Hz]')

# plotting data
ax.plot (wavelength_micron, bb_data, \
         linestyle='-', linewidth=3, color='red', \
         label=f'{T} blackbody')

# drawing a vertical line showing the peak of the spectrum
ax.axvline (x=wavelength_peak_micron.value, ymin=0, ymax=1, \
            linestyle='--', linewidth=3, color='blue', \
            zorder=0.1, \
            label='peak wavelength')

# grid
ax.grid ()

# legend
ax.legend ()

# saving the plot into a file
fig.savefig (file_output, dpi=resolution_dpi)
