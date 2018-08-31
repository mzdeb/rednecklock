#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'mypy==0.620',
]

test_requirements = [
    'flake8==3.5.0',
    'isort==4.3.4',
    'pytest==3.7.4',
    'pytest-cov==2.5.1',
    'tox==3.2.1',
]

dev_requirements = [
    'punch.py==1.5.0',
    'Sphinx==1.7.8',
    'watchdog==0.9.0',
]

setup(
    name='rednecklock',
    version='0.1.0',
    description="Distributed locks with Redis and Python",
    long_description=readme + '\n\n' + history,
    author="Maciej Zdeb",
    author_email='maciej@zdeb.pl',
    url='https://github.com/mzdeb/rednecklock',
    packages=[
        'rednecklock',
    ],
    package_dir={'rednecklock':
                 'rednecklock'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='rednecklock',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    setup_requires=["pytest-runner"],
    test_suite='tests',
    tests_require=test_requirements,
    extras_require={
        'test': test_requirements,
        'dev': dev_requirements,
    },
)
