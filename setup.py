# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
# requirements.txt must be included in MANIFEST.in and include_package_data must be True
# in order for this to work; ensures that tox can use the setup to enforce requirements
REQUIREMENTS = '\n'.join(open(os.path.join(os.path.dirname(__file__), 'requirements.txt')).readlines())  # noqa

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="django-basecrm",
    version="0.4.0-dev",
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    include_package_data=True,
    description='A Django app that connects to the BaseCRM API (v2)',
    long_description=README,
    url='https://github.com/yunojuno/django-basecrm',
    author='Marcel Kornblum',
    author_email='marcel@yunojuno.com',
    maintainer='Hugo Rodger-Brown',
    maintainer_email='hugo@yunojuno.com',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
