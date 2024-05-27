#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/27 18:05:24 (UT+8) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# data file for colour indices
file_ubv = 'compil.ast.ubv-photometry/data/ubvmean.tab'

# data file for albedo measurements
file_albedo = 'compil.ast.albedos/data/albedos.tab'

# data file for taxonomic classification
file_class = 'ast_taxonomy/data/taxonomy10.tab'

# output file
file_output = 'appy_s15_06_10.png'

# making empty dictionaries for storing data
colour_ub     = {}
colour_ub_err = {}
colour_bv     = {}
colour_bv_err = {}
subclass      = {}
albedo        = {}
albedo_err    = {}

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
            # adding data to dictionary
            colour_ub[number]     = ub
            colour_ub_err[number] = ub_err
            colour_bv[number]     = bv
            colour_bv_err[number] = bv_err

# opening data file
with open (file_albedo, 'r') as fh:
    # reading data file line-by-line
    for line in fh:
        # extracting data
        number          = int (line[0:6])
        iras_albedo     = float (line[45:51])
        iras_albedo_err = float (line[52:57])
        quality_code    = int (line[58:59])
        # rejecting data if no measurement done by IRAS
        if (quality_code == 0):
            continue
        # printing data
        if (number > 0):
            albedo[number]     = iras_albedo
            albedo_err[number] = iras_albedo_err

# opening data file
with open (file_class, 'r') as fh:
    # reading data file line-by-line
    for line in fh:
        # extracting data
        number    = int (line[0:7])
        bus_class = line[80:83]
        # finding taxonomic class
        if (bus_class[0] == 'C'):
            taxonomy = 'C'
        elif (bus_class[0] == 'S'):
            taxonomy = 'S'
        elif (bus_class[0] == 'X'):
            taxonomy = 'X'
        elif (bus_class[0] == 'V'):
            taxonomy = 'V'
        elif (bus_class[0] == 'D'):
            taxonomy = 'D'
        else:
            taxonomy = 'others'
        # printing taxonomic classification
        if not ( (taxonomy == 'others') or (number == 0) ):
            # adding data to dictionary
            subclass[number] = taxonomy

# making empty lists for storing data
list_c_ub         = []
list_c_ub_err     = []
list_c_bv         = []
list_c_bv_err     = []
list_c_albedo     = []
list_c_albedo_err = []
list_s_ub         = []
list_s_ub_err     = []
list_s_bv         = []
list_s_bv_err     = []
list_s_albedo     = []
list_s_albedo_err = []
list_x_ub         = []
list_x_ub_err     = []
list_x_bv         = []
list_x_bv_err     = []
list_x_albedo     = []
list_x_albedo_err = []
list_v_ub         = []
list_v_ub_err     = []
list_v_bv         = []
list_v_bv_err     = []
list_v_albedo     = []
list_v_albedo_err = []
list_d_ub         = []
list_d_ub_err     = []
list_d_bv         = []
list_d_bv_err     = []
list_d_albedo     = []
list_d_albedo_err = []

# finding asteroids with known colour indices, albedo, and taxonomy
for number in subclass.keys ():
    # if we have all the (U-B), (B-V), albedo, and taxonomic classification
    if ( (number in colour_ub) and (number in colour_bv) \
         and (number in albedo) ):
        # printing data
        print (f'{number:6d} : U-B={colour_ub[number]:+6.3f},', \
               f'B-V={colour_bv[number]:+6.3f},', \
               f'albedo={albedo[number]:5.3f},', \
               f'subclass={subclass[number]}')
        # appending data to lists
        if (subclass[number] == 'C'):
            list_c_ub.append (colour_ub[number])
            list_c_ub_err.append (colour_ub_err[number])
            list_c_bv.append (colour_bv[number])
            list_c_bv_err.append (colour_bv_err[number])
            list_c_albedo.append (albedo[number])
            list_c_albedo_err.append (albedo[number])
        elif (subclass[number] == 'S'):
            list_s_ub.append (colour_ub[number])
            list_s_ub_err.append (colour_ub_err[number])
            list_s_bv.append (colour_bv[number])
            list_s_bv_err.append (colour_bv_err[number])
            list_s_albedo.append (albedo[number])
            list_s_albedo_err.append (albedo[number])
        elif (subclass[number] == 'X'):
            list_x_ub.append (colour_ub[number])
            list_x_ub_err.append (colour_ub_err[number])
            list_x_bv.append (colour_bv[number])
            list_x_bv_err.append (colour_bv_err[number])
            list_x_albedo.append (albedo[number])
            list_x_albedo_err.append (albedo[number])
        elif (subclass[number] == 'V'):
            list_v_ub.append (colour_ub[number])
            list_v_ub_err.append (colour_ub_err[number])
            list_v_bv.append (colour_bv[number])
            list_v_bv_err.append (colour_bv_err[number])
            list_v_albedo.append (albedo[number])
            list_v_albedo_err.append (albedo[number])
        elif (subclass[number] == 'D'):
            list_d_ub.append (colour_ub[number])
            list_d_ub_err.append (colour_ub_err[number])
            list_d_bv.append (colour_bv[number])
            list_d_bv_err.append (colour_bv_err[number])
            list_d_albedo.append (albedo[number])
            list_d_albedo_err.append (albedo[number])

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('B-V colour index')
ax.set_ylabel ('IRAS albedo')

# axes
ax.grid ()
ax.set_ylim (0.0, 1.0)

# plotting data
ax.errorbar (list_c_bv, list_c_albedo, \
             xerr=list_c_bv_err, yerr=list_c_albedo_err, \
             linestyle='None', marker='o', markersize=3, color='blue', \
             ecolor='black', capsize=1, \
             label='C-type and its variants')
ax.errorbar (list_s_bv, list_s_albedo, \
             xerr=list_s_bv_err, yerr=list_s_albedo_err, \
             linestyle='None', marker='o', markersize=3, color='red', \
             ecolor='black', capsize=1, \
             label='S-type and its variants')
ax.errorbar (list_x_bv, list_x_albedo, \
             xerr=list_x_bv_err, yerr=list_x_albedo_err, \
             linestyle='None', marker='o', markersize=3, color='green', \
             ecolor='black', capsize=1, \
             label='X-type and its variants')
ax.errorbar (list_v_bv, list_v_albedo, \
             xerr=list_v_bv_err, yerr=list_v_albedo_err, \
             linestyle='None', marker='o', markersize=3, color='purple', \
             ecolor='black', capsize=1, \
             label='V-type and its variants')
ax.errorbar (list_d_bv, list_d_albedo, \
             xerr=list_d_bv_err, yerr=list_d_albedo_err, \
             linestyle='None', marker='o', markersize=3, color='cyan', \
             ecolor='black', capsize=1, \
             label='D-type and its variants')

# legend
ax.legend ()

# saving plot into file
fig.savefig (file_output, dpi=150)
