# random - Bookkeeping functions

### Bookkeeping functions

 random.seed(*a=None*, *version=2*)

Initialize the random number generator.

When *a* is left out or set to `None`, the present system time supplies the seed. Should the operating system expose randomness sources, those take precedence over the system time (consult the [`os.urandom()`](https://docs.python.org/3.14/library/os.html#os.urandom) function for notes on availability).

When *a* is an int, its absolute value serves directly.

Under version 2 (the default), a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), or [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) object is turned into an [`int`](https://docs.python.org/3.14/library/functions.html#int) with every one of its bits retained.

Under version 1 (kept around so random sequences from earlier Python releases can be reproduced), the procedure for [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) and [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) yields a more limited span of seeds.

Changed in version 3.2: Switched to the version 2 approach, which draws on every bit of a string seed.

Changed in version 3.11: The *seed* is now restricted to one of these types: `None`, [`int`](https://docs.python.org/3.14/library/functions.html#int), [`float`](https://docs.python.org/3.14/library/functions.html#float), [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), or [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray).

 random.getstate()

Hand back an object that records the generator's current internal state. Passing this object to `setstate()` lets you restore that state.

 random.setstate(*state*)

*state* must have come from an earlier `getstate()` call, and `setstate()` returns the generator's internal state to what it held when `getstate()` ran.

[Subject index](INDEX.md) · [Previous](random-generate-pseudo-random-numbers.md) · [Continue](random-randbytes.md) · [Owning module, declaration or section: random](random-generate-pseudo-random-numbers.md)
