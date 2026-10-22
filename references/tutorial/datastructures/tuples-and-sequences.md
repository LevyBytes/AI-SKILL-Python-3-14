# 5.3. Tuples and Sequences

### 5.3. Tuples and Sequences

We have seen that lists and strings share plenty of behavior, indexing and slicing operations among them. Both rank as examples of *sequence* data types (refer to [Sequence Types — list, tuple, range](https://docs.python.org/3.14/library/stdtypes.html#typesseq)). Because Python keeps evolving as a language, further sequence data types might appear. One more built-in sequence data type also exists: the *tuple*.

A tuple is formed from several values set apart by commas, as in:

```python
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # Tuples may be nested:
>>> u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuples are immutable:
>>> t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # but they can contain mutable objects:
>>> v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])

```

Notice that, on output, tuples come wrapped in parentheses every time, ensuring nested tuples read correctly; you may type them in with or without enclosing parentheses, though parentheses end up required fairly often anyway (whenever the tuple sits inside a larger expression). Assigning to the separate items of a tuple is impossible, yet you can certainly build tuples that hold mutable objects, lists for instance.

Even if tuples appear to resemble lists, the two tend to serve distinct situations and distinct ends. Tuples are [immutable](https://docs.python.org/3.14/glossary.html#term-immutable) and commonly carry a heterogeneous run of elements reached through unpacking (covered further along in this section) or by indexing (or even by attribute when working with [`namedtuples`](https://docs.python.org/3.14/library/collections.html#collections.namedtuple)). Lists are [mutable](https://docs.python.org/3.14/glossary.html#term-mutable), their elements tend to be homogeneous, and they are reached by iterating across the list.

One peculiar matter is forming tuples that hold 0 or 1 items: the syntax carries a couple of additional quirks to handle them. You build an empty tuple from an empty pair of parentheses; you build a one-item tuple by trailing a value with a comma (merely wrapping a lone value in parentheses won't do). Inelegant, yet it works. As an illustration:

```python
>>> empty = ()
>>> singleton = 'hello',    # <-- note trailing comma
>>> len(empty)
0
>>> len(singleton)
1
>>> singleton
('hello',)

```

The line `t = 12345, 54321, 'hello!'` illustrates *tuple packing*: the values `12345`, `54321` and `'hello!'` get bundled together into a tuple. Going the other direction is possible too:

```python
>>> x, y, z = t

```

This goes by the fitting name *sequence unpacking* and applies to any sequence sitting on the right-hand side. For sequence unpacking, the left side of the equals sign needs exactly as many variables as the sequence has elements. Take note that multiple assignment is really nothing more than tuple packing and sequence unpacking working in tandem.

[Subject index](INDEX.md) · [Previous source section](the-del-statement.md) · [Following source section](sets.md)
