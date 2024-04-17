#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/18 19:12:45 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing git module
import git

# URL of repository
url_repo = 'https://github.com/brettonw/YaleBrightStarCatalog.git'

# directory name of downloaded repository
dir_repo = 'bsc'

# downloading repository
repo = git.Repo.clone_from (url_repo, dir_repo)
