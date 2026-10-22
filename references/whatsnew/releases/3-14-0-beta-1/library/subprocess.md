# Python 3.14.0 beta 1 / library / subprocess

[gh-133089](https://github.com/python/cpython/issues/133089): Report the original timeout value in [`subprocess.TimeoutExpired`](https://docs.python.org/3.14/library/subprocess.html#subprocess.TimeoutExpired) whenever [`subprocess.run()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.run) is invoked with a timeout, rather than the occasionally puzzling leftover remaining-time figure that is computed internally for the closing `wait()`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
