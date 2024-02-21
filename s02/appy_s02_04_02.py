#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/21 15:22:15 (UT+8) daisuke>
#

# importing pathlib module
import pathlib

# directory name
dir_zone = '/usr/share/zoneinfo'

# making a pathlib object
path_zone = pathlib.Path (dir_zone)

# finding directory contents
list_files = path_zone.iterdir ()

# printing directory contents
print (f'directory contents of "{path_zone}":')
for filename in list_files:
    # printing file name
    print (f'  {filename}')
