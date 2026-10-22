# 3.2.4.1. `numbers.Integral`

#### 3.2.4.1. [`numbers.Integral`](https://docs.python.org/3.14/library/numbers.html#numbers.Integral)

These stand for members of the mathematical set of integers (both positive and negative).

Note

The conventions for how integers are represented aim to deliver the most sensible reading of shift and mask operations that involve negative integers.

There are two types of integers:

Integers ([`int`](https://docs.python.org/3.14/library/functions.html#int))

These stand for numbers spanning an unlimited range, bounded solely by the (virtual) memory on hand. When shift and mask operations come into play, a binary representation is presumed, and negative numbers are held in a variation on 2’s complement that creates the impression of an endless run of sign bits stretching off to the left.

Booleans ([`bool`](https://docs.python.org/3.14/library/functions.html#bool))

These stand for the truth values False and True. The only Boolean objects are the two objects that represent the values `False` and `True`. Being a subtype of the integer type, the Boolean type makes its values act like 0 and 1, respectively, across nearly every context, save that converting them to a string yields the strings `"False"` or `"True"`, respectively.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Owning language section](numbers-number.md) · [Previous source section](numbers-number.md) · [Following source section](numbers-real.md)
