#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/27 15:41:57 (UT+8) daisuke>
#

# importing numpy module
import numpy

# importing scikit-learn module
import sklearn.gaussian_process
import sklearn.inspection

# importing matplotlib
import matplotlib.figure
import matplotlib.backends.backend_agg

# data file
file_training = 'appy_s15_05_07_training.data'

# data file
file_testing = 'appy_s15_05_07_testing.data'

# figure file
file_fig = 'appy_s15_05_08.png'

# making empty lists for storing data
list_a_x               = []
list_a_y               = []
list_a_z               = []
list_b_x               = []
list_b_y               = []
list_b_z               = []
list_training_features = []
list_training_group    = []

# opening data file
with open (file_training, 'r') as fh:
    # reading data line-by-line
    for line in fh:
        # stripping line feed at the end of line
        line = line.strip ()
        # skipping line if the line starts with '#'
        if (line[0] == '#'):
            continue
        # splitting line into fields
        (x_str, y_str, z_str, group) = line.split ()
        # converting string into float
        x = float (x_str)
        y = float (y_str)
        z = float (z_str)
        # appending data to lists
        if (group == 'A'):
            list_a_x.append (x)
            list_a_y.append (y)
            list_a_z.append (z)
        elif (group == 'B'):
            list_b_x.append (x)
            list_b_y.append (y)
            list_b_z.append (z)
        list_training_features.append ([x, y, z])
        list_training_group.append (group)


# making numpy arrays
array_a_x               = numpy.array (list_a_x)
array_a_y               = numpy.array (list_a_y)
array_a_z               = numpy.array (list_a_z)
array_b_x               = numpy.array (list_b_x)
array_b_y               = numpy.array (list_b_y)
array_b_z               = numpy.array (list_b_z)
array_training_features = numpy.array (list_training_features)
array_training_group    = numpy.array (list_training_group)
        
# building a model by learning training dataset
classifier = sklearn.gaussian_process.GaussianProcessClassifier ()
classifier.fit (list_training_features, list_training_group)

# making empty lists for storing data
list_a_x              = []
list_a_y              = []
list_a_z              = []
list_b_x              = []
list_b_y              = []
list_b_z              = []
list_testing_features = []
list_testing_group    = []

# opening testing data file
with open (file_testing, 'r') as fh:
    # reading data line-by-line
    for line in fh:
        # stripping line feed at the end of line
        line = line.strip ()
        # skipping line if the line starts with '#'
        if (line[0] == '#'):
            continue
        # splitting line into fields
        (x_str, y_str, z_str, group) = line.split ()
        # converting string into float
        x = float (x_str)
        y = float (y_str)
        z = float (z_str)
        # appending data to lists
        list_testing_features.append ([x, y, z])
        list_testing_group.append (group)

# making numpy arrays
array_testing_features = numpy.array (list_testing_features)
array_testing_group    = numpy.array (list_testing_group)

# classification of testing dataset
prediction = classifier.predict (array_testing_features)

# making numpy arrays for plotting
classified_A_X = []
classified_A_Y = []
classified_A_Z = []
classified_B_X = []
classified_B_Y = []
classified_B_Z = []
for i in range (prediction.size):
    if (prediction[i] == 'A'):
        classified_A_X.append (array_testing_features[i][0])
        classified_A_Y.append (array_testing_features[i][1])
        classified_A_Z.append (array_testing_features[i][2])
    elif (prediction[i] == 'B'):
        classified_B_X.append (array_testing_features[i][0])
        classified_B_Y.append (array_testing_features[i][1])
        classified_B_Z.append (array_testing_features[i][2])
array_classified_A_X = numpy.array (classified_A_X)
array_classified_A_Y = numpy.array (classified_A_Y)
array_classified_A_Z = numpy.array (classified_A_Z)
array_classified_B_X = numpy.array (classified_B_X)
array_classified_B_Y = numpy.array (classified_B_Y)
array_classified_B_Z = numpy.array (classified_B_Z)

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax1    = fig.add_subplot (121)
ax2    = fig.add_subplot (122)

# labels
ax1.set_xlabel ('Feature X [arbitrary unit]')
ax1.set_ylabel ('Feature Y [arbitrary unit]')

# axes
ax1.grid ()

# plotting data
ax1.plot (array_a_x, array_a_y, \
          linestyle='None', marker='o', markersize=3, color='blue', \
          label='Known A')
ax1.plot (array_b_x, array_b_y, \
          linestyle='None', marker='^', markersize=3, color='red', \
          label='Known B')
ax1.plot (array_classified_A_X, array_classified_A_Y, \
          linestyle='None', marker='s', markersize=3, color='cyan', \
          label='classified as A')
ax1.plot (array_classified_B_X, array_classified_B_Y, \
          linestyle='None', marker='s', markersize=3, color='magenta', \
          label='classified as B')

# title
ax1.set_title ('Results of classification')

# legend
ax1.legend ()

# labels
ax2.set_xlabel ('Feature X [arbitrary unit]')
ax2.set_ylabel ('Feature Z [arbitrary unit]')

# axes
ax2.grid ()

# plotting data
ax2.plot (array_a_x, array_a_z, \
          linestyle='None', marker='o', markersize=3, color='blue', \
          label='Known A')
ax2.plot (array_b_x, array_b_z, \
          linestyle='None', marker='^', markersize=3, color='red', \
          label='Known B')
ax2.plot (array_classified_A_X, array_classified_A_Z, \
          linestyle='None', marker='s', markersize=3, color='cyan', \
          label='classified as A')
ax2.plot (array_classified_B_X, array_classified_B_Z, \
          linestyle='None', marker='s', markersize=3, color='magenta', \
          label='classified as B')

# title
ax2.set_title ('Results of classification')

# legend
ax2.legend ()

# saving plot into a file
fig.tight_layout ()
fig.savefig (file_fig, dpi=150)
