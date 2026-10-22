# Python 3.14.1 final / library / resolve possible hang within multiprocessing popen spawn posix arising child proc exits

[gh-118981](https://github.com/python/cpython/issues/118981): Resolve a possible hang within `multiprocessing.popen_spawn_posix` arising when the child proc exits early, achieved by shutting the child fds without delay.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
