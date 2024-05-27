#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/27 16:21:56 (UT+8) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# data file of SDSS MOC
file_sdss = 'gbo.sdss-moc.phot/data/sdssmocadr4.tab'

# output file
file_output = 'appy_s15_07_02.png'

# making empty dictionary to store data
colours = {}

# opening data file
with open (file_sdss, 'r') as fh:
    # reading data file line-by-line
    for line in fh:
        # extracting data
        number = int (line[244:251])
        mag_u  = float (line[162:168])
        err_u  = float (line[169:173])
        mag_g  = float (line[174:179])
        err_g  = float (line[180:184])
        mag_r  = float (line[185:190])
        err_r  = float (line[191:195])
        mag_i  = float (line[196:201])
        err_i  = float (line[202:206])
        mag_z  = float (line[207:212])
        err_z  = float (line[213:217])
        # rejecting if a quantity is missing
        if ( (number == 0) or (mag_u > 90.00) or (mag_g > 90.00) \
             or (mag_r > 90.00) or (mag_i > 90.00) or (mag_z > 90.00) ):
            continue
        # calculation of colour indices
        ug     = mag_u - mag_g
        ug_err = numpy.sqrt (err_u**2 + err_g**2)
        gr     = mag_g - mag_r
        gr_err = numpy.sqrt (err_g**2 + err_r**2)
        ri     = mag_r - mag_i
        ri_err = numpy.sqrt (err_r**2 + err_i**2)
        iz     = mag_i - mag_z
        iz_err = numpy.sqrt (err_i**2 + err_z**2)
        # adding data into dictionary
        colours[number] = {}
        colours[number]["ug"]     = ug
        colours[number]["ug_err"] = ug_err
        colours[number]["gr"]     = gr
        colours[number]["gr_err"] = gr_err
        colours[number]["ri"]     = ri
        colours[number]["ri_err"] = ri_err
        colours[number]["iz"]     = iz
        colours[number]["iz_err"] = iz_err


# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('g-r colour index')
ax.set_ylabel ('i-z colour index')

# axes
ax.grid ()

# plotting data
list_gr     = []
list_gr_err = []
list_iz     = []
list_iz_err = []
for i in sorted (colours.keys ()):
    list_gr.append (colours[i]["gr"])
    list_gr_err.append (colours[i]["gr_err"])
    list_iz.append (colours[i]["iz"])
    list_iz_err.append (colours[i]["iz_err"])
ax.errorbar (list_gr, list_iz, \
             xerr=list_gr_err, yerr=list_iz_err, \
             linestyle='None', marker='o', markersize=3, color='blue', \
             ecolor='black', capsize=1)

# saving plot into file
fig.savefig (file_output, dpi=150)
