# 3.2.5.1. Immutable sequences

#### 3.2.5.1. Immutable sequences

Once built, an object of an immutable sequence type cannot be altered. (Should the object keep references to further objects, those further objects may well be mutable and may well be altered; nevertheless the set of objects an immutable object directly references cannot be altered.)

These are the types that count as immutable sequences:

Strings

Each string ([`str`](https://docs.python.org/3.14/library/stdtypes.html#str)) forms a sequence of values that denote *characters* — or, stated with more rigor, *Unicode code points*. A string can hold any code point falling between `0` and `0x10FFFF`.

There is no separate *character* type in Python. Rather, each code point of the string shows up as a string object whose length is `1`.

The built-in function [`ord()`](https://docs.python.org/3.14/library/functions.html#ord) maps a code point from its string form onto an integer somewhere between `0` and `0x10FFFF`; [`chr()`](https://docs.python.org/3.14/library/functions.html#chr) maps an integer somewhere between `0` and `0x10FFFF` onto the corresponding length `1` string object. With a chosen text encoding, [`str.encode()`](https://docs.python.org/3.14/library/stdtypes.html#str.encode) turns a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) into [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), while [`bytes.decode()`](https://docs.python.org/3.14/library/stdtypes.html#bytes.decode) performs the reverse.

Tuples

Whatever Python objects you like may serve as the items of a [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple). To form tuples of two or more items, write expressions separated by commas. A one-item tuple (a ‘singleton’) is built by tacking a comma onto an expression (an expression standing alone does not yield a tuple, because parentheses have to stay available for grouping expressions). An empty pair of parentheses builds an empty tuple.

Bytes

An immutable array is what a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object amounts to. Its items are 8-bit bytes, each shown as an integer where 0 <= x < 256. To make bytes objects, you can write bytes literals (such as `b'abc'`) or call the built-in [`bytes()`](https://docs.python.org/3.14/library/stdtypes.html#bytes) constructor. Furthermore, a bytes object can be turned into a string through its [`decode()`](https://docs.python.org/3.14/library/stdtypes.html#bytes.decode) method.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Owning language section](sequences.md) · [Previous source section](sequences.md) · [Following source section](mutable-sequences.md)
