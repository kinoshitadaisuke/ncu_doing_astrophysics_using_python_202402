#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/03 13:08:11 (UT+8) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.optimize

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# input data file
file_input = 'appy_s12_03_06.data'

# output figure file
file_output = 'appy_s12_03_08.png'

# range of data for fitting
x_min = 13.2038
x_max = 13.2047

# empty numpy array for storing data
data_all_per = numpy.array ([])
data_all_var = numpy.array ([])
data_fit_per = numpy.array ([])
data_fit_var = numpy.array ([])

# opening file for reading
with open (file_input, 'r') as fh:
    # reading file line-by-line
    for line in fh:
        # skipping line if the line starts with '#'
        if (line[0] == '#'):
            continue
        # removing line feed at the end of line
        line = line.strip ()
        # splitting data
        (per_day_str, per_hr_str, per_min_str, var_str) = line.split ()
        # conversion from string into float
        per_hr = float (per_hr_str)
        var    = float (var_str)
        # appending the data at the end of numpy arrays
        data_all_per = numpy.append (data_all_per, per_hr)
        data_all_var = numpy.append (data_all_var, var)
        if ( (per_hr >= x_min) and (per_hr <= x_max) ):
            data_fit_per = numpy.append (data_fit_per, per_hr)
            data_fit_var = numpy.append (data_fit_var, var)

# initial values of coefficients of fitted function
a    = 1000000.0
b    = 10.0
c    = 1.0
init = [a, b, c]

# function to be used for least-squares fitting
def func (x, a, b, c):
    y = a * (x - b)**2 + c
    return y

# least-squares fitting using scipy.optimize.curve_fit
popt, pcov = scipy.optimize.curve_fit (func, data_fit_per, data_fit_var, \
                                       p0=init, method='dogbox')

# fitted coefficients
print ("popt:")
print (popt)

# covariance matrix
print ("pcov:")
print (pcov)

# fitted a and b
a_fitted = popt[0]
b_fitted = popt[1]
c_fitted = popt[2]

# degree of freedom
dof = len (data_fit_per) - 3
print (f"dof = {dof}")

# residual
residual = data_fit_var - func (data_fit_per, a_fitted, b_fitted, c_fitted)
reduced_chi2 = (residual**2).sum () / dof
print (f"reduced chi^2 = {reduced_chi2}")

# errors of a and b
a_err = numpy.sqrt (pcov[0][0])
b_err = numpy.sqrt (pcov[1][1])
c_err = numpy.sqrt (pcov[2][2])
print (f"a = {a_fitted:13.6f} +/- {a_err:13.6f} ({a_err/a_fitted*100:6.2f} %)")
print (f"b = {b_fitted:13.6f} +/- {b_err:13.6f} ({b_err/b_fitted*100:6.2f} %)")
print (f"c = {c_fitted:13.6f} +/- {c_err:13.6f} ({c_err/c_fitted*100:6.2f} %)")

# fitted line
fitted_x = numpy.linspace (x_min, x_max, 10**3)
fitted_y = func (fitted_x, a_fitted, b_fitted, c_fitted)

# making fig and ax
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Period [hr]')
ax.set_ylabel ('Variance')

# range of plot
ax.set_xlim (x_min - 0.001, x_max + 0.001)
ax.set_ylim (c_fitted - 0.1, func (x_max, a_fitted, b_fitted, c_fitted) * 1.5 )

# plotting a figure
ax.plot (data_all_per, data_all_var, \
         linestyle='-', linewidth=5, color='blue', \
         label='result of PDM analysis')
ax.plot (fitted_x, fitted_y, \
         linestyle=':', linewidth=3, color='red', \
         label='fitted curve by curve_fit')
ax.legend ()

# saving the figure to a file
fig.savefig (file_output, dpi=150)
