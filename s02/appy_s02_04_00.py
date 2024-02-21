#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/21 15:22:00 (UT+8) daisuke>
#

# importing pathlib module
import pathlib

# file name
file_hosts = '/etc/hosts'

# making a pathlib object
path_hosts = pathlib.Path (file_hosts)

# existence check
if (path_hosts.exists ()):
    print (f'The file "{path_hosts}" exists!')
else:
    print (f'The file "{path_hosts}" DOES NOT exist!')
