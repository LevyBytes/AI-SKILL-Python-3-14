# Python 3.5.0 alpha 1 / build / build and platforms

[bpo-20644](https://bugs.python.org/issue?@action=redirect&bpo=20644): Added OS X installer support for the documentation build adjustments in 3.4.1, which assume an externally provided sphinx-build sits at /usr/bin.

[bpo-15968](https://bugs.python.org/issue?@action=redirect&bpo=15968): Folded the Tcl, Tk, and Tix builds into the Windows build solution.

[bpo-22919](https://bugs.python.org/issue?@action=redirect&bpo=22919): The Windows build now targets VC 14.0 (Visual Studio 2015), which will serve as the toolchain for the official release.

[bpo-21236](https://bugs.python.org/issue?@action=redirect&bpo=21236): Build _msi.pyd against cabinet.lib rather than fci.lib

[bpo-17128](https://bugs.python.org/issue?@action=redirect&bpo=17128): Ship a private build of OpenSSL with the OS X 10.5+ installer.

[bpo-15506](https://bugs.python.org/issue?@action=redirect&bpo=15506): Within the configure script, use the standard PKG_PROG_PKG_CONFIG autoconf macro.

[bpo-21141](https://bugs.python.org/issue?@action=redirect&bpo=21141): The Windows build process has stopped trying to locate Perl, depending instead on OpenSSL source already being configured and prepared to build. The `PCbuild\build_ssl.py` script was rewritten and renamed into `PCbuild\prepare_ssl.py`; it manages configuring the OpenSSL source for both the 32 and 64 bit platforms. OpenSSL sources fetched from svn.python.org will always arrive pre-configured and ready for building.

[bpo-21037](https://bugs.python.org/issue?@action=redirect&bpo=21037): Provide a build option that turns on AddressSanitizer support.

[bpo-19962](https://bugs.python.org/issue?@action=redirect&bpo=19962): At the root of the source tree, the Windows build process now produces “python.bat”, forwarding every argument along to the interpreter built most recently.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
