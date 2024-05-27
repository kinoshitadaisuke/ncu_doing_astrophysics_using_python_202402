#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/27 18:19:30 (UT+8) daisuke>
#

# importing numpy module
import numpy

# importing scikit-learn module
import sklearn.gaussian_process
import sklearn.naive_bayes
import sklearn.inspection

# importing matplotlib
import matplotlib.figure
import matplotlib.backends.backend_agg

# data file
file_data = 'appy_s15_02_02_training.data'

# figure file
file_fig = 'appy_s15_02_03.png'

# making empty lists for storing data
list_a_x               = []
list_a_y               = []
list_b_x               = []
list_b_y               = []
list_training_features = []
list_training_group    = []

# opening data file
with open (file_data, 'r') as fh:
    # reading data line-by-line
    for line in fh:
        # stripping line feed at the end of line
        line = line.strip ()
        # skipping line if the line starts with '#'
        if (line[0] == '#'):
            continue
        # splitting line into fields
        (x_str, y_str, group) = line.split ()
        # converting string into float
        x = float (x_str)
        y = float (y_str)
        # appending data to lists
        if (group == 'A'):
            list_a_x.append (x)
            list_a_y.append (y)
        elif (group == 'B'):
            list_b_x.append (x)
            list_b_y.append (y)
        list_training_features.append ([x, y])
        list_training_group.append (group)


# making numpy arrays
array_a_x               = numpy.array (list_a_x)
array_a_y               = numpy.array (list_a_y)
array_b_x               = numpy.array (list_b_x)
array_b_y               = numpy.array (list_b_y)
array_training_features = numpy.array (list_training_features)
array_training_group    = numpy.array (list_training_group)
        
# building a model by learning training dataset
classifier = sklearn.gaussian_process.GaussianProcessClassifier ()
classifier.fit (list_training_features, list_training_group)

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Feature X [arbitrary unit]')
ax.set_ylabel ('Feature Y [arbitrary unit]')

# axes
ax.grid ()

# plotting result of training
sklearn.inspection.DecisionBoundaryDisplay.from_estimator \
    (classifier, array_training_features, \
     response_method='predict', \
     ax=ax, alpha=0.3, cmap='coolwarm')

# plotting data
ax.plot (array_a_x, array_a_y, \
         linestyle='None', marker='o', markersize=3, color='blue', \
         label='Known A')
ax.plot (array_b_x, array_b_y, \
         linestyle='None', marker='^', markersize=3, color='red', \
         label='Known B')

# title
ax.set_title ('Classifier built by learning training dataset')

# legend
ax.legend ()

# saving plot into a file
fig.savefig (file_fig, dpi=150)
