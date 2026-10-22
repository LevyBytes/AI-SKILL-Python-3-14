# Python 3.7.0 alpha 1 / c api / platform

[bpo-30832](https://bugs.python.org/issue?@action=redirect&bpo=30832): Dropped the bespoke thread-local storage implementation. CPython had carried its own thread-local storage (TLS) code inside Python/thread.c, employed wherever a platform offered no native TLS. Yet every platform supported today (Windows alongside pthreads) ships native TLS and unconditionally defines the Py_HAVE_NATIVE_TLS macro regardless.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
