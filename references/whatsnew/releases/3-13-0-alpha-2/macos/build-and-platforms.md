# Python 3.13.0 alpha 2 / macos / build and platforms

[gh-59703](https://github.com/python/cpython/issues/59703): On macOS framework builds, have `getpath.c` rely on the system `dladdr` function to locate the shared library, instead of leaning on deprecated macOS APIs.

[gh-110950](https://github.com/python/cpython/issues/110950): Refresh the macOS installer with an upstream Tcl/Tk fix addressing the `Secure coding is not enabled for restorable state!` warning that Tkinter ran into on macOS 14 Sonoma.

[gh-111015](https://github.com/python/cpython/issues/111015): Make certain that IDLE.app and Python Launcher.app receive suitable permissions when installed on macOS builds.

[gh-71383](https://github.com/python/cpython/issues/71383): Refresh the macOS installer with an upstream Tcl/Tk fix for the `ttk::ThemeChanged` error that Tkinter hit.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
