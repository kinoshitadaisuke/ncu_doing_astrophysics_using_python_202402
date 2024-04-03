#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/05 15:45:18 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.constants
import scipy.optimize

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# input file name
file_input = 'cmb_cobe.data'

# output file name
file_output = 'ai2023_s08_04_03.png'

# resolution in DPI
resolution_dpi = 225

#
# constants
#

# speed of light
c = scipy.constants.c
# Planck constant
h = scipy.constants.h
# Boltzmann constant
k = scipy.constants.k

# numpy arrays for storing data
data_freq_kayser = numpy.array ([])
data_intensity   = numpy.array ([])
data_residual    = numpy.array ([])
data_uncertainty = numpy.array ([])
data_galspec     = numpy.array ([])

# opening file
with open (file_input, 'r') as fh:
    # reading data file
    for line in fh:
        # skip if the line starts with '#'.
        if (line[0] == '#'):
            continue
        # splitting the data
        (freq_kayser_str, intensity_str, residual_str, uncertainty_str,
         galspec_str) = line.split ()
        # conversion from string into float
        freq_kayser = float (freq_kayser_str)
        intensity   = float (intensity_str)
        residual    = float (residual_str)
        uncertainty = float (uncertainty_str)
        galspec     = float (galspec_str)
        # appending data to numpy arrays
        data_freq_kayser = numpy.append (data_freq_kayser, freq_kayser)
        data_intensity   = numpy.append (data_intensity, intensity)
        data_residual    = numpy.append (data_residual, residual)
        data_uncertainty = numpy.append (data_uncertainty, uncertainty)
        data_galspec     = numpy.append (data_galspec, galspec)

# printing extracted data
print (f'Frequency in Kayser:')
print (f'{data_freq_kayser}')
print (f'Intensity in MJy/sr:')
print (f'{data_intensity}')

# initial values of coefficients of fitted function
T    = 10.0
a    = 10**10
init = [T, a]

# blackbody function
def func (x, T, a):
    x_mm = 10.0 / x
    x_m = x_mm * 10**-3
    f = c / x_m
    y = a * 2.0 * h * f**3 / c**2 / (numpy.exp (h * f / (k * T) ) - 1.0 )
    return (y)

# least-squares method
popt, pcov = scipy.optimize.curve_fit (func, data_freq_kayser, \
                                       data_intensity, \
                                       p0=init, sigma=data_uncertainty)

print ("popt:")
print (popt)

print ("pcov:")
print (pcov)

# dof
dof = len (data_freq_kayser) - len (init)
print ("dof =", dof)

# residual
residual = data_intensity - func (data_freq_kayser, popt[0], popt[1])
reduced_chi2 = (residual**2).sum () / dof
print ("reduced chi^2 =", reduced_chi2)

# errors of T and a
T_err = numpy.sqrt (pcov[0][0])
a_err = numpy.sqrt (pcov[1][1])
print (f"T = {popt[0]:g} +/- {T_err:g} ({T_err / popt[0] * 100.0} %)")
print (f"a = {popt[1]:g} +/- {a_err:g} ({a_err / popt[1] * 100.0} %)")

# fitted curve
fitted_x = numpy.linspace (0.1, 25.0, 10000)
fitted_y = func (fitted_x, popt[0], popt[1])

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Wavenumber [cm$^{-1}$]')
ax.set_ylabel ('Intensity [MJy sr$^{-1}$]')

# axes
ax.set_xscale ('log')
ax.set_yscale ('log')
ax.set_xlim (1.0, 50.0)
ax.set_ylim (1.0, 1000.0)

# plotting data
ax.errorbar (data_freq_kayser, data_intensity, yerr=data_uncertainty, \
             linestyle='None', marker='o', markersize=5, color='r', \
             ecolor='black', elinewidth=3, capsize=3, \
             zorder=0.2, \
             label='CMB measurement by COBE/FIRAS')
ax.plot (fitted_x, fitted_y, \
         linestyle='-', linewidth=3, color='blue', \
         zorder=0.1, \
         label='Blackbody fitting')

# legend and grid
ax.legend ()
ax.grid ()

# saving the plot into a file
fig.savefig (file_output, dpi=resolution_dpi)
