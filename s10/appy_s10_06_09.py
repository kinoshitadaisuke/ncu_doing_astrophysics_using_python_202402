#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/19 23:41:30 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing git module
import git

# URL of repository
url_repo = 'https://github.com/astrocatalogs/sne-2000-2004.git'

# directory name of downloaded repository
dir_repo = 'osc_2000_2004'

# downloading repository
repo = git.Repo.clone_from (url_repo, dir_repo)
