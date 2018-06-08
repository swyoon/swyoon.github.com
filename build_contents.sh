#! /bin/zsh

pelican -s content -s publishconf.py --ignore-cache
ghp-import output -b master

