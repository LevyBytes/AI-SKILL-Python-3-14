# What's New In Python 3.7 / Platform Support Removals

### Platform Support Removals

- Official support no longer extends to FreeBSD 9 and earlier.

- To get complete Unicode coverage, extension modules included, *nix platforms must now supply at minimum one among `C.UTF-8` (full locale), `C.utf8` (full locale) or `UTF-8` (`LC_CTYPE`-only locale), serving as a substitute for the legacy `ASCII`-based `C` locale.

- Support for OpenSSL 0.9.8 and 1.0.1 has ended, so compiling CPython 3.7 with SSL/TLS capability on older systems that continue to rely on these releases calls for custom build options linking against a newer OpenSSL build.

In particular, this matter touches those LTS Linux distributions Debian 8 (aka "jessie") together with Ubuntu 14.04 (aka "Trusty"), since they continue to default to OpenSSL 1.0.1.

Debian 9 ("stretch") and Ubuntu 16.04 ("xenial"), alongside fresh editions among further LTS Linux releases — for example RHEL/CentOS 7.5 and SLES 12-SP3 — ship OpenSSL 1.0.2 or newer, so they keep working under the default build configuration.

A worked illustration of leveraging the SSL [compatibility testing infrastructure](https://github.com/python/cpython/tree/3.14/Tools/ssl/multissltests.py) inside CPython's test suite to compile and link against OpenSSL 1.1.0 rather than the operating system's outdated OpenSSL appears in CPython's own [CI configuration file](https://github.com/python/cpython/blob/v3.7.13/.travis.yml).

[Subject index](INDEX.md) · [Previous source section](deprecated-functions-and-types-of-the-c-api.md) · [Next source section](api-and-feature-removals.md) · [Release/subject declaration](summary-release-highlights.md)
