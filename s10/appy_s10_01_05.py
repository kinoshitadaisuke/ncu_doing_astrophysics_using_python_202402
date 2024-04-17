#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/18 17:40:17 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing git module
import git

# URL of repository
url_repo = 'https://github.com/astronexus/HYG-Database.git'

# directory name of downloaded repository
dir_repo = 'hyg'

# downloading repository
repo = git.Repo.clone_from (url_repo, dir_repo)
