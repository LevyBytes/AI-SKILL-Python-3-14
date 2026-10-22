# Python 3.12.0 beta 1 / macos / introduce os prio darwin thread os prio darwin process os prio darwin bg os prio darwin nonui

[gh-103545](https://github.com/python/cpython/issues/103545): Introduce `os.PRIO_DARWIN_THREAD`, `os.PRIO_DARWIN_PROCESS`, `os.PRIO_DARWIN_BG` and `os.PRIO_DARWIN_NONUI`. Paired with `os.setpriority`, these let a process drop to a lower priority and take advantage of the efficiency cores found on Apple Silicon systems.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
