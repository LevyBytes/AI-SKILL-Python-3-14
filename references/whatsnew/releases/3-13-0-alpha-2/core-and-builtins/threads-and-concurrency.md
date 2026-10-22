# Python 3.13.0 alpha 2 / core and builtins / threads and concurrency

[gh-81925](https://github.com/python/cpython/issues/81925): Provide native thread ids on GNU KFreeBSD.

[gh-110829](https://github.com/python/cpython/issues/110829): When a thread is joined, the backing OS thread is now guaranteed to have ended. Safer fork() within multi-threaded processes depends on this.

[gh-110481](https://github.com/python/cpython/issues/110481): Bring biased reference counting to `--disable-gil` builds.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
