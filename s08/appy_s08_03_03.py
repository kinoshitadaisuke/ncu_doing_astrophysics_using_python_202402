#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/05 14:44:03 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.optimize

# importing astropy module
import astropy.constants
import astropy.units

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# input file name
file_input = 'hd61005_spec.data'

# output file name
file_output = 'ai2023_s08_03_03.png'

# resolution in DPI
resolution_dpi = 225

# constants
c = astropy.constants.c
h = astropy.constants.h
k = astropy.constants.k_B

# units
u_micron = astropy.units.micron
u_Jy     = astropy.units.Jy
u_K      = astropy.units.K

# making empty numpy arrays
data_wl       = numpy.array ([])
data_flux     = numpy.array ([])
data_flux_err = numpy.array ([])
phot_wl       = numpy.array ([])
phot_flux     = numpy.array ([])
phot_flux_err = numpy.array ([])

# opening data file
with open (file_input, 'r') as fh:
    # reading data line-by-line
    for line in fh:
        # if the word '+or-' is found, then we process the line
        if ('+or-' in line):
            # splitting data
            data = line.split ('+or-')
            # wavelength and flux
            (wl_str, flux_str) = data[0].split ()
            # error of flux
            flux_error_str = data[1].split ()[0]
            # conversion from string into float
            wl         = float (wl_str)
            flux       = float (flux_str)
            flux_error = float (flux_error_str)
            # appending data into numpy arrays
            data_wl       = numpy.append (data_wl, wl)
            data_flux     = numpy.append (data_flux, flux)
            data_flux_err = numpy.append (data_flux_err, flux_error)
            # appending data into numpy arrays for photosphere data
            if (wl < 5.0):
                phot_wl       = numpy.append (phot_wl, wl)
                phot_flux     = numpy.append (phot_flux, flux)
                phot_flux_err = numpy.append (phot_flux_err, flux_error)

# adding units
data_wl       = data_wl * u_micron
data_flux     = data_flux * u_Jy
data_flux_err = data_flux_err * u_Jy
phot_wl       = phot_wl * u_micron
phot_flux     = phot_flux * u_Jy
phot_flux_err = phot_flux_err * u_Jy

# printing data
print (f'SED of HD 61005')
print (f'  wavelength:')
print (f'    {data_wl}')
print (f'  flux:')
print (f'    {data_flux}')
print (f'  error of flux:')
print (f'    {data_flux_err}')

# priting data for SED fitting at visible-NIR
print (f'data for SED fitting at visible-NIR:')
print (f'  {phot_wl}')
print (f'  {phot_flux}')

# initial values of coefficients for fitting by least-squares method
T_phot    = 10000.0
a_phot    = 10**8
init_phot = [T_phot, a_phot]

# function
def bb_nu (x, T, a):
    # wavelength in metre
    x_m = x * 10**-6
    # frequency in Hz
    f = c.value / x_m
    # Planck's radiation law
    y = a * 2.0 * h.value * f**3 / c.value**2 \
        / (numpy.exp (h.value * f / (k.value * T) ) - 1.0 )
    # returning blackbody radiation
    return (y)

# weighted least-squares method
popt_phot, pcov_phot = scipy.optimize.curve_fit (bb_nu, \
                                                 phot_wl.value, \
                                                 phot_flux.value, \
                                                 p0=init_phot, \
                                                 sigma=phot_flux_err.value)

# result of fitting
print (f"T_phot = {popt_phot[0]} K")

# generating fitted curve
wl_min = -1.0
wl_max = 3.0
n      = 4001
phot_x = numpy.logspace (wl_min, wl_max, n)
phot_y = bb_nu (phot_x, popt_phot[0], popt_phot[1])


# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Wavelength [$\mu$m]')
ax.set_ylabel ('Flux [Jy]')

# axes
ax.set_xscale ('log')
ax.set_yscale ('log')
ax.set_xlim (10**-1, 10**3)
ax.set_ylim (10**-2, 10**1)

# plotting data
ax.errorbar (data_wl, data_flux, yerr=data_flux_err, \
             linestyle='None', marker='o', markersize=5, color='red', \
             ecolor='black', elinewidth=2, capsize=5, \
             zorder=0.4, \
             label='HD61005')
ax.plot (phot_x, phot_y, \
         linestyle='--', linewidth=3, color='blue', \
         zorder=0.2, \
         label='Blackbody fitting at visible-NIR')
ax.legend ()

# saving the plot into a file
fig.savefig (file_output, dpi=resolution_dpi)
