#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/23 16:53:05 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing urllib module
import urllib.request

# importing ssl module
import ssl

# allow insecure downloading
ssl._create_default_https_context = ssl._create_unverified_context

# URL of data file
url_data = 'https://www.pas.rochester.edu/~emamajek/' \
    + 'EEM_dwarf_UBVIJHK_colors_Teff.txt'

# output file name
file_output = 'ms.data'

# printing status
print (f'Now, fetching {url_data}...')

# opening URL
with urllib.request.urlopen (url_data) as fh_read:
    # reading data
    data_byte = fh_read.read ()

# printing status
print (f'Finished fetching {url_data}!')

# printing status
print (f'Now, writing data into file "{file_output}"...')

# opening file for writing
with open (file_output, 'wb') as fh_write:
    # writing data
    fh_write.write (data_byte)

# printing status
print (f'Finished writing data into file "{file_output}"!')
