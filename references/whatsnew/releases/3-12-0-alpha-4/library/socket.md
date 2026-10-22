# Python 3.12.0 alpha 4 / library / socket

[gh-100374](https://github.com/python/cpython/issues/100374): Correct a wrong result plus a delay inside [`socket.getfqdn()`](https://docs.python.org/3.14/library/socket.html#socket.getfqdn). Dominic Socular submitted the patch.

[gh-98030](https://github.com/python/cpython/issues/98030): Add missing TCP socket options from Linux: `TCP_MD5SIG`, `TCP_THIN_LINEAR_TIMEOUTS`, `TCP_THIN_DUPACK`, `TCP_REPAIR`, `TCP_REPAIR_QUEUE`, `TCP_QUEUE_SEQ`, `TCP_REPAIR_OPTIONS`, `TCP_TIMESTAMP`, `TCP_CC_INFO`, `TCP_SAVE_SYN`, `TCP_SAVED_SYN`, `TCP_REPAIR_WINDOW`, `TCP_FASTOPEN_CONNECT`, `TCP_ULP`, `TCP_MD5SIG_EXT`, `TCP_FASTOPEN_KEY`, `TCP_FASTOPEN_NO_COOKIE`, `TCP_ZEROCOPY_RECEIVE`, `TCP_INQ`, `TCP_TX_DELAY`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
