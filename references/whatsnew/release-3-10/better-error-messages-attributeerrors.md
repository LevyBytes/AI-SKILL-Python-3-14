# What's New In Python 3.10 / Better error messages / AttributeErrors

#### AttributeErrors

While rendering [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError), `PyErr_Display()` will propose comparable attribute names found on the object from which the exception originated:

```python
>>> collections.namedtoplo
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'collections' has no attribute 'namedtoplo'. Did you mean: namedtuple?

```

> (Contributed by Pablo Galindo in [bpo-38530](https://bugs.python.org/issue?@action=redirect&bpo=38530).)

Warning

Be aware this has no effect when `PyErr_Display()` is bypassed during error display, which can occur when some alternative custom error display routine takes over. You'll run into this often with certain REPLs such as IPython.

[Subject index](INDEX.md) · [Previous source section](better-error-messages-indentationerrors.md) · [Next source section](better-error-messages-nameerrors.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](better-error-messages-syntaxerrors-syntaxerrors.md)
