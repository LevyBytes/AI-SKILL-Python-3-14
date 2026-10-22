# Python 3.6.2 release candidate 1 / windows / build and platforms

[bpo-30687](https://bugs.python.org/issue?@action=redirect&bpo=30687): While building on Windows, find msbuild.exe rather than vcvarsall.bat

[bpo-30450](https://bugs.python.org/issue?@action=redirect&bpo=30450): On Windows the build process no longer relies on Subversion; it instead fetches external code from GitHub through a Python script. Should Python 3.6 be absent from the system (checked via `py -3.6`), NuGet pulls down a copy of 32-bit Python.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
