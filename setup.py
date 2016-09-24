#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pip.download

from pip.req import parse_requirements

from setuptools import find_packages, setup

exec(open('company/package/version.py').read())


def requirements(requirements_file):
    """Return package mentioned in the given file.

    Args:
        requirements_file (str): path to the requirements file to be parsed.

    Returns:
        (list): 3rd-party package dependencies contained in the file.
    """
    return [
        str(pkg.req) for pkg in parse_requirements(
            requirements_file, session=pip.download.PipSession())]


setup(name='primogen',
      version=__version__,
      description='Python basic package.',
      author='Pedro Salgado',
      author_email='steenzout@ymail.com',
      maintainer='Pedro Salgado',
      maintainer_email='steenzout@ymail.com',
      url='https://github.com/steenzout/python-package',
      namespace_packages=('company',),
      packages=find_packages(exclude=('*.tests', '*.tests.*', 'tests.*', 'tests')),
      install_requires=requirements('requirements.txt'),
      tests_require=requirements('requirements-test.txt'))
