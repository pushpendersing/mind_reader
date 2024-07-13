from setuptools import setup
import random
import os
import pyttsx3

VERSION = "0.0.1"
DESCRIPTION ="mind reading by the computer"
LONG_DESCRIPTION = "A mind_reader program"

setup(
    name='mind_reader',
    version='1.0', 
    description='A module to play a mind reading game using Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='chinki5177',
    author_email='pushpendersingh046@email.com',
    url='https://github.com/pushpendersing/mind_reader',
    packages=['mind_reader'],
    install_requires=[
        'pyttsx3',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)