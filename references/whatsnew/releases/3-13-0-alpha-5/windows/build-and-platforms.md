# Python 3.13.0 alpha 5 / windows / build and platforms

[gh-115582](https://github.com/python/cpython/issues/115582): With a standard install, building extensions for free-threaded CPython builds now demands compiling with `/DPy_GIL_DISABLED` by hand. Later releases are expected to alter this.

[gh-115554](https://github.com/python/cpython/issues/115554): When updating the [Python install manager](https://docs.python.org/3.14/using/windows.html#launcher), the installer now enforces tighter rules. Most people keep just one launcher and will notice nothing different. If several launchers are present, installing the launcher stays disabled until only one remains. Downgrading it ? something never permitted ? is now blocked far more visibly.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
