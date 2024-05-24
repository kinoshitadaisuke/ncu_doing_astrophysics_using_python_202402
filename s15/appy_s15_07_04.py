#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/24 08:55:48 (UT+8) daisuke>
#

# importing astropy module
import astropy.io.ascii

# list of data files
list_files = [
    'neowise_diameters_albedos_V2_0/data/neowise_ambos.csv',
    'neowise_diameters_albedos_V2_0/data/neowise_centaurs.csv',
    'neowise_diameters_albedos_V2_0/data/neowise_hildas.csv',
    'neowise_diameters_albedos_V2_0/data/neowise_jupiter_trojans.csv',
    'neowise_diameters_albedos_V2_0/data/neowise_mainbelt.csv',
    'neowise_diameters_albedos_V2_0/data/neowise_neos.csv',
]

# making an empty dictionary for storing data
dic_albedo = {}

# processing each data file
for file_data in list_files:
    # reading data file
    table_data = astropy.io.ascii.read (file_data, format='csv')
    for record in table_data:
        # asteroid number
        number = record[0]
        # visual albedo
        albedo = record[13]
        # error of visual albedo
        albedo_err = record[14]
        # skipping non-numbered asteroids
        if (number == 0):
            continue
        # skipping asteroids with negative albedo values
        if (albedo < 0.0):
            continue
        # adding data into dictionary
        if not (number in dic_albedo):
            dic_albedo[number]               = {}
            dic_albedo[number]['albedo']     = albedo
            dic_albedo[number]['albedo_err'] = albedo_err

# printing extracted data
for i in sorted (dic_albedo.keys ()):
    print (f'{i:6d} :', \
           f'{dic_albedo[i]["albedo"]:5.3f}', \
           f'+/-{dic_albedo[i]["albedo_err"]:5.3f}')
