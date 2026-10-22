# Python 3.14.0 alpha 6 / library / uuid

[gh-131196](https://github.com/python/cpython/issues/131196): Speeds up [`uuid.UUID.hex`](https://docs.python.org/3.14/library/uuid.html#uuid.UUID.hex) along with [`uuid.UUID.__str__`](https://docs.python.org/3.14/reference/datamodel.html#object.__str__).

[gh-130461](https://github.com/python/cpython/issues/130461): Strips the `.. index::` directives from the [`uuid`](https://docs.python.org/3.14/library/uuid.html#module-uuid) module documentation. Those directives had been generating general-index entries for [`getnode()`](https://docs.python.org/3.14/library/uuid.html#uuid.getnode) plus the [`uuid1()`](https://docs.python.org/3.14/library/uuid.html#uuid.uuid1), [`uuid3()`](https://docs.python.org/3.14/library/uuid.html#uuid.uuid3), [`uuid4()`](https://docs.python.org/3.14/library/uuid.html#uuid.uuid4), [`uuid5()`](https://docs.python.org/3.14/library/uuid.html#uuid.uuid5), and [`uuid8()`](https://docs.python.org/3.14/library/uuid.html#uuid.uuid8) constructor functions.

[gh-89083](https://github.com/python/cpython/issues/89083): A new [`uuid.uuid7()`](https://docs.python.org/3.14/library/uuid.html#uuid.uuid7) produces UUIDv7 objects following the specification in [**RFC 9562**](https://datatracker.ietf.org/doc/html/rfc9562.html). Bénédikt Tran wrote the patch.

[gh-89083](https://github.com/python/cpython/issues/89083): A new [`uuid.uuid6()`](https://docs.python.org/3.14/library/uuid.html#uuid.uuid6) produces UUIDv6 objects following the specification in [**RFC 9562**](https://datatracker.ietf.org/doc/html/rfc9562.html). Bénédikt Tran wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
