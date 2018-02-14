# -*- coding: utf-8 -*-
"""Unit tests for the package module."""

import ansiblebit.utils


def test_version():
    """Test version() function."""
    assert ansiblebit.utils.version() == ansiblebit.utils.__version__
