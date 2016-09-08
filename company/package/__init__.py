# -*- coding: utf-8 -*-
"""
.. module:: company.package
    :platform: Unix
    :synopsis: Company package.

.. moduleauthor:: Your Name <email address>
"""

from company.package.version import __version__


def version():
    """
    Return this package version.

    :return: package version.
    :rtype: str
    """
    return __version__
