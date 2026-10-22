# Limited C API and Stable ABI

### Limited C API and Stable ABI

As things stand, neither the [Limited C API](https://docs.python.org/3.14/c-api/stable.html#limited-c-api) nor the stable ABI is available in the free-threaded build. Building through [setuptools](https://setuptools.pypa.io/en/latest/setuptools.html) with `py_limited_api=True` already set? Then writing `py_limited_api=not sysconfig.get_config_var("Py_GIL_DISABLED")` lets you bow out of the limited API specifically when the free-threaded build is the target.

Note

Plan on producing dedicated wheels for the free-threaded build apart from the rest. Where you presently lean on the stable ABI, one wheel can still cover a span of non-free-threaded Python releases.

[Subject index](INDEX.md) · [Previous source context](building-extensions-for-the-free-threaded-build.md) · [Following source context](windows.md)
