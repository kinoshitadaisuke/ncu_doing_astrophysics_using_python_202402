#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/19 15:49:16 (Taiwan_Standard_Time_UT+8) daisuke>
#

# original CSV file
file_original = 'ned1d.csv'

# output new CSV file
file_new = 'ned1d_new.csv'

# header for new CSV file
header = f'"Exclusion Code","D","G","Galaxy ID","m-M","err","D (Mpc)",' \
    + f'"Method","REFCODE","","","Hubble const.","Adopted LMC modulus",' \
    + f'"Date (Yr. - 1980)","NOTES"\n'

# opening new CSV file for writing
with open (file_new, 'w') as fh_w:
    # writing a new header
    fh_w.write (header)
    # opening original CSV file for reading
    with open (file_original, 'r') as fh_r:
        # reading the file line-by-line
        for line in fh_r:
            # if finding "FRN" at the beginning of the line, then skip
            if (line[:5] == '"FRN"'):
                continue
            # writing data into new file
            fh_w.write (line)
