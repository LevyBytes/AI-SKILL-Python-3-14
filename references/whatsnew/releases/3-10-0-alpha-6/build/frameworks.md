# Python 3.10.0 alpha 6 / build / frameworks

[bpo-42603](https://bugs.python.org/issue?@action=redirect&bpo=42603): The configure script now relies on pkg-config to locate Tcl/Tk headers and libraries when building tkinter.

On macOS, a Tcl/Tk setup discovered via pkg-config takes precedence over Tcl/Tk frameworks placed under `/{System/,}Library/Frameworks`. Should both be present and you want the framework version instead, you must spell out the relevant `--with-tcltk-*` configuration options yourself.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
