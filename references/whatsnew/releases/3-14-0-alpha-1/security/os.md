# Python 3.14.0 alpha 1 / security / os

[gh-118773](https://github.com/python/cpython/issues/118773): Repairs ACL creation in [`os.mkdir()`](https://docs.python.org/3.14/library/os.html#os.mkdir) on Windows so it behaves correctly on non-English machines.

[gh-118486](https://github.com/python/cpython/issues/118486): [`os.mkdir()`](https://docs.python.org/3.14/library/os.html#os.mkdir) under Windows now honors a *mode* of `0o700` to confine the freshly created directory to the current user. That addresses [**CVE 2024-4030**](https://www.cve.org/CVERecord?id=CVE-2024-4030) impacting [`tempfile.mkdtemp()`](https://docs.python.org/3.14/library/tempfile.html#tempfile.mkdtemp) whenever the base temporary directory grants more permissions than the default.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
