# Python 3.7.0 alpha 1 / library / sysconfig

[bpo-29585](https://bugs.python.org/issue?@action=redirect&bpo=29585): Skip importing `sysconfig` from within `site` to speed up startup. Python startup runs roughly 5% faster on Linux and 30% faster on macOS.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
