#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/26 18:16:47 (UT+8) daisuke>
#

# importing numpy module
import numpy

# importing scikit-learn module
import sklearn.ensemble
import sklearn.inspection

# importing matplotlib
import matplotlib.figure
import matplotlib.backends.backend_agg

# data file
file_data = 'appy_s15_00_00.data'

# figure file
file_fig = 'appy_s15_00_04.png'

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
        (x_str, y_str, group) = line.split (',')
        # converting string into float
        x = float (x_str)
        y = float (y_str)
        # removing white spaces
        group = group.strip ()
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
classifier = sklearn.ensemble.RandomForestClassifier ()
classifier.fit (list_training_features, list_training_group)

#
# generating synthetic data for testing
#

# mean value of feature X for group A
mean_A_X = 1.0

# mean value of feature X for group B
mean_B_X = 3.0

# standard deviation of feature X for group A
stddev_A_X = 0.5

# standard deviation of feature X for group B
stddev_B_X = 0.5

# mean value of feature Y for group A
mean_A_Y = 9.0

# mean value of feature Y for group B
mean_B_Y = 7.0

# standard deviation of feature Y for group A
stddev_A_Y = 0.5

# standard deviation of feature Y for group B
stddev_B_Y = 0.5

# size of group A
n_A = 50

# size of group B
n_B = 50

# making a random number generator
rng = numpy.random.default_rng ()

# generating synthetic data
data_A_X = rng.normal (loc=mean_A_X, scale=stddev_A_X, size=n_A)
data_A_Y = rng.normal (loc=mean_A_Y, scale=stddev_A_Y, size=n_A)
data_B_X = rng.normal (loc=mean_B_X, scale=stddev_B_X, size=n_B)
data_B_Y = rng.normal (loc=mean_B_Y, scale=stddev_B_Y, size=n_B)

# modifying distribution
a = 0.06
b = 0.04
for i in range (n_A):
    data_A_X[i] = data_A_X[i] + a * i
    data_A_Y[i] = data_A_Y[i] + b * i
for i in range (n_B):
    data_B_X[i] = data_B_X[i] + a * i
    data_B_Y[i] = data_B_Y[i] + b * i
data_AB_X = numpy.concatenate ( [data_A_X, data_B_X] )
data_AB_Y = numpy.concatenate ( [data_A_Y, data_B_Y] )

# data for classification
array_test_features = numpy.transpose ( [data_AB_X, data_AB_Y] )

# classification of test dataset using Random Forest classifier
prediction = classifier.predict (array_test_features)

# making numpy arrays for plotting
classified_A_X = []
classified_A_Y = []
classified_B_X = []
classified_B_Y = []
for i in range (prediction.size):
    if (prediction[i] == 'A'):
        classified_A_X.append (array_test_features[i][0])
        classified_A_Y.append (array_test_features[i][1])
    elif (prediction[i] == 'B'):
        classified_B_X.append (array_test_features[i][0])
        classified_B_Y.append (array_test_features[i][1])
array_classified_A_X = numpy.array (classified_A_X)
array_classified_A_Y = numpy.array (classified_A_Y)
array_classified_B_X = numpy.array (classified_B_X)
array_classified_B_Y = numpy.array (classified_B_Y)

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
ax.plot (array_classified_A_X, array_classified_A_Y, \
         linestyle='None', marker='s', markersize=3, color='cyan', \
         label='Classified as A')
ax.plot (array_classified_B_X, array_classified_B_Y, \
         linestyle='None', marker='s', markersize=3, color='magenta', \
         label='Classified as B')

# title
ax.set_title ('Results of classification of test dataset')

# legend
ax.legend ()

# saving plot into a file
fig.savefig (file_fig, dpi=150)
