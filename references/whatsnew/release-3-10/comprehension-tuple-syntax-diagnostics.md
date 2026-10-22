# Python 3.10 changes: Comprehension tuple and target syntax diagnostics

Unparenthesised tuples in comprehensions targets:

```python
>>> {x,y for x,y in zip('abcd', '1234')}
  File "<stdin>", line 1
    {x,y for x,y in zip('abcd', '1234')}
     ^
SyntaxError: did you forget parentheses around the comprehension target?

```

> (Contributed by Pablo Galindo in [bpo-43017](https://bugs.python.org/issue?@action=redirect&bpo=43017).)

- Missing commas in collection literals and between expressions:

```python
>>> items = {
... x: 1,
... y: 2
... z: 3,
  File "<stdin>", line 3
    y: 2
       ^
SyntaxError: invalid syntax. Perhaps you forgot a comma?

```

> (Contributed by Pablo Galindo in [bpo-43822](https://bugs.python.org/issue?@action=redirect&bpo=43822).)

- Multiple Exception types without parentheses:

```python
>>> try:
...     build_dyson_sphere()
... except NotEnoughScienceError, NotEnoughResourcesError:
  File "<stdin>", line 3
    except NotEnoughScienceError, NotEnoughResourcesError:
           ^
SyntaxError: multiple exception types must be parenthesized

```

> (Contributed by Pablo Galindo in [bpo-43149](https://bugs.python.org/issue?@action=redirect&bpo=43149).)

- Missing `:` and values in dictionary literals:

```python
>>> values = {
... x: 1,
... y: 2,
... z:
... }
  File "<stdin>", line 4
    z:
     ^
SyntaxError: expression expected after dictionary key and ':'

>>> values = {x:1, y:2, z w:3}
  File "<stdin>", line 1
    values = {x:1, y:2, z w:3}
                        ^
SyntaxError: ':' expected after dictionary key

```

> (Contributed by Pablo Galindo in [bpo-43823](https://bugs.python.org/issue?@action=redirect&bpo=43823).)

- `try` blocks without `except` or `finally` blocks:

[Subject index](INDEX.md) · [Previous source section](better-error-messages-syntaxerrors-syntaxerrors.md) · [Next source section](comparison-operator-syntax-diagnostics.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](better-error-messages-syntaxerrors-syntaxerrors.md)
