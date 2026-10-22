# What’s New in Python 2.3 / Porting to Python 2.3

### Porting to Python 2.3

This section enumerates previously covered changes that might call for adjustments to your code:

- [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield) is now invariably a keyword; should it appear as a variable name in your code, you must pick a different name.

- For strings *X* and *Y*, `X in Y` now works when *X* is longer than a single character.

- When a string or floating-point number is too large to fit inside an integer, the [`int()`](https://docs.python.org/3.14/library/functions.html#int) type constructor now hands back a long integer rather than raising an [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError).

- If your Unicode strings hold 8-bit characters, you must state the file's encoding (UTF-8, Latin-1, or otherwise) by inserting a comment at the top of the file. Consult the section PEP 263: Source Code Encodings for additional information.

- Calling Tcl methods via `_tkinter` no longer hands back nothing but strings. Instead, when Tcl returns other objects, those objects are translated into their Python counterpart, if one exists, or wrapped in a `_tkinter.Tcl_Obj` object when no Python counterpart exists.

- Large octal and hex literals like `0xffffffff` now raise a [`FutureWarning`](https://docs.python.org/3.14/library/exceptions.html#FutureWarning). For now they're held as 32-bit numbers and yield a negative value, but in Python 2.4 they'll turn into positive long integers.

You have a couple of options for silencing this warning. If you genuinely want a positive number, simply append an `L` to the literal. If your aim is a 32-bit integer with low bits set and you've formerly written an expression such as `~(1 << 31)`, it's likely cleanest to begin with every bit set and then clear the upper bits you don't want. For example, to clear only the top bit (bit 31), you could write `0xffffffffL &~(1L<<31)`.

- Assigning to `__debug__` to turn off assertions is no longer permitted.

- The Distutils `setup()` function has picked up several new keyword arguments, among them *depends*. Older versions of the Distutils will fail if given unfamiliar keywords. One workaround is to test for the presence of the new `get_distutil_options()` function in your `setup.py` and only employ the new keywords with a Distutils version that supports them:

```python
from distutils import core

kw = {'sources': 'foo.c', ...}
if hasattr(core, 'get_distutil_options'):
    kw['depends'] = ['foo.h']
ext = Extension(**kw)

```

- Using `None` as a variable name will now produce a [`SyntaxWarning`](https://docs.python.org/3.14/library/exceptions.html#SyntaxWarning) warning.

-

For extension types that ship in Python's bundled modules, the reported name is now prefixed with the originating module followed by a `'.'` before the actual type name.

[Subject index](INDEX.md) · [Previous source section](other-changes-and-fixes.md) · [Release/subject declaration](standard-set-type.md) · [Next source section](acknowledgements.md)
