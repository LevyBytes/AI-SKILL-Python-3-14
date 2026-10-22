# 5.2. The `del` statement

### 5.2. The `del` statement

A list also offers a way to drop an item by its index rather than by its value: the [`del`](https://docs.python.org/3.14/reference/simple_stmts.html#del) statement. It is unlike the [`pop()`](https://docs.python.org/3.14/library/stdtypes.html#list.pop) method, which gives back a value. The `del` statement serves equally well to strip slices out of a list or to empty the whole list (something we accomplished before by assigning an empty list to the slice). As an illustration:

```python
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]

```

[`del`](https://docs.python.org/3.14/reference/simple_stmts.html#del) is also good for erasing whole variables:

```python
>>> del a

```

After that point, naming `a` is an error (at any rate until some new value gets assigned to it). Further uses for [`del`](https://docs.python.org/3.14/reference/simple_stmts.html#del) will turn up later on.

[Subject index](INDEX.md) · [Previous source section](nested-list-comprehensions.md) · [Following source section](tuples-and-sequences.md)
