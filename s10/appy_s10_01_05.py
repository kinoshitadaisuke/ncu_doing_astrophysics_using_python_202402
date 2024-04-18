#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/04/18 20:27:07 (UT+8) daisuke>
#

# importing git module
import git

# URL of repository
url_repo = 'https://github.com/astronexus/HYG-Database.git'

# directory name of downloaded repository
dir_repo = 'hyg'

# downloading repository
repo = git.Repo.clone_from (url_repo, dir_repo)
