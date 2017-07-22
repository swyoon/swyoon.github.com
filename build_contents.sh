#! /bin/zsh

pyenv exec pelican -s content -s publishconf.py
pyenv exec ghp-import output -b master

