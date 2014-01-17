#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from distutils.core import setup
import glob

setup(
	name='tuuliviiri',
	version='1.0',
	description='',
	author='Teemu Puukko',
	author_email='teemuki@gmail.com',
	packages=[''],
	license='LICENSE.txt',
	long_description=open('README.txt').read(),
	install_requires=[],
	keywords=[],
	scripts=glob.glob('bin/*.py')
)
