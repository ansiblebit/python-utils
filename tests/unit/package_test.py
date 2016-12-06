# -*- coding: utf-8 -*-
"""Unit tests for the package module."""

import steenzout.primogen


def test_version():
    """Test version() function."""
    assert steenzout.primogen.version() == steenzout.primogen.__version__
