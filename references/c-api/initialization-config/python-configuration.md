# Python Configuration

### Python Configuration

The `PyPreConfig_InitPythonConfig()` and `PyConfig_InitPythonConfig()` functions produce a configuration for assembling a tailored Python that still acts like the ordinary Python.

Environment variables and command line arguments do the configuring here, while global configuration variables are left out.

This function switches on C locale coercion ([**PEP 538**](https://peps.python.org/pep-0538/)) along with [Python UTF-8 Mode](https://docs.python.org/3.14/library/os.html#utf8-mode) ([**PEP 540**](https://peps.python.org/pep-0540/)), contingent on the LC_CTYPE locale plus the [`PYTHONUTF8`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONUTF8) and [`PYTHONCOERCECLOCALE`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONCOERCECLOCALE) environment variables.

[Subject index](INDEX.md) · [Previous source contract](isolated-configuration.md) · [Following source contract](pyconfig-home-to-pyconfig-executable.md)
