# Python 3.9.0 alpha 1 / core and builtins / stdtypes

[bpo-28029](https://bugs.python.org/issue?@action=redirect&bpo=28029): For every non-zero `n`, the expression `"".replace("", s, n)` yields `s` rather than an empty result. Equivalent fixes apply to [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) objects.

[bpo-38465](https://bugs.python.org/issue?@action=redirect&bpo=38465): The [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray), [`array`](https://docs.python.org/3.14/library/array.html#array.array) and [`mmap`](https://docs.python.org/3.14/library/mmap.html#mmap.mmap) objects can henceforth export more than `2**31` buffers simultaneously.

[bpo-38219](https://bugs.python.org/issue?@action=redirect&bpo=38219): Sped up the [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) constructor along with the [`update()`](https://docs.python.org/3.14/library/stdtypes.html#dict.update) method whenever the supplied argument happens to be a dict.

[bpo-37417](https://bugs.python.org/issue?@action=redirect&bpo=37417): Brandt Bucher contributed a fix so [`bytearray.extend()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray.extend) properly deals with errors raised throughout iteration.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
