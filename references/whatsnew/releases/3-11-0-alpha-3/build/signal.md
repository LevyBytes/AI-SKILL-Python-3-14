# Python 3.11.0 alpha 3 / build / signal

[bpo-41498](https://bugs.python.org/issue?@action=redirect&bpo=41498): Python now builds on platforms lacking `sigset_t`. When `sigset_t` is absent, a handful of functions in [`signal`](https://docs.python.org/3.14/library/signal.html#module-signal) become unavailable.

This builds on a patch from Roman Yurchak for pyodide.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
