# Python 3.10 changes: Syntax error diagnostics and location information

> (Contributed by Guido van Rossum, Pablo Galindo and Lysandros Nikolaou in [bpo-12782](https://bugs.python.org/issue?@action=redirect&bpo=12782) and [bpo-40334](https://bugs.python.org/issue?@action=redirect&bpo=40334).)

### Better error messages

#### SyntaxErrors

While reading source that has parentheses or brackets left open, the interpreter now reports where the unmatched bracket or parenthesis sits, rather than printing *SyntaxError: unexpected EOF while parsing* or aiming at some wrong spot. To illustrate, take the snippet below (observe the open "{"):

```python
expected = {9: 1, 18: 2, 19: 2, 27: 3, 28: 3, 29: 3, 36: 4, 37: 4,
            38: 4, 39: 4, 45: 5, 46: 5, 47: 5, 48: 5, 49: 5, 54: 6,
some_other_code = foo()

```

Earlier interpreter releases flagged misleading positions for the syntax error:

```python
File "example.py", line 3
    some_other_code = foo()
                    ^
SyntaxError: invalid syntax

```

yet under Python 3.10 a clearer diagnostic appears:

```python
File "example.py", line 1
    expected = {9: 1, 18: 2, 19: 2, 27: 3, 28: 3, 29: 3, 36: 4, 37: 4,
               ^
SyntaxError: '{' was never closed

```

Along the same lines, problems with unterminated string literals (both single and triple quoted) now reference where the string began rather than flagging EOF/EOL.

The PyPy interpreter's earlier work served as the basis for these enhancements.

> (Contributed by Pablo Galindo in [bpo-42864](https://bugs.python.org/issue?@action=redirect&bpo=42864) and Batuhan Taskaya in [bpo-40176](https://bugs.python.org/issue?@action=redirect&bpo=40176).)

[`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) exceptions thrown by the interpreter now mark the entire span of the expression that forms the syntax error, rather than only the point where the issue was caught. Therefore, in place of showing (prior to Python 3.10):

```python
>>> foo(x, z for z in range(10), t, w)
  File "<stdin>", line 1
    foo(x, z for z in range(10), t, w)
           ^
SyntaxError: Generator expression must be parenthesized

```

Python 3.10 now renders that exception this way:

```python
>>> foo(x, z for z in range(10), t, w)
  File "<stdin>", line 1
    foo(x, z for z in range(10), t, w)
           ^^^^^^^^^^^^^^^^^^^^
SyntaxError: Generator expression must be parenthesized

```

> This improvement was contributed by Pablo Galindo in [bpo-43914](https://bugs.python.org/issue?@action=redirect&bpo=43914).

Quite a few fresh specialized diagnostics for [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) exceptions were folded in. A handful of the most noteworthy ones include:

- Missing `:` before blocks:

```python
>>> if rocket.position > event_horizon
  File "<stdin>", line 1
    if rocket.position > event_horizon
                                      ^
SyntaxError: expected ':'

```

> (Contributed by Pablo Galindo in [bpo-42997](https://bugs.python.org/issue?@action=redirect&bpo=42997).)

-

[Subject index](INDEX.md) · [Previous source section](parenthesized-context-managers.md) · [Next source section](comprehension-tuple-syntax-diagnostics.md) · [Release/subject declaration](summary-release-highlights.md)
