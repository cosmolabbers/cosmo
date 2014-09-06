#!/usr/bin/env python

from setuptools import setup, find_packages

__version__ = '1.0'

__build__ = ''

setup(name='cosmo',
      version=__version__ + __build__,
      description='cosmo',
      author='Location Labs',
      author_email='info@locationlabs.com',
      url='http://www.locationlabs.com',
      packages=find_packages(exclude=['*.tests']),
      setup_requires=[
          'nose>=1.0',
      ],
      install_requires=[
          'Flask>=0.8',
          'uWSGI>=1.9.20',
      ],
      tests_require=[
      ],
      test_suite='cosmo.tests',
      entry_points={
          'console_scripts': [
              'development = cosmo.development:main',
          ]
      },
      )
