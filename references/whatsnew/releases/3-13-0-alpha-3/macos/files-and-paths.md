# Python 3.13.0 alpha 3 / macos / files and paths

[gh-109981](https://github.com/python/cpython/issues/109981): On macOS, rely on `/dev/fd` to count open files within `test.support.os_helper.fd_count`, sidestepping a crash on "guarded" file descriptors while probing for open files.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
