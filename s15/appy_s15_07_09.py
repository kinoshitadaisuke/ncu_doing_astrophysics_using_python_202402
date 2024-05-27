#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/27 16:41:36 (UT+8) daisuke>
#

# importing scikit-learn module
import sklearn.gaussian_process
import sklearn.inspection

# training data file
file_training = 'appy_s15_07_08_training.data'

# testing data file
file_testing = 'appy_s15_07_08_testing.data'

# making empty lists for storing data
list_training_number   = []
list_training_features = []
list_training_group    = []
list_testing_number    = []
list_testing_features  = []
list_testing_group     = []

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

# printing results of classification
for i in range (len (prediction)):
    if (prediction[i] != list_testing_group[i]):
        print (f'{list_testing_number[i]:6d} :', \
               f'u-g={list_testing_features[i][0]:+5.2f},', \
               f'g-r={list_testing_features[i][1]:+5.2f},', \
               f'r-i={list_testing_features[i][2]:+5.2f},', \
               f'i-z={list_testing_features[i][3]:+5.2f},', \
               f'p={list_testing_features[i][4]:5.3f},', \
               f'{list_testing_group[i]}', \
               f'==> {prediction[i]} [failed]')
    else:
        print (f'{list_testing_number[i]:6d} :', \
               f'u-g={list_testing_features[i][0]:+5.2f},', \
               f'g-r={list_testing_features[i][1]:+5.2f},', \
               f'r-i={list_testing_features[i][2]:+5.2f},', \
               f'i-z={list_testing_features[i][3]:+5.2f},', \
               f'p={list_testing_features[i][4]:5.3f},', \
               f'{list_testing_group[i]}', \
               f'==> {prediction[i]}')
