#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/24 08:55:14 (UT+8) daisuke>
#

# data file
file_albedo = 'compil.ast.albedos/data/albedos.tab'

# printing header
print (f'# asteroid number, albedo, albedo error')

# opening data file
with open (file_albedo, 'r') as fh:
    # reading data file line-by-line
    for line in fh:
        # extracting data
        number          = int (line[0:6])
        iras_albedo     = float (line[45:51])
        iras_albedo_err = float (line[52:57])
        quality_code    = int (line[58:59])
        # rejecting data if no measurement done by IRAS
        if (quality_code == 0):
            continue
        # printing data
        if (number > 0):
            print (f'{number:6d} {iras_albedo:5.3f} {iras_albedo_err:5.3f}')
