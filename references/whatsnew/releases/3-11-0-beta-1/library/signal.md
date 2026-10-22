# Python 3.11.0 beta 1 / library / signal

[gh-64783](https://github.com/python/cpython/issues/64783): Correct the [`signal.NSIG`](https://docs.python.org/3.14/library/signal.html#signal.NSIG) value on FreeBSD so that signal numbers above 32, such as `signal.SIGRTMIN` and `signal.SIGRTMAX`, are accepted. Victor Stinner authored the patch.

[gh-90623](https://github.com/python/cpython/issues/90623): [`signal.raise_signal()`](https://docs.python.org/3.14/library/signal.html#signal.raise_signal) together with [`os.kill()`](https://docs.python.org/3.14/library/os.html#os.kill) now check right away for any pending signals. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
