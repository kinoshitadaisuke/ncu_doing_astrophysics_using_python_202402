#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/19 16:32:05 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing scipy module
import scipy.optimize
import scipy.constants

# importing astropy module
import astropy.io.ascii
import astropy.units
import astropy.constants

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# command-line argument analysis
desc   = 'making Hubble diagram using NED-D data'
parser = argparse.ArgumentParser (description=desc)
parser.add_argument ('-i', '--input', help='input data file name')
parser.add_argument ('-o', '--output', help='output figure file name')
parser.add_argument ('-r', '--resolution', type=float, default=225.0, \
                     help='resolution in DPI (default: 225)')

# command-line arguments analysis
args = parser.parse_args ()

# input parameters
file_data      = args.input
file_fig       = args.output
resolution_dpi = args.resolution

# speed of light
c = astropy.constants.c

# units
unit_m_per_s  = astropy.units.m / astropy.units.s
unit_km_per_s = astropy.units.km / astropy.units.s
unit_Mpc      = astropy.units.Mpc

# reading CSV data
rawdata = astropy.io.ascii.read (file_data, format='csv')

# dictionary to store data
data = {}

# examining the data
for i in range ( len (rawdata) ):
    # extracting data
    # name of galaxy
    name = rawdata[i]['Galaxy ID']
    # distance modulus
    distmod = rawdata[i]['m-M']
    # error of distance modulus
    distmod_err = rawdata[i]['err']
    # distance in Mpc
    dist_Mpc = rawdata[i]['D (Mpc)'] * unit_Mpc
    # redshift
    z = rawdata[i]['_1']
    # velocity
    v = ( (z + 1.0)**2 - 1.0 ) / ( (z + 1.0)**2 + 1.0 ) * c

    # appending data to the dictionary
    # skip if redshift is missing.
    # skip if error of distance modulus is large.
    # skip if distance is larger than 500 Mpc
    # skip if velocity is larger than 50000 km/s
    if ( (z > 0.0) and (distmod_err < 0.05) and (dist_Mpc.value < 500.0) \
         and (v.value < 5*10**7) ):
        # if the data is not in the dictionary, add data
        if not name in data:
            data[name] = {}
            data[name]['distmod'] = distmod
            data[name]['distmod_err'] = distmod_err
            data[name]['dist_Mpc'] = dist_Mpc
            data[name]['z'] = z
            data[name]['v'] = v

# making numpy arrays for plotting data
data_d = numpy.array ([])
data_v = numpy.array ([])
for name in sorted (data, key=lambda x: data[x]['dist_Mpc']):
    data_d = numpy.append (data_d, data[name]['dist_Mpc'].value)
    data_v = numpy.append (data_v, data[name]['v'].to (unit_km_per_s).value)

# initial values of coefficient
H0 = 100.0
init = [H0]

# function
def func (x, H0):
    y = H0 * x
    return (y)

# least-squares method
popt, pcov = scipy.optimize.curve_fit (func, data_d, data_v, p0=init)

# result of fitting
H0_bestfit = popt[0]
print ("popt:")
print (popt)
print ("pcov:")
print (pcov)

# degree of freedom
dof = len (data_d) - len (init)
print (f"dof = {dof}")

# residual
residual = data_v - func (data_d, popt[0])
reduced_chi2 = (residual**2).sum () / dof
print (f"reduced chi^2 = {reduced_chi2}")

# error of H0
H0_err = numpy.sqrt (pcov[0][0])
print (f"H0 = {H0_bestfit} +/- {H0_err} ({H0_err / H0_bestfit * 100.0} %)")

# fitted curve
fitted_x = numpy.linspace (0.0, 500.0, 1000)
fitted_y = func (fitted_x, H0_bestfit)

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# axes
ax.set_xlabel ('Distance [Mpc]')
ax.set_ylabel ('Velocity [km/s]')
ax.grid ()

# making a Hubble diagram
ax.plot (data_d, data_v, \
         linestyle='None', marker='o', markersize=2, color='blue', \
         zorder=0.2, \
         label='galaxies in NED-1D')
label_fitting = f"best-fit line (H0={H0_bestfit:4.1f} km/sec/Mpc)"
ax.plot (fitted_x, fitted_y, \
         linestyle='--', linewidth=3, color='red', \
         zorder=0.1, \
         label=label_fitting)
ax.legend ()

# saving the plot into a file
fig.savefig (file_fig, dpi=resolution_dpi)
