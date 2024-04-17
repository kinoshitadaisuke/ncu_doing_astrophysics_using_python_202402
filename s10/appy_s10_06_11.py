#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/19 23:49:00 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing git module
import git

# URL of repository
url_repo = 'https://github.com/astrocatalogs/sne-2005-2009.git'

# directory name of downloaded repository
dir_repo = 'osc_2005_2009'

# downloading repository
repo = git.Repo.clone_from (url_repo, dir_repo)
