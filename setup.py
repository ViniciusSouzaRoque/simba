from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in simba_app/__init__.py
from simba_app import __version__ as version

setup(
	name="simba_app",
	version=version,
	description="Day off system",
	author="Vinicius Roque",
	author_email="vinicius.roque@simbioseventures.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
