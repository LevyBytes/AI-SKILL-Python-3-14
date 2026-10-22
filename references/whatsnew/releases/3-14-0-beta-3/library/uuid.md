# Python 3.14.0 beta 3 / library / uuid

[gh-135244](https://github.com/python/cpython/issues/135244): [`uuid`](https://docs.python.org/3.14/library/uuid.html#module-uuid): if the MAC address is undeterminable, the 48-bit node ID is now produced via a cryptographically-secure pseudo-random number generator (CSPRNG), following [**RFC 9562,6.10.3**](https://datatracker.ietf.org/doc/html/rfc9562.html#section-6.10-3). Both [`uuid1()`](https://docs.python.org/3.14/library/uuid.html#uuid.uuid1) and [`uuid6()`](https://docs.python.org/3.14/library/uuid.html#uuid.uuid6) are affected.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
