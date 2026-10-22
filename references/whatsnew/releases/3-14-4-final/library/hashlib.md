# Python 3.14.4 final / library / hashlib

[gh-145376](https://github.com/python/cpython/issues/145376): Corrects a double free along with a null pointer dereference across unusual error scenarios inside the [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib) plus [`hmac`](https://docs.python.org/3.14/library/hmac.html#module-hmac) modules.

[gh-145301](https://github.com/python/cpython/issues/145301): [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib): corrects a crash whenever initialization of the underlying C extension module fails.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
