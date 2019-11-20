#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Sangwoong Yoon'
SITENAME = "swyoon's blog"
SITEURL = 'https://swyoon.github.io'
# SITEURL = 'http://swyoon.iptime.org:22002'
SITETITLE = AUTHOR
SITESUBTITLE = 'Machine learning researcher'
SITELOGO = SITEURL + '/images/sangwoong_yoon_small.jpg'

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
LINKS = (('Archives', '/archives.html'),)
         # ('Categories', '/categories.html'),
        # ('Tags', '/tags.html'))

# Social widget
SOCIAL = (('github', 'https://www.github.com/swyoon'),
          ('facebook', 'https://www.facebook.com/sangwoong.yoon.18'))

DEFAULT_PAGINATION = 10

# THEME = "/home/swyoon/pelican-themes/Flex"
THEME = "Flex"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# added by swyoon
MARKUP = ('md', 'ipynb')

# PLUGIN_PATHS = ['/home/swyoon/cloned/pelican-plugins']
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['pelican-ipynb.markup']


GOOGLE_ANALYTICS = 'UA-135002298-1'
DISQUS_SITENAME = 'swyoon'
