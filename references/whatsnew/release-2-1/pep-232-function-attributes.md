# What’s New in Python 2.1 / PEP 232: Function Attributes

### PEP 232: Function Attributes

Under Python 2.1, you can now hang arbitrary information off of functions. People had often pressed docstrings into service to store details about functions and methods, since the [`__doc__`](https://docs.python.org/3.14/reference/datamodel.html#function.__doc__) attribute was the sole avenue for attaching any data to a function. In the Zope web application server, for instance, functions get flagged as safe for public access by carrying a docstring, while in John Aycock’s SPARK parsing framework, docstrings carry portions of the BNF grammar awaiting parsing. Such overloading is regrettable, given that docstrings are genuinely meant to hold a function’s documentation; it means, for one, that you cannot properly document functions intended for private use within Zope.

You can now assign and read back arbitrary attributes on functions through ordinary Python syntax:

```python
def f(): pass

f.publish = 1
f.secure = 1
f.grammar = "A ::= B (C D)*"

```

The dictionary holding these attributes is reachable as the function’s [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#function.__dict__). In contrast to the [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#type.__dict__) attribute on class instances, with functions you really can assign a brand-new dictionary to `__dict__`, though the value you assign must be a plain Python dictionary; you *can’t* get clever and set it to a `UserDict` instance, or to any other arbitrary object that mimics a mapping.

See also

[**PEP 232**](https://peps.python.org/pep-0232/) - Function Attributes

Written and implemented by Barry Warsaw.

[Subject index](INDEX.md) · [Previous source section](pep-205-weak-references.md) · [Next source section](pep-235-importing-modules-on-case-insensitive-platforms.md) · [Release/subject declaration](introduction.md)
