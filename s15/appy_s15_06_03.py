#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/24 08:54:48 (UT+8) daisuke>
#

# data file
file_ubv = 'compil.ast.ubv-photometry/data/ubvmean.tab'

# priting header
print (f'# asteroid number, U-B colour index, B-V colour index')

# opening file
with open (file_ubv, 'r') as fh:
    # reading file line-by-line
    for line in fh:
        # extracting data
        number        = int (line[0:5])
        designation   = line[6:16]
        ub            = float (line[17:22])
        ub_err        = float (line[24:29])
        ub_obsnumber  = int (line[31:33])
        ub_phase_min  = float (line[34:40])
        ub_phase_max  = float (line[41:47])
        ub_phase_mean = float (line[48:54])
        bv            = float (line[55:60])
        bv_err        = float (line[62:67])
        bv_obsnumber  = int (line[69:71])
        bv_phase_min  = float (line[72:78])
        bv_phase_max  = float (line[79:85])
        bv_phase_mean = float (line[86:92])

        # printing extracted colour indices of asteroids
        if not ( (number == 0) or (ub > 9.0) or (bv > 9.0) ):
            print (f'{number:5d} : U-B = {ub:+6.3f} +/- {ub_err:5.3f},', \
                   f'B-V = {bv:+6.3f} +/- {bv_err:5.3f}')
