#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/04/18 20:29:31 (UT+8) daisuke>
#

# importing git module
import git

# URL of repository
url_repo = 'https://github.com/astrocatalogs/sne-pre-1990.git'

# directory name of downloaded repository
dir_repo = 'osc_0000_1989'

# downloading repository
repo = git.Repo.clone_from (url_repo, dir_repo)
