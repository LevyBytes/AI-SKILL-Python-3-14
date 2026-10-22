# operator: In-place arithmetic and bitwise operator functions

### In-place Operators

A good number of operations come with an “in-place” counterpart. The functions below expose lower-level access to those in-place operators than the ordinary syntax offers; for instance, the [statement](https://docs.python.org/3.14/glossary.html#term-statement) `x += y` is equivalent to `x = operator.iadd(x, y)`. Put differently, `z = operator.iadd(x, y)` is equivalent to the compound statement `z = x; z += y`.

Notice in those cases that invoking an in-place method splits the work into two distinct phases: computing and assigning. The in-place functions shown here cover only the first phase — calling the in-place method — and leave the second phase, the assignment, to you.

When the target is immutable, as with strings, numbers, and tuples, the new value gets computed but is never written back to the input variable:

```python
>>> a = 'hello'
>>> iadd(a, ' world')
'hello world'
>>> a
'hello'

```

When the target is mutable, as with lists and dictionaries, the in-place method carries out the change directly, so there's no follow-up assignment to do:

```python
>>> s = ['h', 'e', 'l', 'l', 'o']
>>> iadd(s, [' ', 'w', 'o', 'r', 'l', 'd'])
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
>>> s
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

```

 `operator.iadd(*a*, *b*)`

 `operator.__iadd__(*a*, *b*)`

`a = iadd(a, b)` is equivalent to `a += b`.

 `operator.iand(*a*, *b*)`

 `operator.__iand__(*a*, *b*)`

`a = iand(a, b)` is equivalent to `a &= b`.

 `operator.iconcat(*a*, *b*)`

 `operator.__iconcat__(*a*, *b*)`

`a = iconcat(a, b)` is equivalent to `a += b` for *a* and *b* sequences.

 `operator.ifloordiv(*a*, *b*)`

 `operator.__ifloordiv__(*a*, *b*)`

`a = ifloordiv(a, b)` is equivalent to `a //= b`.

 `operator.ilshift(*a*, *b*)`

 `operator.__ilshift__(*a*, *b*)`

`a = ilshift(a, b)` is equivalent to `a <<= b`.

 `operator.imod(*a*, *b*)`

 `operator.__imod__(*a*, *b*)`

`a = imod(a, b)` is equivalent to `a %= b`.

 `operator.imul(*a*, *b*)`

 `operator.__imul__(*a*, *b*)`

`a = imul(a, b)` is equivalent to `a *= b`.

 `operator.imatmul(*a*, *b*)`

 `operator.__imatmul__(*a*, *b*)`

`a = imatmul(a, b)` is equivalent to `a @= b`.

Added in version 3.5.

 `operator.ior(*a*, *b*)`

 `operator.__ior__(*a*, *b*)`

`a = ior(a, b)` is equivalent to `a |= b`.

[Subject index](INDEX.md) · [Previous](mapping-operators-to-functions.md) · [Continue](operator-ipow-to-operator-ixor.md) · [Owning module, declaration or section: operator](operator-lt-to-operator-abs.md)
