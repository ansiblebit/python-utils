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
        import steenzout.primogen

        self.assertTrue(
            steenzout.primogen.version() == steenzout.primogen.__version__
        )
