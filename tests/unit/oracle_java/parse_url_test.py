# -*- coding: utf-8 -*-
"""Unit tests for the ansiblebit.lib.oracle_java.parse_url() function."""

from ansiblebit.lib import oracle_java


def test_parse_url_jdk8():
    expected = []
    out = oracle_java.parse_url(oracle_java.URL_JDK_8)

    for expected_download in expected:
        assert expected_download in out


def test_parse_url_jdk9():
    expected = []
    out = oracle_java.parse_url(oracle_java.URL_JDK_9)

    for expected_download in expected:
        assert expected_download in out


def test_parse_url_jre8():
    prefix = 'http://download.oracle.com/otn-pub/java/jdk/8u161-b12/2f38c3b165be4555a1fa6e98c45e0808'
    expected = [
        oracle_java.Download(title='Linux x86',
                             size='63.4 MB',
                             filepath='%s/jre-8u161-linux-i586.rpm' % prefix,
                             md5='b34512f9f0026089707eb9690f2b597b',
                             sha256='8d6fde589042d4a009e5140b0f4e95eb6a4930c6056616becb7edaf46ee05fdc'),
        oracle_java.Download(title='Linux x86', size='79.29 MB',
                             filepath='%s/jre-8u161-linux-i586.tar.gz' % prefix,
                             md5='32db95dd417fd7949922206b2a61aa19',
                             sha256='1ed63892fc48093bf77f9b30cd1bb3ddc8703649e0e8211e1eb970f11746458a'),
        oracle_java.Download(title='Linux x64', size='60.4 MB',
                             filepath='%s/jre-8u161-linux-x64.rpm' % prefix,
                             md5='ea94f2c881e06c01d6ff5255c560416b',
                             sha256='4cdda5b2f40bfff9e0c6dfa145609eeb0596fd584d31a8609bd30ea644b8e309'),
        oracle_java.Download(title='Linux x64', size='76.35 MB',
                             filepath='%s/jre-8u161-linux-x64.tar.gz' % prefix,
                             md5='4385bc121b085862be623f4a31e7e0b4',
                             sha256='f5013ffab71cfb690de18d2b75a2d8c95e87175c888c50042be06b167ea6b4b5'),
        oracle_java.Download(title='macOS', size='74.17 MB',
                             filepath='%s/jre-8u161-macosx-x64.dmg' % prefix,
                             md5='e2524e7c20fecf5533df8307f9b93a42',
                             sha256='7fb418e00edab19e8a25cd1eb480fa7d1f1db55309e52b408503d60ce97e1e94'),
        oracle_java.Download(title='macOS', size='65.86 MB',
                             filepath='%s/jre-8u161-macosx-x64.tar.gz' % prefix,
                             md5='87170bc5c018ba34f1b0f4a9e98531cd',
                             sha256='611ac48ca3db2f143c7a565bd8139bce43ad8f5262555fed542394d127cd14fb'),
        oracle_java.Download(title='Solaris SPARC 64-bit',
                             size='52.24 MB',
                             filepath='%s/jre-8u161-solaris-sparcv9.tar.gz' % prefix,
                             md5='d72900f0a2be61076ac446c3eac33f7d',
                             sha256='aa3dd4b687d2ce4d7e850bdc247489c524355e1de2fba2b9769266022c05a39d'),
        oracle_java.Download(title='Solaris x64', size='50 MB',
                             filepath='%s/jre-8u161-solaris-x64.tar.gz' % prefix,
                             md5='5f81bfd341eb8691f4253d5f398d2ce5',
                             sha256='903878c6599efcf8cd816411a002d9db101b4f9dae177141ab1fae083d40f4e7'),
        oracle_java.Download(title='Windows x86 Online',
                             size='1.78 MB',
                             filepath='%s/jre-8u161-windows-i586-iftw.exe' % prefix,
                             md5='7e890f27d14d1e695b00a933e5a34326',
                             sha256='4232f5ab8a358e7aa7b86346b467fca066dff8ea4459e6e08a5ea4790cc41b23'),
        oracle_java.Download(title='Windows x86 Offline',
                             size='61.35 MB',
                             filepath='%s/jre-8u161-windows-i586.exe' % prefix,
                             md5='e125b34bc81953139e397b598eda2587',
                             sha256='9d4ab1c5eff210fd165a1aca33734da82c6bac9437bd8f20637e68460f3e9008'),
        oracle_java.Download(title='Windows x86',
                             size='64.56 MB',
                             filepath='%s/jre-8u161-windows-i586.tar.gz' % prefix,
                             md5='33ef9c03a22a0d0485e66c1b05f776e6',
                             sha256='e3b804bfb7c57972620c8e59780919b8df2b6e8d05bafa6d0dee848cf6c25017'),
        oracle_java.Download(title='Windows x64 Offline',
                             size='68.02 MB',
                             filepath='%s/jre-8u161-windows-x64.exe' % prefix,
                             md5='f728297a275699b9151d07d768de7bac',
                             sha256='59c02eb80acfaeeaf3728c3841440c68ea9e3b4d5e735a7a863f6e2492760b5d'),
        oracle_java.Download(title='Windows x64', size='68.58 MB',
                             filepath='%s/jre-8u161-windows-x64.tar.gz' % prefix,
                             md5='404c148a2d509ff5271222aeac882e8a',
                             sha256='929a7cc795cffb3304271be9ffcb43f08c2c1cc077dee67f8487649661ee30d0')
    ]
    out = oracle_java.parse_url(oracle_java.URL_JRE_8)

    for expected_download in expected:
        assert expected_download in out


def test_parse_url_jre9():
    expected = []
    out = oracle_java.parse_url(oracle_java.URL_JRE_9)

    for expected_download in expected:
        assert expected_download in out
