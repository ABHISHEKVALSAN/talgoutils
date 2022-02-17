'''
Setup file for talgoutils library
'''
from setuptools import setup, find_packages

setup(
    name                =    'talgoutils',
    version             =    '1.0',
    url = '',
    author = 'Abhishek Valsan',
    author_email = 'talgo.abhishekvalsan@gmail.com',
    license = 'Talgo',
    packages            =    find_packages(),
    package_dir         =    {'talgoutils':'talgoutils'},
    install_requires    =    ['numpy', 'pandas'],
    zip_safe            =    False
)
