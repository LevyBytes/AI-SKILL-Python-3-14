# expressions: Value-comparison operators and object semantics

### 6.10.1. Value comparisons

The operators `<`, `>`, `==`, `>=`, `<=`, and `!=` compare the values held by two objects. Those objects need not share a type.

Chapter [Objects, values and types](https://docs.python.org/3.14/reference/datamodel.html#objects) explains that objects carry a value (alongside type and identity). In Python, an object's value is a fairly abstract idea: there is, for example, no canonical access method for retrieving an object’s value. There is likewise no requirement that an object's value be assembled in any specific manner — say, out of all its data attributes. The comparison operators realize a particular idea of what an object's value is. You can regard them as defining an object's value indirectly, by way of their comparison implementation.

Since all types are (directly or indirectly) subtypes of [`object`](https://docs.python.org/3.14/library/functions.html#object), they pick up the default comparison behavior from `object`. Types are able to customize their comparison behavior by implementing *rich comparison methods* such as [`__lt__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__lt__), covered in [Basic customization](https://docs.python.org/3.14/reference/datamodel.html#customization).

The default behavior for equality comparison (`==` and `!=`) rests on the identity of the objects. As a result, equality comparison of instances sharing the same identity gives equality, and equality comparison of instances with differing identities gives inequality. One reason behind this default behavior is the wish that every object be reflexive (that is, `x is y` implies `x == y`).

No default order comparison (`<`, `>`, `<=`, and `>=`) is supplied; attempting one raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). One reason behind this default behavior is the absence of an invariant comparable to the one for equality.

The default equality comparison behavior — that instances with differing identities are forever unequal — may run counter to what is needed by types that carry a sensible definition of object value and value-based equality. Types of that sort will have to customize their comparison behavior, and indeed a number of built-in types already do so.

The list below describes the comparison behavior of the most important built-in types.

-

>

`x > y and y > z` implies `x > z`

`x < y and y <= z` implies `x < z`

- An inverse comparison ought to come out as the boolean negation. Stated otherwise, the expressions below ought to share a result:

>

`x == y` and `not x != y`

`x < y` and `not x >= y` (for total ordering)

`x > y` and `not x <= y` (for total ordering)

Those final two expressions hold for collections that are totally ordered (sequences, say, though not sets or mappings). The [`total_ordering()`](https://docs.python.org/3.14/library/functools.html#functools.total_ordering) decorator is worth a look here too.

- Whatever [`hash()`](https://docs.python.org/3.14/library/functions.html#hash) returns ought to line up with equality. Two equal objects should either carry the same hash value or else be declared unhashable.

These consistency rules are not enforced by Python. The not-a-number values, in point of fact, are a case that disregards them.

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Owning language section](comparisons.md) · [Following source contract continuation](numeric-and-sequence-value-comparisons.md) · [Previous source section](comparisons.md) · [Contract or procedure setup](numeric-and-sequence-value-comparisons.md) · [Previous source section](numeric-and-sequence-value-comparisons.md) · [Following source section](membership-test-operations.md)
