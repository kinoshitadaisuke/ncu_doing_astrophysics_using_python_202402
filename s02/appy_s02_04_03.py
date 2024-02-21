#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/21 15:22:21 (UT+8) daisuke>
#

# importing pathlib module
import pathlib

# file
file_taipei = '/usr/share/zoneinfo/Asia/Taipei'

# making a pathlib object
path_taipei = pathlib.Path (file_taipei)

# file status
info_taipei = path_taipei.stat ()

# printing information of file
print (f'file information of "{file_taipei}":')
print (f'  file mode         = {oct (info_taipei.st_mode)}')
print (f'  file size         = {info_taipei.st_size} bytes')
print (f'  last modification = {info_taipei.st_mtime} sec from 01/Jan/1970')
