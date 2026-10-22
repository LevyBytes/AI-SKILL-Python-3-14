# getrandom nonblocking and entropy-source flags

os.GRND_NONBLOCK

Out of the box, a `getrandom()` call against `/dev/random` will wait whenever no random bytes can be supplied yet; pointed at `/dev/urandom`, the same call waits until the entropy pool finishes initializing.

Turning on the `GRND_NONBLOCK` flag changes that behaviour: rather than waiting in either situation, `getrandom()` returns at once and raises [`BlockingIOError`](https://docs.python.org/3.14/library/exceptions.html#BlockingIOError).

Added in version 3.6.

 os.GRND_RANDOM

When this bit is enabled, the random bytes come from the `/dev/random` pool rather than from the `/dev/urandom` pool.

Added in version 3.6.

[Subject index](INDEX.md)
