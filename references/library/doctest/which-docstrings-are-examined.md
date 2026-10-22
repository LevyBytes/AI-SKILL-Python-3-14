# doctest — Which Docstrings Are Examined?

### Which Docstrings Are Examined?

Searching covers the module docstring plus every function, class, and method docstring. Anything imported into the module gets skipped.

Beyond that, there are situations where you'd like the tests bundled with a module yet kept out of the help text, which means those tests must stay outside the docstring. Doctest watches for a module-level variable named `__test__` and consults it to track down additional tests. Whenever `M.__test__` is present, it has to be a dict, with each entry pairing a (string) name to a function object, class object, or string. Docstrings discovered on function and class objects reached through `M.__test__` get searched, while strings are handled as though they themselves were docstrings. Within the output, a key `K` from `M.__test__` shows up bearing the name `M.__test__.K`.

To illustrate, drop this snippet at the head of `example.py`:

```python
__test__ = {
    'numbers': """
>>> factorial(6)
720

>>> [factorial(n) for n in range(6)]
[1, 1, 2, 6, 24, 120]
"""
}

```

Whatever sits in `example.__test__["numbers"]` is handled as a docstring, and every test found within it gets executed. Worth stressing: that value may instead point to a function, class object, or module; should that be the case, `doctest` walks them recursively in search of docstrings, which then get scanned for tests.

Whatever classes turn up are likewise walked recursively in the same manner, so that docstrings in their member methods and nested classes get tested.

Note

`doctest` is only able to automatically locate classes and functions declared at module level or sitting inside other classes.

Because nested classes and functions come into being only once an enclosing function runs, they evade discovery. Move them to the outer scope to make them findable.

[Subject index](INDEX.md) · [Previous](how-it-works.md) · [Continue](how-are-docstring-examples-recognized.md) · [Owning module, declaration or section: doctest](interactive-example-testing-overview.md)
