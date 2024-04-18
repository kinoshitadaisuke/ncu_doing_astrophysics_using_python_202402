#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/04/18 20:30:08 (UT+8) daisuke>
#

# importing git module
import git

# URL of repository
url_repo = 'https://github.com/astrocatalogs/sne-1990-1999.git'

# directory name of downloaded repository
dir_repo = 'osc_1990_1999'

# downloading repository
repo = git.Repo.clone_from (url_repo, dir_repo)
