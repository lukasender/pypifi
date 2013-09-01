#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

import os

NAME = 'pypifi'
PATH = ['pypifi'] + ['version.txt']
VERSION = open(os.path.join(*PATH)).read().strip()

CLASSIFIERS = """
Programming Language :: Python
Topic :: Software Development
"""[1:-1]

long_description = open('README.md').read()

setup(
  name             = NAME,
  version          = VERSION,
  description      = 'Pipes and Filters implemented in Python',
  long_description = long_description,
  author           = 'Lukas Ender',
  author_email     = 'developer@lukasender.at',
  url              = 'https://github.com/lumannnn/pypifi',
  license          = 'GNU GPL v3',
  keywords         = 'pipe filter pipes filters',
  platforms        = 'any',
  zip_safe         = False,
  classifiers      = CLASSIFIERS.splitlines(),
  package_dir      = {'':'pypifi'},
  packages         = find_packages('pypifi')
)
