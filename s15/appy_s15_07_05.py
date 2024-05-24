#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/24 08:56:01 (UT+8) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.io.ascii

# data file for taxonomic classification
file_class = 'ast_taxonomy/data/taxonomy10.tab'

# data file for SDSS colour indices
file_colours = 'gbo.sdss-moc.phot/data/sdssmocadr4.tab'

# list of data files for NEOWISE albedo measurements
list_albedo_files = [
    'neowise_diameters_albedos_V2_0/data/neowise_ambos.csv',
    'neowise_diameters_albedos_V2_0/data/neowise_centaurs.csv',
    'neowise_diameters_albedos_V2_0/data/neowise_hildas.csv',
    'neowise_diameters_albedos_V2_0/data/neowise_jupiter_trojans.csv',
    'neowise_diameters_albedos_V2_0/data/neowise_mainbelt.csv',
    'neowise_diameters_albedos_V2_0/data/neowise_neos.csv',
]

# making empty dictionaries for storing data
dic_subclass = {}
dic_colours  = {}
dic_albedo   = {}

# opening data file
with open (file_class, 'r') as fh:
    # reading data file line-by-line
    for line in fh:
        # extracting data
        number    = int (line[0:7])
        bus_class = line[80:83]
        # finding taxonomic class
        if (bus_class[0] == 'C'):
            taxonomy = 'C'
        elif (bus_class[0] == 'S'):
            taxonomy = 'S'
        elif (bus_class[0] == 'X'):
            taxonomy = 'X'
        elif (bus_class[0] == 'V'):
            taxonomy = 'V'
        elif (bus_class[0] == 'D'):
            taxonomy = 'D'
        else:
            taxonomy = 'others'
        # printing taxonomic classification
        if not ( (taxonomy == 'others') or (number == 0) ):
            # adding data to dictionary
            dic_subclass[number] = taxonomy

# opening data file
with open (file_colours, 'r') as fh:
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
        dic_colours[number] = {}
        dic_colours[number]["ug"]     = ug
        dic_colours[number]["ug_err"] = ug_err
        dic_colours[number]["gr"]     = gr
        dic_colours[number]["gr_err"] = gr_err
        dic_colours[number]["ri"]     = ri
        dic_colours[number]["ri_err"] = ri_err
        dic_colours[number]["iz"]     = iz
        dic_colours[number]["iz_err"] = iz_err

# processing each data file
for file_data in list_albedo_files:
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

# finding asteroids with all the taxonomic classification,
# SDSS colour indices, and NEOWISE albedo measurements
print (f'# asteroid number, u-g, g-r, r-i, i-z, albedo, taxonomic type')
for i in sorted (dic_subclass.keys ()):
    # if there are all the taxonomic classification, SDSS colour indices,
    # and NEOWISE albedo, then printing those values
    if ( (i in dic_colours) and (i in dic_albedo) ):
        print (f'{i:6d} {dic_colours[i]["ug"]:5.2f}', \
               f'{dic_colours[i]["gr"]:5.2f} {dic_colours[i]["ri"]:5.2f}', \
               f'{dic_colours[i]["iz"]:5.2f} {dic_albedo[i]["albedo"]:5.3f}', \
               f'{dic_subclass[i]}')
