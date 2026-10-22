# --without-remote-debug

--without-remote-debug

Turn off the remote debugging support detailed in [**PEP 768**](https://peps.python.org/pep-0768/) (on by default). With this flag supplied, the code permitting the interpreter to arrange execution of a Python file inside a separate process, as detailed in [**PEP 768**](https://peps.python.org/pep-0768/), does not get compiled. That covers both the capability to schedule code for execution and the capability to receive code for execution.

 Py_REMOTE_DEBUG

This macro is defined by default, unless Python is configured with `--without-remote-debug`.

Bear in mind that, even with the macro defined, remote debugging might still be unavailable (on an incompatible platform, for instance).

Added in version 3.14.

[Subject index](INDEX.md) · [Previous source section](with-strict-overflow.md) · [Following source section](python-debug-build.md)
