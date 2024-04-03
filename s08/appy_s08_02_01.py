#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/05 09:26:46 (CST) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# data file name
file_input = 'solar_spec.data'

# figure file name
file_output = 'ai2023_s08_02_01.png'

# resolution in DPI
resolution_dpi = 225

# initialisation of numpy arrays for storing data
wl         = numpy.array ([])
irradiance = numpy.array ([])

# opening file
with open (file_input, 'r') as fh:
    # initialisation of the parameter "i" for counting lines
    i = 0
    # reading data line-by-line
    for line in fh:
        # incrementing line number
        i += 1
        # skipping first 9 lines
        if (i < 10):
            continue
        # splitting data into wavelength and irradiance
        line = line.strip ()
        (wl_str, irradiance_str) = line.split ()
        # converting string into float
        wl_float         = float (wl_str)
        irradiance_float = float (irradiance_str)
        # appending data to numpy arrays
        wl         = numpy.append (wl, wl_float)
        irradiance = numpy.append (irradiance, irradiance_float)

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Wavelength [nm]')
ax.set_ylabel ('Irradiance [W m$^{-2}$ nm$^{-1}$]')

# axes
ax.set_xlim (100, 10000)
ax.set_ylim (0.0, 2.5)
ax.set_xscale ('log')

# plotting data
ax.plot (wl, irradiance, linestyle='-', linewidth=2, color='r', label='Sun')
ax.legend ()

# saving the plot into a file
fig.savefig (file_output, dpi=resolution_dpi)
