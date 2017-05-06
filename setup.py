"""Setup for git_learn."""

from setuptools import setup

setup(
    name='git_learn',
    version='0.1.0',
    packages=['githi'],
    entry_points={
        'console_scripts': [
            'howdy = githi.git_learn:main'
        ]
    })
