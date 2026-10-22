# Python 3.10 changes: Assignment-versus-comparison syntax diagnostics

```python
>>> try:
...     x = 2
... something = 3
  File "<stdin>", line 3
    something  = 3
    ^^^^^^^^^
SyntaxError: expected 'except' or 'finally' block

```

> (Contributed by Pablo Galindo in [bpo-44305](https://bugs.python.org/issue?@action=redirect&bpo=44305).)

- Usage of `=` instead of `==` in comparisons:

```python
>>> if rocket.position = event_horizon:
  File "<stdin>", line 1
    if rocket.position = event_horizon:
                       ^
SyntaxError: cannot assign to attribute here. Maybe you meant '==' instead of '='?

```

> (Contributed by Pablo Galindo in [bpo-43797](https://bugs.python.org/issue?@action=redirect&bpo=43797).)

- Usage of `*` in f-strings:

```python
>>> f"Black holes {*all_black_holes} and revelations"
  File "<stdin>", line 1
    (*all_black_holes)
     ^
SyntaxError: f-string: cannot use starred expression here

```

[Subject index](INDEX.md) · [Previous source section](comprehension-tuple-syntax-diagnostics.md) · [Next source section](better-error-messages-indentationerrors.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](better-error-messages-syntaxerrors-syntaxerrors.md)
