# object.__getitem__(*self*, *subscript*)

object.__getitem__(*self*, *subscript*)

Invoked to back *subscription*, namely `self[subscript]`. Consult [Subscriptions and slicings](https://docs.python.org/3.14/reference/expressions.html#subscriptions) for the syntax specifics.

Two categories of built-in objects allow subscription by way of `__getitem__()`:

- **sequences**, in which *subscript* (sometimes called the [index](https://docs.python.org/3.14/glossary.html#term-index)) should be an integer or a [`slice`](https://docs.python.org/3.14/library/functions.html#slice) object. The sequence documentation describes the expected behavior, covering how `slice` objects and negative indices are handled.

- **mappings**, in which *subscript* is also referred to as the [key](https://docs.python.org/3.14/glossary.html#term-key). The mapping documentation describes the expected behavior.

When *subscript* is of an unsuitable type, `__getitem__()` ought to raise [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). When *subscript* carries an unsuitable value, `__getitem__()` ought to raise an [`LookupError`](https://docs.python.org/3.14/library/exceptions.html#LookupError) or some subclass of it ([`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError) for sequences; [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) for mappings).

Note

Slice operations are managed by `__getitem__()`, `__setitem__()`, and `__delitem__()`. A statement such as

```python
a[1:2] = b

```

becomes

```python
a[slice(1, 2, None)] = b

```

and similarly for the rest. Any omitted slice items are always supplied as `None`.

Note

The sequence iteration protocol (employed, for instance, by [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for) loops) anticipates that an [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError) gets raised for out-of-range indexes so that the end of a sequence can be detected properly.

Note

While [subscripting](https://docs.python.org/3.14/reference/expressions.html#subscriptions) a *class*, the special class method `__class_getitem__()` may run in place of `__getitem__()`. Refer to __class_getitem__ versus __getitem__ for further details.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](emulating-container-types.md) · [Previous source section](object-length-hint.md) · [Following source section](object-setitem.md)
