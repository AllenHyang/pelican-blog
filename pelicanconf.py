#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Allen'
SITENAME = u"Allen's blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = u'Asia/Shanghai'

DEFAULT_LANG = u'zh'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#FEED_ALL_RSS = 'feeds/all.rss.xml'
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
)
# Social widget
SOCIAL = (('My sina weibo', 'http://weibo.com/u/1644145160'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = 'themes/new-bootstrap2'
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 50
PLUGIN_PATHS=["plugins"]
PLUGINS = ["render_math"]
DUOSHUO_SITENAME = "Allen's blog"
