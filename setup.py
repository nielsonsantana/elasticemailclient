#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup


setup(
    name='elasticmailclient',
    version='0.1',
    description='ElasticMailClient Python API - https://elasticemail.com/resources/api/integration-libraries/.',
    author='Elastic Email, Inc.',
    author_email='<author email>',
    url='https://github.com/nielsonsantana/elasticmailclient',
    install_requires=['requests'],
    packages=[
        'elasticmailclient',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
