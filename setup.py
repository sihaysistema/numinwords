# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA

import re
from io import open

from setuptools import find_packages, setup

PACKAGE_NAME = "numinwords"

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU Library or Lesser General Public License '
    '(LGPL)',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Topic :: Software Development :: Internationalization',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Software Development :: Localization',
    'Topic :: Text Processing :: Linguistic',
]

LONG_DESC = open('README.rst', 'rt', encoding="utf-8").read() + '\n\n' + \
    open('CHANGES.rst', 'rt', encoding="utf-8").read()


def find_version(fname):
    """Parse file & return version number matching 0.0.1 regex
    Returns str or raises RuntimeError
    """
    version = ''
    with open(fname, 'r', encoding="utf-8") as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError('Cannot find version information')
    return version


setup(
    name=PACKAGE_NAME,
    version=find_version("bin/numinwords"),
    description='Modules to convert numbers to words. Easily extensible.\
                Guatemala test',
    long_description=LONG_DESC,
    license='LGPL',
    author='Taro Ogawa <tso at users sourceforge net>',
    author_email='tos@users.sourceforge.net',
    maintainer='m.m@sihaysistema.com SIHAYSISTEMA',
    maintainer_email='m.m@sihaysistema.com',
    keywords=' number word numbers words convert conversion i18n '
             'localisation localization internationalisation '
             'internationalization',
    url='https://github.com/sihaysistema/numinwords',
    packages=find_packages(exclude=['tests']),
    test_suite='tests',
    classifiers=CLASSIFIERS,
    scripts=['bin/numinwords'],
    install_requires=["docopt>=0.6.2"],
    tests_require=['delegator.py'],
)
