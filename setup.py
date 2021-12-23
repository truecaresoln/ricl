# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ricl/__init__.py
from ricl import __version__ as version

setup(
	name="ricl",
	version=version,
	description="Certificate Agency",
	author="RICL",
	author_email="erp@ricliso.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
