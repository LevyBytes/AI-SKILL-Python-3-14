# What's New In Python 3.10 / Better error messages / NameErrors

#### NameErrors

While rendering a [`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError) thrown by the interpreter, `PyErr_Display()` will propose similar variable names drawn from the function where the exception arose:

```python
>>> schwarzschild_black_hole = None
>>> schwarschild_black_hole
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'schwarschild_black_hole' is not defined. Did you mean: schwarzschild_black_hole?

```

> (Contributed by Pablo Galindo in [bpo-38530](https://bugs.python.org/issue?@action=redirect&bpo=38530).)

Warning

Be aware this has no effect when `PyErr_Display()` is bypassed during error display, which can occur when some alternative custom error display routine takes over. You'll run into this often with certain REPLs such as IPython.

[Subject index](INDEX.md) · [Previous source section](better-error-messages-attributeerrors.md) · [Next source section](pep-626-precise-line-numbers-for-debugging-and-other-tools.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](better-error-messages-syntaxerrors-syntaxerrors.md)
