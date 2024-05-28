#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/28 09:50:43 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# construction of parser object for argparse
descr  = f'plotting result of DBSCAN using parallax, rv, pmra, and pmdec'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-i', '--input', help='input file name')
parser.add_argument ('-o', '--output', help='output file name')
parser.add_argument ('-t', '--target', help='target object name')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
file_input  = args.input
file_output = args.output
target_name = args.target

# making an empty list
list_clusters = []

# opening file for reading
with open (file_input, 'r') as fh:
    # reading file line-by-line
    for line in fh:
        # if line starts with '#', then skip
        if (line[0] == '#'):
            continue
        # splitting line
        (source_id, ra, dec, \
         parallax, dist_pc, dist_norm, \
         pmra, pmdec, \
         rv, rv_norm, \
         label) = line.split ()
        # appending data to list
        list_clusters.append (label)

# making a set
set_clusters = set (list_clusters)

# making an empty 2-D list for storing data
data = []
for i in range (len (set_clusters)):
    data.append ([])

# opening file for reading
with open (file_input, 'r') as fh:
    # reading file line-by-line
    for line in fh:
        # if line starts with '#', then skip
        if (line[0] == '#'):
            continue
        # splitting line
        (source_id, ra, dec, \
         parallax, dist_pc, dist_norm, \
         pmra, pmdec, \
         rv, rv_norm, \
         label) = line.split ()
        # converting string into integer
        source_id = int (source_id)
        label     = int (label)
        # converting string into float
        ra        = float (ra)
        dec       = float (dec)
        parallax  = float (parallax)
        dist_pc   = float (dist_pc)
        dist_norm = float (dist_norm)
        pmra      = float (pmra)
        pmdec     = float (pmdec)
        rv        = float (rv)
        rv_norm   = float (rv_norm)
        # appending data to lists
        data[label].append ([source_id, ra, dec, \
                             parallax, dist_pc, dist_norm, \
                             pmra, pmdec, rv, rv_norm])

# making fig object
fig    = matplotlib.figure.Figure ()

# making canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making axes object
ax1     = fig.add_subplot (221)

# making pmra and pmdec plot
ax1.set_xlabel ('Proper motion in RA [mas/yr]')
ax1.set_ylabel ('Proper motion in Dec [mas/yr]')
ax1.set_xlim (-30, +30)
ax1.set_ylim (-30, +30)
ax1.grid ()
for i in range (len (data)):
    # re-arrangement of data
    source_id, ra, dec, parallax, dist_pc, dist_norm, \
        pmra, pmdec, rv, rv_norm = numpy.array (data[i]).T
    # plotting data
    if (i < len (data) - 1):
        ax1.plot (pmra, pmdec, linestyle='None', marker='o', markersize=1, \
                  zorder=0.2, \
                  label=f'cluster {i}')
    else:
        ax1.plot (pmra, pmdec, linestyle='None', marker='.', markersize=1, \
                  zorder=0.1, \
                  label=f'field stars')
ax1.legend ()

# making axes object
ax2     = fig.add_subplot (222)

# making pmra and pmdec plot
ax2.set_xlabel ('Distance [pc]')
ax2.set_ylabel ('Radial velocity [km/s]')
ax2.set_xlim (0, 4000)
ax2.set_ylim (-100, +100)
ax2.grid ()
for i in range (len (data)):
    # re-arrangement of data
    source_id, ra, dec, parallax, dist_pc, dist_norm, \
        pmra, pmdec, rv, rv_norm = numpy.array (data[i]).T
    # plotting data
    if (i < len (data) - 1):
        ax2.plot (dist_pc, rv, linestyle='None', marker='o', markersize=1, \
                  zorder=0.2, \
                  label=f'cluster {i}')
    else:
        ax2.plot (dist_pc, rv, linestyle='None', marker='.', markersize=1, \
                  zorder=0.1, \
                  label=f'field stars')
ax2.legend ()

# making axes object
ax3     = fig.add_subplot (223)

# making pmra and pmdec plot
ax3.set_xlabel ('Proper motion in RA [mas/yr]')
ax3.set_ylabel ('Distance [pc]')
ax3.set_xlim (-30, +30)
ax3.set_ylim (0, 4000)
ax3.grid ()
for i in range (len (data)):
    # re-arrangement of data
    source_id, ra, dec, parallax, dist_pc, dist_norm, \
        pmra, pmdec, rv, rv_norm = numpy.array (data[i]).T
    # plotting data
    if (i < len (data) - 1):
        ax3.plot (pmra, dist_pc, linestyle='None', marker='o', markersize=1, \
                  zorder=0.2, \
                  label=f'cluster {i}')
    else:
        ax3.plot (pmra, dist_pc, linestyle='None', marker='.', markersize=1, \
                  zorder=0.1, \
                  label=f'field stars')
ax3.legend ()

# making axes object
ax4     = fig.add_subplot (224)

# making pmra and pmdec plot
ax4.set_xlabel ('Proper motion in Dec [mas/yr]')
ax4.set_ylabel ('Radial velocity [km/s]')
ax4.set_xlim (-30, +30)
ax4.set_ylim (-100, +100)
ax4.grid ()
for i in range (len (data)):
    # re-arrangement of data
    source_id, ra, dec, parallax, dist_pc, dist_norm, \
        pmra, pmdec, rv, rv_norm = numpy.array (data[i]).T
    # plotting data
    if (i < len (data) - 1):
        ax4.plot (pmdec, rv, linestyle='None', marker='o', markersize=1, \
                  zorder=0.2, \
                  label=f'cluster {i}')
    else:
        ax4.plot (pmdec, rv, linestyle='None', marker='.', markersize=1, \
                  zorder=0.1, \
                  label=f'field stars')
ax4.legend ()
        
# saving file
fig.suptitle (target_name)
fig.tight_layout ()
fig.savefig (file_output, dpi=150.0)
