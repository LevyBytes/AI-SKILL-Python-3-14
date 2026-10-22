# Python 3.12.0 alpha 1 / tests / os

[gh-94315](https://github.com/python/cpython/issues/94315): Rather than leaning on [`os.geteuid()`](https://docs.python.org/3.14/library/os.html#os.geteuid), tests now probe for DAC override capability.

[gh-90473](https://github.com/python/cpython/issues/90473): A `chmod(2)` syscall is absent from WASI. On WASI, [`os.chmod()`](https://docs.python.org/3.14/library/os.html#os.chmod) is therefore a no-op stub. Every test depending on a working `os.chmod()` is skipped.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
