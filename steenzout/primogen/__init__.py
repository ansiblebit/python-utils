# -*- coding: utf-8 -*-
"""
.. module:: steenzout.primogen
    :platform: Unix
    :synopsis: Company primogen.

.. moduleauthor:: Your Name <email address>
"""

from steenzout.primogen.metadata import __version__


def version():
    """
    Return this primogen version.

    :return: primogen version.
    :rtype: str
    """
    return __version__
