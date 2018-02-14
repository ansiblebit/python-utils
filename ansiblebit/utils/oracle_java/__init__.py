# -*- coding: utf-8 -*-
#
# Copyright 2018 ansiblebit
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""Python support module for ansiblebit.oracle-java Ansible role."""


from .download import Download


ARCH_ARM32 = 'arm32-vfp-hflt'
# (str): name used for the ARM 32 Hard Float ABI architecture.
ARCH_ARM64 = 'arm64-vfp-hflt'
# (str): name used for the ARM 64 Hard Float ABI architecture.
ARCH_I586 = 'i586'
# (str): name used for the x86 architecture.
ARCH_X64 = 'x64'
# (str): name used for the x86_64 architecture.
ARCH_SPARC = 'sparcv9'
# (str): name used for the Sparc V9 architecture.

OS_LINUX = 'linux'
# (str): name used for the Linux operating system.
OS_MACOSX = 'macosx'
# (str): name used, in Java 8, for the OSX operating system.
OS_OSX = 'osx'
# (str): name used, in Java 9, for the OSX operating system.
OS_SOLARIS = 'solaris'
# (str): name used for the Solaris operating system.
OS_WINDOWS = 'windows'
# (str): name used for the Windows operating system.

URL_JDK_8 = 'http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html'
# (str): URL where the user can download the Oracle Java 9 SDK.
URL_JDK_9 = 'http://www.oracle.com/technetwork/java/javase/downloads/jdk9-downloads-3848520.html',
# (str): URL where the user can download the Oracle Java 8 SDK.
URL_JRE_8 = 'http://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html'
# (str): URL where the user can download the Oracle Java 8 Runtime Environment.
URL_JRE_9 = 'http://www.oracle.com/technetwork/java/javase/downloads/jre9-downloads-3848532.html',
# (str): URL where the user can download the Oracle Java 9 Runtime Environment.


def get_download_link(version=9, update=None, os=OS_LINUX, arch=ARCH_X64):
    """Returns the Oracle Java download link.

    Args:
        version (int): Java version.
        update (int): update number.
        os (str): name of the operating system.
        arch (str): name of the architecture.

    Returns:
        (str): URL where target can be download; None if target is not found.
    """
    return None


def get_download_links(version=9, update=None):
    """Returns all download links from the Oracle Java download link.

    Args:
        version (int): Java version.
        update (int): update number.

    Returns:
        (list[str]): list of URLs where targets can be downloaded; empty list if no target can be found.
    """
    return None


def parse_page(html, version=9):
    """Returns the download targets present in the given HTML document.

    Args:
        html (str): HTML document to be parsed.
        version (int): Java version.

    Returns:
        (generator[Download]): the download targets present in the given URL.
    """
    for line in html:
        continue


def parse_url(url, version=9):
    """Returns the download targets present in the given URL.

    Args:
        url (str): download URL to be parsed.
        version (int): Java version.

    Returns:
        (generator[Download]): the download targets present in the given URL.
    """
    # download document
    doc = '<html></html>'

    # parse page
    return parse_page(doc, version=version)

