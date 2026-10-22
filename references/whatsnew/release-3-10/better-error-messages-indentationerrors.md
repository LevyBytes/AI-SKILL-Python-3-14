# What's New In Python 3.10 / Better error messages / IndentationErrors

> (Contributed by Pablo Galindo in [bpo-41064](https://bugs.python.org/issue?@action=redirect&bpo=41064).)

#### IndentationErrors

A large number of [`IndentationError`](https://docs.python.org/3.14/library/exceptions.html#IndentationError) exceptions now carry richer context about which sort of block was anticipating indentation, along with where the statement sits:

```python
>>> def foo():
...    if lel:
...    x = 2
  File "<stdin>", line 3
    x = 2
    ^
IndentationError: expected an indented block after 'if' statement in line 2

```

[Subject index](INDEX.md) · [Previous source section](comparison-operator-syntax-diagnostics.md) · [Next source section](better-error-messages-attributeerrors.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](better-error-messages-syntaxerrors-syntaxerrors.md)
