#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/27 16:43:46 (UT+8) daisuke>
#

# importing scikit-learn module
import sklearn.gaussian_process
import sklearn.inspection

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# training data file
file_training = 'appy_s15_07_08_training.data'

# testing data file
file_testing = 'appy_s15_07_08_testing.data'

# output file
file_output = 'appy_s15_07_10.png'

# making empty lists for storing data
list_training_number   = []
list_training_features = []
list_training_group    = []
list_testing_number    = []
list_testing_features  = []
list_testing_group     = []
list_training_c_colour = []
list_training_c_albedo = []
list_training_s_colour = []
list_training_s_albedo = []
list_testing_c_colour  = []
list_testing_c_albedo  = []
list_testing_s_colour  = []
list_testing_s_albedo  = []

# opening training data file
with open (file_training, 'r') as fh_training:
    # reading data file line-by-line
    for line in fh_training:
        # splitting data
        (number_str, ug_str, gr_str, ri_str, iz_str, albedo_str, subclass) \
            = line.split ()
        # converting string into integer
        number = int (number_str)
        # converting string into float
        ug     = float (ug_str)
        gr     = float (gr_str)
        ri     = float (ri_str)
        iz     = float (iz_str)
        albedo = float (albedo_str)
        # appending data to lists
        list_training_number.append (number)
        list_training_features.append ([ug, gr, ri, iz, albedo])
        list_training_group.append (subclass)
        if (subclass == 'C'):
            list_training_c_colour.append (iz)
            list_training_c_albedo.append (albedo)
        elif (subclass == 'S'):
            list_training_s_colour.append (iz)
            list_training_s_albedo.append (albedo)

# building a classifier model by learning training dataset
classifier = sklearn.gaussian_process.GaussianProcessClassifier ()
classifier.fit (list_training_features, list_training_group)

# opening testing data file
with open (file_testing, 'r') as fh_testing:
    # reading data file line-by-line
    for line in fh_testing:
        # splitting data
        (number_str, ug_str, gr_str, ri_str, iz_str, albedo_str, subclass) \
            = line.split ()
        # converting string into integer
        number = int (number_str)
        # converting string into float
        ug     = float (ug_str)
        gr     = float (gr_str)
        ri     = float (ri_str)
        iz     = float (iz_str)
        albedo = float (albedo_str)
        # appending data to lists
        list_testing_number.append (number)
        list_testing_features.append ([ug, gr, ri, iz, albedo])
        list_testing_group.append (subclass)

# classification of testing data
prediction = classifier.predict (list_testing_features)

# results of classification
for i in range (len (prediction)):
    # data
    subclass = prediction[i]
    iz       = list_testing_features[i][3]
    albedo   = list_testing_features[i][4]
    # appending data to lists
    if (subclass == 'C'):
        list_testing_c_colour.append (iz)
        list_testing_c_albedo.append (albedo)
    elif (subclass == 'S'):
        list_testing_s_colour.append (iz)
        list_testing_s_albedo.append (albedo)

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('SDSS i-z colour index')
ax.set_ylabel ('NEOWISE albedo')

# axes
ax.grid ()

# plotting data
ax.plot (list_training_c_colour, list_training_c_albedo, \
         linestyle='None', marker='o', markersize=5, color='blue', \
         label='C-type training data')
ax.plot (list_training_s_colour, list_training_s_albedo, \
         linestyle='None', marker='^', markersize=5, color='red', \
         label='S-type training data')
ax.plot (list_testing_c_colour, list_testing_c_albedo, \
         linestyle='None', marker='s', markersize=5, color='cyan', \
         label='C-type testing data')
ax.plot (list_testing_s_colour, list_testing_s_albedo, \
         linestyle='None', marker='*', markersize=5, color='magenta', \
         label='S-type testing data')

# legend
ax.legend ()

# saving plot into file
fig.savefig (file_output, dpi=150)
