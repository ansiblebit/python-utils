# -*- coding: utf-8 -*-
"""Unit tests for the metadata module."""

from steenzout.primogen import metadata


def test_attributes():
    """
    Tests the version module attributes.
    """
    metadata_dir = dir(metadata)

    assert '__version__' in metadata_dir
