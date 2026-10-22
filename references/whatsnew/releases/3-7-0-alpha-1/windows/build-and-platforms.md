# Python 3.7.0 alpha 1 / windows / build and platforms

[bpo-31392](https://bugs.python.org/issue?@action=redirect&bpo=31392): Move the Windows build onto OpenSSL 1.1.0f

[bpo-30581](https://bugs.python.org/issue?@action=redirect&bpo=30581): On Windows, os.cpu_count() now reports the right processor count even when there are more than 64 logical processors.

[bpo-30916](https://bugs.python.org/issue?@action=redirect&bpo=30916): Compile OpenSSL, Tcl and Tk ahead of time and ship those binaries within the build.

[bpo-30450](https://bugs.python.org/issue?@action=redirect&bpo=30450): The Windows build process no longer leans on Subversion; it instead pulls external code from GitHub by way of a Python script. When Python 3.6 cannot be located on the machine (through `py -3.6`), NuGet fetches a copy of 32-bit Python.

[bpo-28251](https://bugs.python.org/issue?@action=redirect&bpo=28251): Better help manuals for Windows.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
