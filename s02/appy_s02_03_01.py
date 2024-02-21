#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/21 15:21:40 (UT+8) daisuke>
#

# importing urllib module
import urllib.request

# importing ssl module
import ssl

# allow insecure downloading
ssl._create_default_https_context = ssl._create_unverified_context

# URL of a resource
url_map = 'https://www.ncu.edu.tw/upload/ckupload/20230103_02011120.png'

# output file name
file_output = 'ncu_map.png'

# printing status
print (f'Now, opening {url_map}...')

# opening URL
with urllib.request.urlopen (url_map) as fh_read:
    # reading data
    data_byte = fh_read.read ()

# printing status
print (f'Retrieved data from {url_map}!')
    
# printing status
print (f'Now, writing data to file "{file_output}"...')

# opening file for writing
with open (file_output, 'wb') as fh_write:
    # writing data into file
    fh_write.write (data_byte)

# printing status
print (f'Finished writing data to file "{file_output}"!')
