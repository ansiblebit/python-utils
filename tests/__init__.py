"""

"""

import os

import logging

import company.package.config
import company.package.logging


LOGGING_CONFIG_FILE = '%s/tests/logging.conf' % os.curdir
PACKAGE_CONFIG_FILE = '%s/tests/package.cfg' % os.curdir


class Basic(object):
    """
    Basic functionality to enhance test cases.
    """

    __slots__ = ('config', 'logger')

    configuration_loaded = False
    logging_loaded = False

    def setup_configuration(self):
        """
        Setup test configuration.
        It will also load (once) the test configuration.

        :param name: the name of the logger.
        :type name: str
        """
        logging.getLogger('%s.%s' % (__name__, 'BaseTestCase')).info('setup_configuration()')

        if not Basic.configuration_loaded:
            company.package.config.load_configuration(PACKAGE_CONFIG_FILE)
            Basic.configuration_loaded = True

        self.configuration = company.package.config.get()

    def setup_logger(self, name):
        """
        Setup test logger.
        It will also load (once) the test logging configuration.

        :param name: the name of the logger.
        :type name: str
        """
        logging.getLogger('%s.%s' % (__name__, 'BaseTestCase')).info('setup_logger()')

        if not Basic.logging_loaded:
            company.package.logging.load_configuration(LOGGING_CONFIG_FILE)
            Basic.logging_loaded = True

        self.logger = logging.getLogger(name)