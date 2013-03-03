# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

f = open('README', 'r')
try:
    long_desc = f.read()
finally:
    f.close()
    
requires = ['Sphinx>=0.6']

setup(
    name='sphinxcontrib-smblink',
    version='0.1',
    url='https://github.com/goingmywaynet/sphinxcontrib-smblink.git',
    download_url='https://github.com/goingmywaynet/sphinxcontrib-smblink.git',
    license='BSD',
    author='Joey Chen',
    author_email='joey-tech@goingmyway.net',
    description='Sphinx Windows Share Links (WSL) role extension',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
