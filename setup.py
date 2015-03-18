# coding=utf-8
import os
import sys
from setuptools import setup

import tabelafipe


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]
if sys.argv[1] == 'develop':
    REQUIREMENTS += [i.strip()
                     for i in open("requirements_dev.txt").readlines()]


setup(
    name="tabelafipe",
    version=tabelafipe.__version__,
    author=tabelafipe.__author__,
    author_email=tabelafipe.__email__,
    description=tabelafipe.__description__,
    license=tabelafipe.__license__,
    keywords="tabelafipe",
    url="https://github.com/ervilis/tabelafipe-sdk",
    packages=['tabelafipe', 'tests'],
    namespace_packages=['tabelafipe'],
    package_dir={'tabelafipe': 'tabelafipe'},
    install_requires=REQUIREMENTS,
    download_url="https://github.com/ervilis/tabelafipe-sdk/tarball/master",
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Topic :: Utilities",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
