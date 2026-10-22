# Python 3.13.0 alpha 1 / tests / build and platforms

[gh-109015](https://github.com/python/cpython/issues/109015): Repaired the test_asyncio, test_imaplib, and test_socket tests on FreeBSD whenever the TCP blackhole is turned on (`sysctl net.inet.tcp.blackhole`). Omit those handful of tests that broke with `ETIMEDOUT` under such a nonstandard setup. As things stand, the [FreeBSD GCP image enables TCP and UDP blackhole](https://reviews.freebsd.org/D41751) (`sysctl net.inet.tcp.blackhole=2` and `sysctl net.inet.udp.blackhole=1`). Victor Stinner authored the patch.

[gh-108962](https://github.com/python/cpython/issues/108962): Omit `test_tempfile.test_flags()` whenever `chflags()` breaks with ?OSError: [Errno 45] Operation not supported? (e.g. on FreeBSD 13). Victor Stinner authored the patch.

[gh-91960](https://github.com/python/cpython/issues/91960): Cirrus-CI (a hosted CI service spanning Linux, macOS, Windows, and FreeBSD) now delivers FreeBSD 13.2 CI coverage for pull requests.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
