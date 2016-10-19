# -*- coding: utf-8 -*-
"""
.. module:: steenzout.primogen.tests
    :platform: Unix
    :synopsis:

.. moduleauthor:: Your Name <email address>
"""

import os

import steenzout.primogen.config
import steenzout.primogen.logging

import logging

import unittest


LOGGING_CONFIG_FILE = '%s/tests/logging.conf' % os.curdir
PACKAGE_CONFIG_FILE = '%s/tests/primogen.cfg' % os.curdir


class Basic(object):
    """
    Basic functionality to enhance test cases.
    """

    def setup_configuration(self):
        """
        Setup test configuration.
        It will also load (once) the test configuration.
        """
        logging.getLogger('%s.%s' % (__name__, 'Basic')).info('setup_configuration()')

        steenzout.primogen.config.reset()
        steenzout.primogen.config.load_configuration(PACKAGE_CONFIG_FILE)

        self.configuration = steenzout.primogen.config.get()

    def setup_logger(self):
        """
        Setup test logger.
        It will also load (once) the test logging configuration.
        """
        logging.getLogger('%s.%s' % (__name__, 'Basic')).info('setup_logger()')

        steenzout.primogen.logging.load_configuration(LOGGING_CONFIG_FILE)

        self.logger = logging.getLogger('%s.%s' % (__name__, self.__class__.__name__))


class BaseTestCase(unittest.TestCase, Basic):
    """
    Base test case.
    """

    __slots__ = ('configuration', 'logger')

    def __init__(self, methodName):
        """
        Initializes a BaseTestCase instance.

        :param methodName: the test method to be executed.
        :type methodName: str
        """
        super(BaseTestCase, self).__init__(methodName)

        self.setup_logger()
        self.setup_configuration()

    def setUp(self):
        """
        Setup test resources.
        """
        self.logger.info('setUp()')

    def tearDown(self):
        """
        Tear down test resources.
        """
        self.logger.info('tearDown()')
