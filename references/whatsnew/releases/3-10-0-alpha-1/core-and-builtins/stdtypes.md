# Python 3.10.0 alpha 1 / core and builtins / stdtypes

[bpo-41681](https://bugs.python.org/issue?@action=redirect&bpo=41681): Corrects the misleading error text produced when 2 `,` appear in a format string inside an f-string and [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format).

[bpo-29882](https://bugs.python.org/issue?@action=redirect&bpo=29882): Introduce [`int.bit_count()`](https://docs.python.org/3.14/library/stdtypes.html#int.bit_count), which counts how many ones occur in an integer's binary form. Niklas Fiekas wrote the patch.

[bpo-40792](https://bugs.python.org/issue?@action=redirect&bpo=40792): The `start`, `stop` and `step` attributes of a [`range`](https://docs.python.org/3.14/library/stdtypes.html#range) object are now guaranteed to carry the exact type [`int`](https://docs.python.org/3.14/library/functions.html#int). Earlier releases allowed them to be an instance of an `int` subclass.

[bpo-41334](https://bugs.python.org/issue?@action=redirect&bpo=41334): The [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str), [`bytes()`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`bytearray()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) constructors now run quicker (roughly 30–40% on small objects).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
