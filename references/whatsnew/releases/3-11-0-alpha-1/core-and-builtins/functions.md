# Python 3.11.0 alpha 1 / core and builtins / functions

[bpo-37330](https://bugs.python.org/issue?@action=redirect&bpo=37330): [`open()`](https://docs.python.org/3.14/library/functions.html#open), [`io.open()`](https://docs.python.org/3.14/library/io.html#io.open), [`codecs.open()`](https://docs.python.org/3.14/library/codecs.html#codecs.open) and [`fileinput.FileInput`](https://docs.python.org/3.14/library/fileinput.html#fileinput.FileInput) will no longer take `'U'` (“universal newline”) within the file mode. That flag had been deprecated since Python 3.3. Victor Stinner contributed the patch.

[bpo-44232](https://bugs.python.org/issue?@action=redirect&bpo=44232): Corrected a regression in [`type()`](https://docs.python.org/3.14/library/functions.html#type) whenever a metaclass raises an exception. The C function `type_new()` has to report the exception correctly when a metaclass constructor raises one and the winner class differs from the metaclass. Victor Stinner wrote the patch.

[bpo-44523](https://bugs.python.org/issue?@action=redirect&bpo=44523): Removed the pass-through for [`hash()`](https://docs.python.org/3.14/library/functions.html#hash) on [`weakref.proxy`](https://docs.python.org/3.14/library/weakref.html#weakref.proxy) objects, sidestepping unintended fallout when the original referent dies while the proxy belongs to a hashable object. Pablo Galindo wrote the patch.

[bpo-24234](https://bugs.python.org/issue?@action=redirect&bpo=24234): Provide the `__complex__()` special method on the [`complex`](https://docs.python.org/3.14/library/functions.html#complex) type, allowing a complex number `z` to clear an `isinstance(z, typing.SupportsComplex)` check.

[bpo-44698](https://bugs.python.org/issue?@action=redirect&bpo=44698): Bring back the behaviour of complex exponentiation when the exponent is integer-valued and of type [`float`](https://docs.python.org/3.14/library/functions.html#float) or [`complex`](https://docs.python.org/3.14/library/functions.html#complex).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
