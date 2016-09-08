# -*- coding: utf-8 -*-

import unittest


class VersionTestCase(unittest.TestCase):
    """
    Test case for the version module.
    """

    def test_attributes(self):
        """
        Tests the version module attributes.
        """
        import company.package

        self.assertTrue(
            company.package.version() == company.package.__version__
        )
