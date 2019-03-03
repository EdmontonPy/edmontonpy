#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from os.path import dirname, join

from setuptools import find_packages, setup

tests_require = [
    'coverage>=4.5.1, < 5.0',
    'flake8>=3.5.0, < 4.0',
    'pycodestyle>=2.3.1',
    'pyflakes>=1.6.0',
    'tblib>=1.3.2, < 2.0',
]

setup(
    name='edmontonpy',
    version='0.0.1',
    description='Website for the Edmonton Python meetup',
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
        'django>=2.1.2',
        'psycopg2>=2.7.6.1',
    ],
    test_suite="edmontonpy.test_runners.test_suite",
    tests_require=tests_require,
    extras_require={
        'dev': tests_require,
    },
)
