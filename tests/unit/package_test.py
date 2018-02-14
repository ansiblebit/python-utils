# -*- coding: utf-8 -*-
"""Unit tests for the package module."""

import ansiblebit.lib


def test_version():
    """Test version() function."""
    assert ansiblebit.lib.version() == ansiblebit.lib.__version__
