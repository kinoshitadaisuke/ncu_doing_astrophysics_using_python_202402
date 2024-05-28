#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/28 09:26:21 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing scikit-learn
import sklearn.cluster

# construction of parser object for argparse
descr  = f'finding star cluster members using parallax, rv, pmra, and pmdec'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-i', '--input', help='input file name')
parser.add_argument ('-o', '--output', help='output file name')
parser.add_argument ('-d', '--norm-factor-distance', type=float, default=30, \
                     help='normalisation factor for distance in pc (default: 30)')
parser.add_argument ('-r', '--norm-factor-rv', type=float, default=2, \
                     help='normalisation factor for rv in km/s (default: 2)')
parser.add_argument ('-e', '--eps', type=float, default=1.0, \
                     help='parameter eps for DBSCAN analysis (default: 1)')
parser.add_argument ('-n', '--min-samples', type=int, default=30, \
                     help='parameter min-samples for DBSCAN analysis (default: 30)')
parser.add_argument ('-v', '--verbose', action='store_true', default=False, \
                     help='verbose mode (default: False)')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
file_input      = args.input
file_output     = args.output
normfactor_dist = args.norm_factor_distance
normfactor_rv   = args.norm_factor_rv
eps             = args.eps
min_samples     = args.min_samples
verbose         = args.verbose

# making empty lists for storing data
list_id        = []
list_ra        = []
list_dec       = []
list_parallax  = []
list_dist      = []
list_dist_norm = []
list_pmra      = []
list_pmdec     = []
list_rv        = []
list_rv_norm   = []
list_stars     = []

# printing status
if (verbose):
    print (f'Now, reading Gaia DR3 data file...')

# opening file for reading
with open (file_input, 'r') as fh:
    # reading file line-by-line
    for line in fh:
        # if line starts with '#', then skip
        if (line[0] == '#'):
            continue
        # splitting line
        (source_id, ra, ra_err, dec, dec_err, \
         parallax, parallax_err, parallax_snr, \
         pmra, pmra_err, pmdec, pmdec_err, \
         rv, rv_err, \
         mag_b, mag_b_snr, mag_g, mag_g_snr, mag_r, mag_r_snr, \
         colour_br, colour_bg, colour_gr) = line.split ()
        # if value of radial velocity is "nan", then skip
        if (rv == 'nan'):
            continue
        # converting string into integer
        source_id = int (source_id)
        # converting string into float
        ra       = float (ra)
        dec      = float (dec)
        parallax = float (parallax)
        pmra     = float (pmra)
        pmdec    = float (pmdec)
        rv       = float (rv)
        # calculation of distance in pc
        dist_pc = 1000.0 / parallax
        # normalisation of distance in pc
        dist_norm = dist_pc / normfactor_dist
        # normalisation of radial velocity in km/s
        rv_norm = rv / normfactor_rv
        # appending data to lists
        list_id.append (source_id)
        list_ra.append (ra)
        list_dec.append (dec)
        list_parallax.append (parallax)
        list_dist.append (dist_pc)
        list_dist_norm.append (dist_norm)
        list_pmra.append (pmra)
        list_pmdec.append (pmdec)
        list_rv.append (rv)
        list_rv_norm.append (rv_norm)
       
# printing status
if (verbose):
    print (f'Finished reading Gaia DR3 data file!')

# printing status
if (verbose):
    print (f'Now, constructing Numpy array...')

# making Numpy arrays
array_id        = numpy.array (list_id)
array_ra        = numpy.array (list_ra)
array_dec       = numpy.array (list_dec)
array_parallax  = numpy.array (list_parallax)
array_dist      = numpy.array (list_dist)
array_dist_norm = numpy.array (list_dist_norm)
array_pmra      = numpy.array (list_pmra)
array_pmdec     = numpy.array (list_pmdec)
array_rv        = numpy.array (list_rv)
array_rv_norm   = numpy.array (list_rv_norm)

# constructing a Numpy array for DBSCAN analysis
stars = numpy.stack ([ \
                       array_dist_norm, \
                       array_pmra, \
                       array_pmdec, \
                       array_rv_norm \
                      ]).transpose ()
    
# printing status
if (verbose):
    print (f'Finished constructing Numpy array!')
    
# printing status
if (verbose):
    print (f'Now, doing DBSCAN analysis...')

# clustering analysis by DBSCAN
result_dbscan = sklearn.cluster.DBSCAN (eps=eps, \
                                        min_samples=min_samples, \
                                        n_jobs=-1).fit (stars)
labels = result_dbscan.labels_

# printing status
if (verbose):
    print (f'Finished doing DBSCAN analysis!')

# printing status
if (verbose):
    print (f'Now, writing results into output file...')

# opening file for writing
with open (file_output, 'w') as fh:
    # header of output file
    header = f'#\n' \
        + f'# Results of DBSCAN analysis\n' \
        + f'#\n' \
        + f'#  format of this data file\n' \
        + f'#\n' \
        + f'#   column 01 : source ID\n' \
        + f'#   column 02 : RA in deg\n' \
        + f'#   column 03 : Dec in deg\n' \
        + f'#   column 04 : parallax in mas\n' \
        + f'#   column 05 : distance in pc\n' \
        + f'#   column 06 : normalised distance\n' \
        + f'#   column 07 : proper motion in RA in mas/yr\n' \
        + f'#   column 08 : proper motion in Dec in mas/yr\n' \
        + f'#   column 09 : radial velocity in km/s\n' \
        + f'#   column 10 : normalised radial velocity\n' \
        + f'#   column 11 : labels (0=1st cluster, 1=2nd cluster, ... , -1=field stars)\n' \
        + f'#\n'
    # writing header
    fh.write (header)

    # writing data of individual stars
    for i in range (len (array_id)):
        record = f"{array_id[i]:19d}" \
            + f" {array_ra[i]:12.8f}" \
            + f" {array_dec[i]:12.8f}" \
            + f" {array_parallax[i]:8.3f}" \
            + f" {array_dist[i]:8.3f}" \
            + f" {array_dist_norm[i]:8.3f}" \
            + f" {array_pmra[i]:8.3f}" \
            + f" {array_pmdec[i]:8.3f}" \
            + f" {array_rv[i]:12.6f}" \
            + f" {array_rv_norm[i]:12.6f}" \
            + f" {labels[i]}\n"
        fh.write (record)

# printing status
if (verbose):
    print (f'Finished writing results into output file!')
