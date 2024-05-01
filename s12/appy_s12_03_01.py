#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/12/01 05:48:48 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing tarfile module
import tarfile

# gzipped tar file
file_targz = 'linear.tar.gz'

# target directory for extraction of files
dir_target = 'linear'

# opening tar file
with tarfile.open (file_targz, 'r:gz') as fh_targz:
    # extracting files
    fh_targz.extractall (path=dir_target)
