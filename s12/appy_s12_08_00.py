#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/02 08:22:05 (UT+8) daisuke>
#

# importing urllib module
import urllib.request

# importing ssl module
import ssl

# allow insecure downloading
ssl._create_default_https_context = ssl._create_unverified_context

# list of URL
list_url = [
    'http://exoplanetarchive.ipac.caltech.edu/data/ETSS/Kepler/005/754/97/' \
    + 'kplr009941662-2009201121230_slc.fits', \
    'http://exoplanetarchive.ipac.caltech.edu/data/ETSS/Kepler/005/754/97/' \
    + 'kplr009941662-2009231120729_slc.fits', \
    'http://exoplanetarchive.ipac.caltech.edu/data/ETSS/Kepler/005/754/97/' \
    + 'kplr009941662-2009259162342_slc.fits', \
    ]

# downloading each data file
for url_data in list_url:
    # output file
    file_output = url_data.split ('/')[-1]
    
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
