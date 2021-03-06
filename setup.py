# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os
import re


NAME = 'schemapy'
KEYWORDS = 'schema api database'
DESC = 'Centralize database access'
URL = 'https://github.com/link-society/schemapy'
AUTHOR = 'Link Society'
AUTHOR_EMAIL = 'contact@link-society.com'
LICENSE = 'Apache'
REQUIREMENTS = [
    'pyDAL>=17.11',
    'addict>=2.1.2',
    'pytest-runner>=3.0'
]
TESTS_REQUIREMENTS = [
    'pytest>=3.4.0',
    'python-decouple>=3.1'
]

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: Implementation :: CPython'
]


def get_cwd():
    return os.path.dirname(os.path.abspath(os.path.expanduser(__file__)))


def get_version(default='0.1'):
    _name = NAME.replace('.', os.sep)
    path = os.path.join(get_cwd(), _name, '__init__.py')

    with open(path) as f:
        stream = f.read()
        regex = re.compile(r'.*__version__ = \'(.*?)\'', re.S)
        version = regex.match(stream)

        if version is None:
            version = default

        else:
            version = version.group(1)

    return version


def get_long_description():
    path = os.path.join(get_cwd(), 'README.rst')
    desc = None

    if os.path.exists(path):
        with open(path) as f:
            desc = f.read()

    return desc


def get_test_suite():
    return 'tests'


setup(
    name=NAME,
    keywords=KEYWORDS,
    version=get_version(),
    url=URL,
    description=DESC,
    long_description=get_long_description(),
    license=LICENSE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    test_suite=get_test_suite(),
    tests_require=TESTS_REQUIREMENTS,
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
)
