# List-comprehension construction and equivalent nested loops

### 5.1.3. List Comprehensions

A compact route to building lists is the list comprehension. They are typically employed to construct fresh lists whose every element comes from applying some operation across each member of another sequence or iterable, or to assemble the subsequence of members that meet a given condition.

Suppose, for instance, that we wish to build a list of squares, like so:

```python
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

```

Observe that this leaves behind (or overwrites) a variable named `x` which lingers once the loop has finished. The same list of squares can be produced free of side effects through:

```python
squares = list(map(lambda x: x**2, range(10)))

```

or, to the same effect:

```python
squares = [x**2 for x in range(10)]

```

which reads more cleanly and stays shorter.

A list comprehension is made of brackets wrapping an expression, after which comes a `for` clause and then any number of further `for` or `if` clauses. What you get back is a fresh list built by evaluating that expression within the scope of the `for` and `if` clauses trailing it. As an example, the listcomp below joins the members of two lists whenever they differ:

```python
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

```

and that amounts to:

```python
>>> combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
...
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

```

Observe that the [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for) and [`if`](https://docs.python.org/3.14/reference/compound_stmts.html#if) statements appear in the very same order across both of these snippets.

Should the expression itself be a tuple (such as the `(x, y)` shown just above), you have to wrap it in parentheses.

[Subject index](INDEX.md) · [Previous source section](using-lists-as-queues.md) · [Following source section](list-comprehension-filtering-and-flattening.md) · [Related tutorial example and explanation](list-comprehension-filtering-and-flattening.md)
