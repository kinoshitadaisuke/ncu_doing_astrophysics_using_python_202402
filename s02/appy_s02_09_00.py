#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/21 15:24:13 (UT+8) daisuke>
#

# importing urllib module
import urllib.request

# importing ssl module
import ssl

# allow insecure downloading
ssl._create_default_https_context = ssl._create_unverified_context

# URL of Yale Bright Star Catalogue
url_bsc = 'https://cdsarc.cds.unistra.fr/ftp/V/50/catalog.gz'

# output file name
file_bsc = 'catalog.gz'

# printing status
print (f'Now, opening {url_bsc}...')

# opening URL
with urllib.request.urlopen (url_bsc) as fh_read:
    # reading data
    data_byte = fh_read.read ()

# printing status
print (f'Retrieved data from {url_bsc}!')
    
# printing status
print (f'Now, writing data to file "{file_bsc}"...')

# opening file for writing
with open (file_bsc, 'wb') as fh_write:
    # writing data
    fh_write.write (data_byte)

# printing status
print (f'Finished writing data to file "{file_bsc}"!')
