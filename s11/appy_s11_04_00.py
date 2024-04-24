#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/23 08:54:59 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.io.votable

# VOTable file name
file_votable = "m3.vot.gz"

# output file name
file_output = 'm3.list'

# reading VOTable
table = astropy.io.votable.parse_single_table (file_votable).to_table ()

# data
data_id        = numpy.array (table['source_id'])
data_ra        = numpy.array (table['ra'])
data_dec       = numpy.array (table['dec'])
data_parallax  = numpy.array (table['parallax'])
data_pmra      = numpy.array (table['pmra'])
data_pmdec     = numpy.array (table['pmdec'])
data_g         = numpy.array (table['phot_g_mean_mag'])
data_gr        = numpy.array (table['g_rp'])

# opening file for writing
with open (file_output, 'w') as fh:
    # writing header
    header = '# ID, RA, Dec, parallax, pm in RA, pm in Dec, g mag, g-r colour\n'
    fh.write (header)

    # writing data
    for i in range ( len (data_id) ):
        # if no parallax measurement is available, then skip
        if ( numpy.isnan (data_parallax[i]) ):
            continue
        # if measured parallax value is negative, then skip
        if (data_parallax[i] < 0.0):
            continue
        # data
        data = f"{data_id[i]:19d} {data_ra[i]:8.4f} {data_dec[i]:+8.4f}" \
            + f" {data_parallax[i]:8.4f}" \
            + f" {data_pmra[i]:+8.3f} {data_pmdec[i]:+8.3f}" \
            + f" {data_g[i]:+6.3f} {data_gr[i]:+6.3f}\n"
        # writing data
        fh.write (data)
