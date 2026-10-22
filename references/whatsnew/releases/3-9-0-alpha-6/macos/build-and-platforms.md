# Python 3.9.0 alpha 6 / macos / build and platforms

[bpo-38329](https://bugs.python.org/issue?@action=redirect&bpo=38329): For 3.9 installs, python.org's macOS installers now refresh the Current version symlink under /Library/Frameworks/Python.framework/Versions. Up to now, Current was refreshed solely for Python 2.x installs. This ought to make embedding Python 3 inside other macOS applications simpler.

[bpo-40164](https://bugs.python.org/issue?@action=redirect&bpo=40164): Move the macOS installer builds onto OpenSSL 1.1.1g.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
