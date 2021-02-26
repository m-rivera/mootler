#!/usr/bin/env python

from setuptools import setup, Extension

setup(name='mootler',
      version='0.1',
      description='Utility to analyse Moodle data and plot it',
      author='Miguel Rivera',
      author_email='miguel.rivera@ucl.ac.uk',
      license='MIT',
      packages=['mootler',],
      scripts=['mootler/scripts/mootler.py'],
      install_requires=[
          'pandas',
          'plotly',],
      )
