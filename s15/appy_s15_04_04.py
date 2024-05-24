#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/24 08:47:03 (UT+8) daisuke>
#

# importing numpy module
import numpy

# importing scikit-learn module
import sklearn.gaussian_process
import sklearn.inspection

# importing matplotlib
import matplotlib.figure
import matplotlib.backends.backend_agg

# training data file
file_training = 'ai2023_s15_04_02_training.data'

# testing data file
file_testing = 'ai2023_s15_04_02_testing.data'

# figure file
file_fig = 'ai2023_s15_04_04.png'

# making empty lists for storing data
list_a_x               = []
list_a_y               = []
list_b_x               = []
list_b_y               = []
list_c_x               = []
list_c_y               = []
list_training_features = []
list_training_group    = []

# opening training data file
with open (file_training, 'r') as fh:
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
        elif (group == 'C'):
            list_c_x.append (x)
            list_c_y.append (y)
        list_training_features.append ([x, y])
        list_training_group.append (group)


# making numpy arrays
array_a_x               = numpy.array (list_a_x)
array_a_y               = numpy.array (list_a_y)
array_b_x               = numpy.array (list_b_x)
array_b_y               = numpy.array (list_b_y)
array_c_x               = numpy.array (list_c_x)
array_c_y               = numpy.array (list_c_y)
array_training_features = numpy.array (list_training_features)
array_training_group    = numpy.array (list_training_group)
        
# building a model by learning training dataset
classifier = sklearn.gaussian_process.GaussianProcessClassifier ()
classifier.fit (list_training_features, list_training_group)

# making empty lists for storing data
list_a_x              = []
list_a_y              = []
list_b_x              = []
list_b_y              = []
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
        (x_str, y_str, group) = line.split ()
        # converting string into float
        x = float (x_str)
        y = float (y_str)
        # appending data to lists
        list_testing_features.append ([x, y])

# making numpy arrays
array_testing_features = numpy.array (list_testing_features)
array_testing_group    = numpy.array (list_testing_group)

# classification of testing dataset
prediction = classifier.predict (array_testing_features)

# making numpy arrays for plotting
classified_A_X = []
classified_A_Y = []
classified_B_X = []
classified_B_Y = []
classified_C_X = []
classified_C_Y = []
for i in range (prediction.size):
    if (prediction[i] == 'A'):
        classified_A_X.append (array_testing_features[i][0])
        classified_A_Y.append (array_testing_features[i][1])
    elif (prediction[i] == 'B'):
        classified_B_X.append (array_testing_features[i][0])
        classified_B_Y.append (array_testing_features[i][1])
    elif (prediction[i] == 'C'):
        classified_C_X.append (array_testing_features[i][0])
        classified_C_Y.append (array_testing_features[i][1])
array_classified_A_X = numpy.array (classified_A_X)
array_classified_A_Y = numpy.array (classified_A_Y)
array_classified_B_X = numpy.array (classified_B_X)
array_classified_B_Y = numpy.array (classified_B_Y)
array_classified_C_X = numpy.array (classified_C_X)
array_classified_C_Y = numpy.array (classified_C_Y)

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
ax.plot (array_c_x, array_c_y, \
         linestyle='None', marker='s', markersize=3, color='green', \
         label='Known B')
ax.plot (array_classified_A_X, array_classified_A_Y, \
         linestyle='None', marker='*', markersize=3, color='cyan', \
         label='Classified as A')
ax.plot (array_classified_B_X, array_classified_B_Y, \
         linestyle='None', marker='*', markersize=3, color='magenta', \
         label='Classified as B')
ax.plot (array_classified_C_X, array_classified_C_Y, \
         linestyle='None', marker='*', markersize=3, color='lime', \
         label='Classified as C')

# title
ax.set_title ('Results of classification of testing dataset')

# legend
ax.legend ()

# saving plot into a file
fig.savefig (file_fig, dpi=100)
