#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Sangwoong Yoon'
SITENAME = "Sangwoong Yoon"
SITEURL = 'https://swyoon.github.io'
# SITEURL = 'http://swyoon.iptime.org:22002'
SITETITLE = AUTHOR
SITESUBTITLE = 'Research Fellow @ University College London'
SITELOGO = SITEURL + '/images/swyoon_profile_josun_crop.jpg'

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
# LINKS = (('Archives', '/archives.html'),)
         # ('Categories', '/categories.html'),
        # ('Tags', '/tags.html'))

# Social widget
SOCIAL = (('github', 'https://www.github.com/swyoon'),
          ('facebook', 'https://www.facebook.com/sangwoong.yoon.18'),
          ('twitter', 'https://twitter.com/WoongSSang'),
          ('linkedin', 'https://www.linkedin.com/in/sangwoong-yoon-8a6944b9/'))

DEFAULT_PAGINATION = 10

# THEME = "/home/swyoon/pelican-themes/Flex"
THEME = "Flex"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# added by swyoon
MARKUP = ('md')

# PLUGIN_PATHS = ['/home/swyoon/cloned/pelican-plugins']
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = []


GOOGLE_ANALYTICS = 'UA-135002298-1'
DISQUS_SITENAME = 'swyoon'

STATIC_PATHS = ['images', 'pdfs', 'extra']

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
}
