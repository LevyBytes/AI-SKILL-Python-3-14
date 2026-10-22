# What’s New In Python 3.12 / Improved Error Messages

### Improved Error Messages

- When a [`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError) reaches the top level, the interpreter may now point to standard-library modules within the error text it shows. (Contributed by Pablo Galindo in [gh-98254](https://github.com/python/cpython/issues/98254).)

```python
>>> sys.version_info
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sys' is not defined. Did you forget to import 'sys'?

```

- Sharpen the hint given for [`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError) exceptions on instances. From now on, when a `NameError` fires inside a method and the instance carries an attribute matching the name in the exception exactly, the proposal points to `self.<NAME>` rather than the nearest match within the method scope. (Contributed by Pablo Galindo in [gh-99139](https://github.com/python/cpython/issues/99139).)

```python
>>> class A:
...    def __init__(self):
...        self.blech = 1
...
...    def foo(self):
...        somethin = blech
...
>>> A().foo()
Traceback (most recent call last):
  File "<stdin>", line 1
    somethin = blech
               ^^^^^
NameError: name 'blech' is not defined. Did you mean: 'self.blech'?

```

- Sharpen the [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) message shown when someone writes `import x from y` rather than `from y import x`. (Contributed by Pablo Galindo in [gh-98931](https://github.com/python/cpython/issues/98931).)

```python
>>> import a.y.z from b.y.z
Traceback (most recent call last):
  File "<stdin>", line 1
    import a.y.z from b.y.z
    ^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: Did you mean to use 'from ... import ...' instead?

```

- For a failed `from <module> import <name>` statement, the resulting [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) now proposes a value for `<name>` drawn from the names that `<module>` makes available. (Contributed by Pablo Galindo in [gh-91058](https://github.com/python/cpython/issues/91058).)

```python
>>> from collections import chainmap
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'chainmap' from 'collections'. Did you mean: 'ChainMap'?

```

[Subject index](INDEX.md) · [Previous source section](pep-709-comprehension-inlining.md) · [Next source section](new-features-related-to-type-hints.md) · [Release/subject declaration](summary-release-highlights.md)
