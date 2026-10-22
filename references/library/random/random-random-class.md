# random: `random.Random`

### Alternative Generator

 *class *random.Random([*seed*])

Class providing the default pseudo-random number generator that the `random` module relies on.

Changed in version 3.11: Previously the *seed* could be any hashable object. It is now confined to: `None`, [`int`](https://docs.python.org/3.14/library/functions.html#int), [`float`](https://docs.python.org/3.14/library/functions.html#float), [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), or [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray).

Subclasses of `Random` ought to override the methods below when they intend to plug in a different basic generator:

[Subject index](INDEX.md) · [Previous](random-random-to-random-weibullvariate.md) · [Continue](random-random-seed-to-random-random-randbytes.md) · [Owning module, declaration or section: random](random-generate-pseudo-random-numbers.md)
