# PYTHON_GIL

PYTHON_GIL

Setting this variable to `1` compels the global interpreter lock (GIL) to stay enabled, while `0` compels the GIL to remain disabled (this requires a Python built with the [`--disable-gil`](https://docs.python.org/3.14/using/configure.html#cmdoption-disable-gil) build option).

Consult as well the `-X gil` command-line option — it overrides this variable — together with [Free-threaded CPython](https://docs.python.org/3.14/whatsnew/3.13.html#whatsnew313-free-threaded-cpython).

Added in version 3.13.

[Subject index](INDEX.md) · [Previous source section](python-history.md) · [Following source section](python-thread-inherit-context.md)
