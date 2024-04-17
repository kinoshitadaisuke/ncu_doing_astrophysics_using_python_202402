#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/18 18:19:06 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing git module
import git

# URL of repository
url_repo = 'https://github.com/paulfitz/exoplanets.git'

# directory name of downloaded repository
dir_repo = 'exoplanets'

# downloading repository
repo = git.Repo.clone_from (url_repo, dir_repo)
