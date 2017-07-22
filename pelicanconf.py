#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Sangwoong Yoon'
SITENAME = "swyoon's blog"
SITEURL = 'https://swyoon.github.io'
SITETITLE = AUTHOR
SITESUBTITLE = 'Machine Learning Researcher'

PATH = 'content'

TIMEZONE = 'Asia/Seoul'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MAIN_MENU = False
USE_FOLDER_AS_CATEGORY = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

# Blogroll
LINKS = (('Archives', '/archives.html'),
         ('Categories', '/categories.html'),
        ('Tags', '/tags.html'))

# Social widget
SOCIAL = (('github', 'https://www.github.com/swyoon'),
          ('facebook', 'https://www.facebook.com/sangwoong.yoon.18'))

DEFAULT_PAGINATION = 10

THEME = "/home/sangwoong/pelican-themes/Flex"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# added by swyoon
MARKUP = ('md', 'ipynb')

PLUGIN_PATH = ['./plugins']
PLUGINS = ['ipynb.markup']
