# Python 3.14.0 alpha 5 / security / imaplib

[gh-119511](https://github.com/python/cpython/issues/119511): A possible denial of service in the [`imaplib`](https://docs.python.org/3.14/library/imaplib.html#module-imaplib) module has been fixed. Connecting to a hostile server could provoke an arbitrary quantity of memory to be allocated. On many systems that does no harm, since unused virtual memory is merely a mapping, but were it to reach a virtual address size limit it might raise a [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError) or otherwise crash the process. On unusual systems or builds where every allocated byte is touched and backed by real ram or storage, it could have kept eating resources up until a similar crash.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
