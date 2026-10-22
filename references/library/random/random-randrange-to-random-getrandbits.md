# random — Functions for integers

### Functions for integers

 random.randrange(*stop*)

 random.randrange(*start*, *stop*[, *step*])

Return a randomly selected element from `range(start, stop, step)`.

In effect this matches `choice(range(start, stop, step))`, yet it copes with ranges of any size and is tuned for the usual cases.

The way positional arguments work here mirrors the [`range()`](https://docs.python.org/3.14/library/stdtypes.html#range) function.

Avoid keyword arguments, since they may be read in surprising ways. As an illustration, `randrange(start=100)` ends up being read as `randrange(0, 100, 1)`.

Changed in version 3.2: `randrange()` now does a better job of yielding evenly spread values. Previously it relied on a form akin to `int(random()*n)`, which could leave the distribution a little lopsided.

Changed in version 3.12: Non-integer types are no longer converted automatically. Calls along the lines of `randrange(10.0)` and `randrange(Fraction(10, 1))` now raise a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

 random.randint(*a*, *b*)

Return a random integer *N* such that `a <= N <= b`. Alias for `randrange(a, b+1)`.

 random.getrandbits(*k*)

Hand back a non-negative Python integer carrying *k* random bits. The Mersenne Twister generator ships with this method, and certain other generators may expose it too as an optional piece of the API. Where it exists, `getrandbits()` lets `randrange()` cope with ranges of any size.

Changed in version 3.9: A value of zero for *k* is now permitted by this method.

[Subject index](INDEX.md) · [Previous](random-randbytes.md) · [Continue](random-choice-to-random-sample.md) · [Owning module, declaration or section: random](random-generate-pseudo-random-numbers.md)
