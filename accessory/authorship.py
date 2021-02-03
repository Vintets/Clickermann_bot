#!/usr/bin/env python
# -*- coding: utf-8 -*-


# __author__ = u'master by Vint'
# __title__ = u'--- TeplonetNew ---'
# __version__ = u'0.0.1'
# __build__ = 0x000000
# __copyright__ = u'Copyright 2017 (c)  bitbucket.org/Vintets'
# __license__ = ''
# authorship.authorship(__author__, __title__, __version__, __copyright__)

def authorship(author, title, version, copyright_, width=80):
    copyright_ = copyright_.center(width, ' ')
    version = ('version %s %s' % (version, author)).center(width, ' ')
    name_product = title.center(width, ' ')
    print('{0}{1}{2}{0}'.format('*'*width, copyright_, version))
    print('{0}\n'.format(name_product))

