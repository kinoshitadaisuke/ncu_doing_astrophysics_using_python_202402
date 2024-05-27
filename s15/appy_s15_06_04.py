#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/27 15:55:39 (UT+8) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# data file
file_ubv = 'compil.ast.ubv-photometry/data/ubvmean.tab'

# output file
file_output = 'appy_s15_06_04.png'

# making empty lists for storing data
list_ub     = []
list_ub_err = []
list_bv     = []
list_bv_err = []

# priting header
print (f'# asteroid number, U-B colour index, B-V colour index')

# opening file
with open (file_ubv, 'r') as fh:
    # reading file line-by-line
    for line in fh:
        # extracting data
        number        = int (line[0:5])
        designation   = line[6:16]
        ub            = float (line[17:22])
        ub_err        = float (line[24:29])
        ub_obsnumber  = int (line[31:33])
        ub_phase_min  = float (line[34:40])
        ub_phase_max  = float (line[41:47])
        ub_phase_mean = float (line[48:54])
        bv            = float (line[55:60])
        bv_err        = float (line[62:67])
        bv_obsnumber  = int (line[69:71])
        bv_phase_min  = float (line[72:78])
        bv_phase_max  = float (line[79:85])
        bv_phase_mean = float (line[86:92])

        # printing extracted colour indices of asteroids
        if not ( (number == 0) or (ub > 9.0) or (bv > 9.0) ):
            # appending data to lists
            list_ub.append (ub)
            list_ub_err.append (ub_err)
            list_bv.append (bv)
            list_bv_err.append (ub_err)
            # printing extracted data
            print (f'{number:5d} : U-B = {ub:+6.3f} +/- {ub_err:5.3f},', \
                   f'B-V = {bv:+6.3f} +/- {bv_err:5.3f}')

# making numpy arrays
array_ub     = numpy.array (list_ub)
array_ub_err = numpy.array (list_ub_err)
array_bv     = numpy.array (list_bv)
array_bv_err = numpy.array (list_bv_err)
            
# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('U-B colour index')
ax.set_ylabel ('B-V colour index')

# axes
ax.grid ()

# plotting data
ax.errorbar (array_ub, array_bv, xerr=array_ub_err, yerr=array_bv_err, \
             linestyle='None', marker='o', markersize=3, color='blue', \
             ecolor='black', capsize=1, \
             label='asteroids')

# legend
ax.legend ()

# saving plot into file
fig.savefig (file_output, dpi=150)
