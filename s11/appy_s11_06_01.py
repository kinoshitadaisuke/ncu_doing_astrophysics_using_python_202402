#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/23 17:21:53 (Taiwan_Standard_Time_UT+8) daisuke>
#

# data file
file_ms = 'ms.data'

# opening data file
with open (file_ms, 'r') as fh_r:
    # reading data file line-by-line
    for line in fh_r:
        # strip
        line = line.strip ()
        # if line is empty, then stop the script
        if (line == ''):
            break
        # if line starts with '#', then skip
        if (line[0] == '#'):
            continue
        # splitting line
        fields = line.split ()
        # spectral type
        sptype = fields[0]
        # effective temperature
        teff = float (fields[1])
        # Gaia (b-r) colour index
        try:
            colour_br = float (fields[11])
        except:
            colour_br = 999.999
        # Gaia g-band absolute magnitude
        try:
            absmag_g = float (fields[13])
        except:
            absmag_g = 999.999
        # printing information
        if ( (colour_br < 100.0) and (absmag_g < 100.0) ):
            print (f'{sptype:5s} {teff:5.0f} {colour_br:+6.3f} {absmag_g:6.3f}')
