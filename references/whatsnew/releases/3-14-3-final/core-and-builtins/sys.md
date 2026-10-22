# Python 3.14.3 final / core and builtins / sys

[gh-143135](https://github.com/python/cpython/issues/143135): When [`PYTHONINSPECT`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONINSPECT) holds `0`, set [`sys.flags.inspect`](https://docs.python.org/3.14/library/sys.html#sys.flags.inspect) to `1`. Earlier it was left at `0` for that scenario.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
