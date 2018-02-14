# -*- coding: utf-8 -*-
"""Unit tests for ansiblebit.lib.oracle_java package."""

from ansiblebit.lib import oracle_java


def test_parse_url_jdk8():
    expected = []
    out = oracle_java.parse_url(oracle_java.URL_JDK_8)


def test_parse_url_jdk9():
    expected = []
    out = oracle_java.parse_url(oracle_java.URL_JDK_9)


def test_parse_url_jre8():
    expected = []
    out = oracle_java.parse_url(oracle_java.URL_JRE_8)


def test_parse_url_jre9():
    expected = []
    out = oracle_java.parse_url(oracle_java.URL_JRE_9)
