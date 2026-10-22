# reprlib: `Repr.indent`, `Repr.repr()`, `Repr.repr1()`, `Repr.repr_TYPE()`

Repr.indent

When this attribute holds `None` (the default), the output comes out with no line breaks or indentation, just like the standard [`repr()`](https://docs.python.org/3.14/library/functions.html#repr). Take this example:

```pycon
>>> example = [
...     1, 'spam', {'a': 2, 'b': 'spam eggs', 'c': {3: 4.5, 6: []}}, 'ham']
>>> import reprlib
>>> aRepr = reprlib.Repr()
>>> print(aRepr.repr(example))
[1, 'spam', {'a': 2, 'b': 'spam eggs', 'c': {3: 4.5, 6: []}}, 'ham']

```

When `indent` holds a string, every recursion level lands on its own line, indented using that string:

```pycon
>>> aRepr.indent = '-->'
>>> print(aRepr.repr(example))
[
-->1,
-->'spam',
-->{
-->-->'a': 2,
-->-->'b': 'spam eggs',
-->-->'c': {
-->-->-->3: 4.5,
-->-->-->6: [],
-->-->},
-->},
-->'ham',
]

```

Giving `indent` a positive integer value works as though you had set it to a string holding that many spaces:

```pycon
>>> aRepr.indent = 4
>>> print(aRepr.repr(example))
[
    1,
    'spam',
    {
        'a': 2,
        'b': 'spam eggs',
        'c': {
            3: 4.5,
            6: [],
        },
    },
    'ham',
]

```

Added in version 3.12.

 Repr.repr(*obj*)

The counterpart to the built-in [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) that applies the formatting the instance enforces.

 Repr.repr1(*obj*, *level*)

The recursive implementation that `repr()` relies on. It inspects the type of *obj* to pick which formatting method to invoke, handing that method *obj* and *level*. The type-specific methods are expected to invoke `repr1()` for recursive formatting, supplying `level - 1` as the *level* value in the recursive call.

 Repr.repr_TYPE(*obj*, *level*)

Formatting methods for particular types take the form of methods whose names derive from the type name. Within the method name, **TYPE** stands in for `'_'.join(type(obj).__name__.split())`. `repr1()` takes care of dispatching to these methods. A type-specific method that needs to format a value recursively should invoke `self.repr1(subobj, level - 1)`.

[Subject index](INDEX.md) · [Previous](repr-fillvalue-to-repr-maxother.md) · [Continue](subclassing-repr-objects.md) · [Owning module, declaration or section: reprlib](reprlib-repr-class-to-reprlib-repr.md) · [Owning module, declaration or section: Repr Objects](repr-fillvalue-to-repr-maxother.md)
