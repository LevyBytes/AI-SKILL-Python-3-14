# Python 3.10.0 alpha 1 / core and builtins / collections and iteration

[bpo-41175](https://bugs.python.org/issue?@action=redirect&bpo=41175): Defends against a NULL pointer dereference inside bytearrayobject set off by the `bytearray() + bytearray()` operation.

[bpo-29590](https://bugs.python.org/issue?@action=redirect&bpo=29590): Produce a correct stack trace after [`generator.throw()`](https://docs.python.org/3.14/reference/expressions.html#generator.throw) is called on a generator that has delegated through a `yield from`.

[bpo-4022](https://bugs.python.org/issue?@action=redirect&bpo=4022): Boost generator performance by avoiding the internal StopIteration raise.

[bpo-40889](https://bugs.python.org/issue?@action=redirect&bpo=40889): Symmetric difference operations over dictionary item views now run faster. Dennis Sweeney authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
