#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/18 16:26:57 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing subprocess module
import subprocess

# URL of GitHub repository
url_repo = 'https://github.com/architecture-building-systems/honey-badger.git'

# command for downloading GitHub repository
command_git = f'git clone {url_repo}'

# downloading GitHub repository
subprocess.run (command_git, shell=True)
