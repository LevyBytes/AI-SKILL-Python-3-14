# Python 3.12.0 alpha 1 / core and builtins / adopts exponential backoff interpreter s specialization counters

[gh-93354](https://github.com/python/cpython/issues/93354): Adopts exponential backoff for the interpreter's specialization counters. This can cut the count of failed specializations a great deal and dodge slowdown across program sections poorly suited to specialization.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
