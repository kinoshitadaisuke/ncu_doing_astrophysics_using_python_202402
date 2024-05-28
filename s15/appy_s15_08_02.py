#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/28 08:37:51 (UT+8) daisuke>
#

# importing numpy module
import numpy

# importing scikit-learn
import sklearn.cluster

# input file name
file_input = 'appy_s15_08_00.data'

# output file name
file_output = 'appy_s15_08_02.data'

# parameters for DBSCAN analysis
epsilon = 5.0
n_min   = 10

# making empty lists for storing data
list_x  = []
list_y  = []

# opening file for reading
with open (file_input, 'r') as fh:
    # reading file line-by-line
    for line in fh:
        # if line starts with '#', then skip
        if (line[0] == '#'):
            continue
        # reading data
        (x_str, y_str, group) = line.split ()
        # conversion from string into float
        x = float (x_str)
        y = float (y_str)
        # appending data to lists
        list_x.append (x)
        list_y.append (y)

# making a numpy array for analysis
#
#  we now have data like [x1, x2, x3, ... , xN] and [y1, y2, y3, ..., yN].
#  for DBSCAN analysis, we need [ [x1, y1], [x2, y2], [x3, y3], ... ,[xN, yN] ]
#
data = numpy.stack ([list_x, list_y]).T

# carrying out DBSCAN analysis
db     = sklearn.cluster.DBSCAN (eps=epsilon, min_samples=n_min).fit (data)
labels = db.labels_

# opening file for writing
with open (file_output, 'w') as fh:
    # header of output file
    header = f'# feature X, feature Y, classification\n'
    # writing header of output file
    fh.write (header)
    # writing results of DBSCAN analysis
    for i in range (len (data)):
        record = f'{data[i][0]:8.3f} {data[i][1]:8.3f} {labels[i]}\n'
        fh.write (record)
