# Python 3.8.0 alpha 1 / library / uuid

[bpo-32493](https://bugs.python.org/issue?@action=redirect&bpo=32493): Corrected [`uuid.uuid1()`](https://docs.python.org/3.14/library/uuid.html#uuid.uuid1) on FreeBSD.

[bpo-31784](https://bugs.python.org/issue?@action=redirect&bpo=31784): [`uuid.uuid1()`](https://docs.python.org/3.14/library/uuid.html#uuid.uuid1) now invokes [`time.time_ns()`](https://docs.python.org/3.14/library/time.html#time.time_ns) in place of `int(time.time() * 1e9)`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
