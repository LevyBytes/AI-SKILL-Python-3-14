# Python 3.7.0 beta 3 / macos / build and platforms

[bpo-32726](https://bugs.python.org/issue?@action=redirect&bpo=32726): Compile and link against a private copy of Tcl/Tk 8.6 for the installer targeting macOS 10.6+. The 10.9+ installer flavor was already doing this. As a result, the Python 3.7 shipped by the python.org macOS installers no longer requires or relies on any outside builds of Tcl/Tk, whether supplied by the system or installed by the user, including ActiveTcl.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
