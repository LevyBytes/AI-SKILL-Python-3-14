# expressions: Numeric, string, collection and sequence comparisons

Values belonging to the built-in numeric types ([Numeric Types — int, float, complex](https://docs.python.org/3.14/library/stdtypes.html#typesnumeric)), together with the standard library's [`fractions.Fraction`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction) and [`decimal.Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal), may be compared both among their own kind and across these kinds, the lone caveat being that complex numbers offer no order comparison. As far as the participating types allow, that comparison is mathematically (algorithmically) accurate and surrenders no precision.

A unique status belongs to the not-a-number values `float('NaN')` and `decimal.Decimal('NaN')`. Whenever a number is ordered against a not-a-number value, the result is false. One unexpected upshot is that a not-a-number value never equals itself. To illustrate, given `x = float('NaN')`, each of `3 < x`, `x < 3` and `x == x` comes out false, whereas `x != x` is true. Such conduct conforms to IEEE 754.

- Both `None` and [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented) exist as singletons. The guidance in [**PEP 8**](https://peps.python.org/pep-0008/) is that you check singletons with `is` or `is not` at all times, and never reach for the equality operators.

- You can compare binary sequences (objects of [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) or [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray)) within a single type and between the two. The comparison proceeds lexicographically, drawing on the numeric value of each element.

- Strings (objects of [`str`](https://docs.python.org/3.14/library/stdtypes.html#str)) are ranked lexicographically by the numeric Unicode code points of their characters (what the built-in [`ord()`](https://docs.python.org/3.14/library/functions.html#ord) function yields). [3]

A direct comparison between a string and a binary sequence is not allowed.

- Sequences (objects of [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple), [`list`](https://docs.python.org/3.14/library/stdtypes.html#list), or [`range`](https://docs.python.org/3.14/library/stdtypes.html#range)) are comparable solely within their own type, with ranges again offering no order comparison. Testing equality between two of these distinct types yields inequality, while attempting an ordering comparison between them raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

Two sequences are ranked lexicographically by pairing up and comparing their matching elements. As a rule the built-in containers take it for granted that an object is equal to itself. This assumption lets them skip the equality check for identical objects, which boosts speed and keeps their internal invariants intact.

Here is how the lexicographical comparison among built-in collections plays out:

  - Two collections count as equal only when they share a type, match in length, and every matching pair of elements compares equal (so `[1,2] == (1,2)` turns out false, the types being different).

  - Where order comparison is available, collections rank according to the first place their elements differ (thus `[1,2,x] <= [1,2,y]` works out the same as `x <= y`). When a matching element is missing, the shorter collection comes first (so `[1,2] < [1,2,3]` holds true).

- Mappings (objects of [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict)) are equal precisely when their `(key, value)` pairs match. When the keys and values are compared for equality, reflexivity is assumed.

Any order comparison (`<`, `>`, `<=`, and `>=`) raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

- Sets (objects of [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) or [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset)) admit comparison inside one type and across the two.

For sets, the order comparison operators stand for subset and superset checks. These relations fall short of a total ordering (consider how the sets `{1,2}` and `{2,3}` are neither equal, nor subset of, nor superset of each other). For that reason, sets make poor arguments to functions that rely on total ordering (passing a list of sets to [`min()`](https://docs.python.org/3.14/library/functions.html#min), [`max()`](https://docs.python.org/3.14/library/functions.html#max), or [`sorted()`](https://docs.python.org/3.14/library/functions.html#sorted), for instance, gives undefined results).

When sets are compared, reflexivity of their elements is assumed.

- The remaining built-in types mostly supply no comparison methods of their own, leaving them with the default comparison behavior.

Whenever a user-defined class tailors how it compares, it ought to honor a few consistency rules where it can:

- Keep equality comparison reflexive. Said another way, an object ought to compare equal to itself:

>

`x is y` implies `x == y`

- Keep comparison symmetric. Put differently, these expressions ought to yield matching results:

>

`x == y` and `y == x`

`x != y` and `y != x`

`x < y` and `y > x`

`x <= y` and `y >= x`

- Keep comparison transitive. The following sampling (by no means complete) demonstrates this:

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Owning language section](comparisons.md) · [Owning language section](value-comparisons.md) · [Previous source contract continuation](value-comparisons.md) · [Following source section](value-comparisons.md)
