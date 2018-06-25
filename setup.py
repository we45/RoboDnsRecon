from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='RoboDnsRecon',
    version='1.0',
    packages=[''],
    package_dir={'': 'robodnsrecon'},
    url='https://github.com/we45/RoboDnsRecon',
    license='MIT',
    author='we45',
    author_email='info@we45.com',
    description='Robot Framework Library for DNS Recon' ,
    install_requires=[
        'docker',
        'robotframework==3.0.4'
    ],
    long_description = long_description,
    long_description_content_type='text/markdown'
)
