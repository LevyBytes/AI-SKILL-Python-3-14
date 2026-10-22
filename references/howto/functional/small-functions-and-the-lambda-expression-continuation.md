# Small functions and the lambda expression continuation

```python
import functools
def combine(a, b):
    return 0, a[1] + b[1]

total = functools.reduce(combine, items)[1]

```

Yet the finest choice of all would have been to just reach for a `for` loop:

```python
total = 0
for a, b in items:
    total += b

```

Or the [`sum()`](https://docs.python.org/3.14/library/functions.html#sum) built-in and a generator expression:

```python
total = sum(b for a, b in items)

```

A great deal of [`functools.reduce()`](https://docs.python.org/3.14/library/functools.html#functools.reduce) code reads more plainly once recast as `for` loops.

Fredrik Lundh at one point put forward this collection of guidelines for reworking `lambda` usage:

1.

Draft a lambda function.

2.

Add a comment that spells out what on earth that lambda is doing.

3.

Sit with that comment a moment, then come up with a name that distills its gist.

4.

Turn the lambda into a def statement that carries that name.

5.

Remove the comment.

These guidelines appeal to me a lot, though you are welcome to take a different view on whether dropping lambdas truly reads better.

[Subject index](INDEX.md) · [Previous source owning section](small-functions-and-the-lambda-expression.md) · [Following source context](revision-history-and-acknowledgements.md)
