#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup


setup(
    name='elasticemailclient',
    version='0.1',
    description='ElasticEmailClient Python API - https://elasticemail.com/resources/api/integration-libraries/.',
    author='Elastic Email, Inc.',
    author_email='<author email>',
    url='https://github.com/nielsonsantana/elasticemailclient',
    install_requires=['requests'],
    packages=[
        'elasticemailclient',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
