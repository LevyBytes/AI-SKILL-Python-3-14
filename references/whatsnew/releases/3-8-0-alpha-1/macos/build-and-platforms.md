# Python 3.8.0 alpha 1 / macos / build and platforms

[bpo-35401](https://bugs.python.org/issue?@action=redirect&bpo=35401): Refresh the macOS installer to use OpenSSL 1.1.0j.

[bpo-35025](https://bugs.python.org/issue?@action=redirect&bpo=35025): Properly fence off the usage of the `CLOCK_GETTIME` and related macros within `timemodule` under macOS.

[bpo-34405](https://bugs.python.org/issue?@action=redirect&bpo=34405): Move up to OpenSSL 1.1.0i for the macOS installer builds.

[bpo-33184](https://bugs.python.org/issue?@action=redirect&bpo=33184): Refresh the macOS installer build so it uses OpenSSL 1.1.0h.

[bpo-32726](https://bugs.python.org/issue?@action=redirect&bpo=32726): Compile and link against a private copy of Tcl/Tk 8.6 for the macOS 10.6+ installer. The 10.9+ installer variant does this already. Consequently the Python 3.7 shipped by the python.org macOS installers no longer requires nor uses any outside versions of Tcl/Tk, whether system-supplied or user-installed, such as ActiveTcl.

[bpo-32901](https://bugs.python.org/issue?@action=redirect&bpo=32901): Refresh the macOS 10.9+ installer to Tcl/Tk 8.6.8.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
