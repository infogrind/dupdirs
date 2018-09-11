import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    description = f.read()

setup(
    name='dupdirs',
    version="0.1",
    author='Marius Kleiner',
    author_email='kleiner@gmail.com',
    url='https://github.com/infogrind/dupdirs',
    description='Script to find duplicate files and directories in two ' +
                'different directories',
    long_description=description,
    packages=find_packages(),
    install_requires=[
        "fuzzywuzzy",
        "python-Levenshtein"
        ],
    entry_points={
        "console_scripts": ["dupdirs = dupdirs.dupdirs:main"]
        },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English'
        ]
    )
