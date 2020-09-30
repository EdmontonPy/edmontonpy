#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from os.path import dirname, join

from setuptools import find_packages, setup

tests_require = [
    'coverage>=4.5.4, < 5.0',
    'flake8>=3.7.8, < 4.0',
    'pycodestyle>=2.5.0',
    'pyflakes>=2.1.1',
    'tblib>=1.4.0, < 2.0',
]

setup(
    name='edmontonpy',
    version='0.0.1',
    description='Website is for the Edmonton Python meetup',
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    author='Andrew Crouse',
    author_email='amcrouse@data-get.org',
    url='https://github.com/EdmontonPy/edmontonpy',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # See: http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords=[
        'edmontonpy',
    ],
    scripts=[
        'manage.py',
    ],
    install_requires=[
        'django>=2.2.4',
        'psycopg2-binary>=2.8.3',
    ],
    test_suite="edmontonpy.test_runners.test_suite",
    tests_require=tests_require,
    extras_require={
        'dev': tests_require,
    },
)
