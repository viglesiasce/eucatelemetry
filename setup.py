#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()

requirements = [
    'stevedore',
    'eutester'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='eucatelemetry',
    version='0.1.0',
    description='Monitor you Eucalyptus cloud resources',
    long_description=readme,
    author='Vic Iglesias',
    author_email='viglesiasce@gmail.com',
    url='https://github.com/viglesiasce/eucatelemetry',
    packages=find_packages(),
    package_dir={'eucatelemetry':
                 'eucatelemetry'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='eucatelemetry',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    provides=['eucatelemetry'], 
    entry_points={
        'eucatelemetry': [
            'vm_capacity = eucatelemetry.plugins.eutester.vm_capacity:VMCapacity',
            'resource_count = eucatelemetry.plugins.eutester.resource_count:ResourceCount',
            'api_latency = eucatelemetry.plugins.eutester.api_latency:APILatency'
        ],
    },
    test_suite='tests',
    tests_require=test_requirements
)

