# doctest: `doctest.script_from_examples()`, `doctest.testsource()`, `doctest.debug()`, `doctest.debug_src()`

doctest.script_from_examples(*s*)

Turn example-bearing text into a script.

The *s* argument is a string holding doctest examples. That string becomes a Python script in which the doctest examples within *s* turn into ordinary code while everything else turns into Python comments. The script produced is handed back as a string. To illustrate,

```python
import doctest
print(doctest.script_from_examples(r"""
    Set x and y to 1 and 2.
    >>> x, y = 1, 2

    Print their sum:
    >>> print(x+y)
    3
"""))

```

displays:

```python
# Set x and y to 1 and 2.
x, y = 1, 2
#
# Print their sum:
print(x+y)
# Expected:
## 3

```

Other functions call on this one behind the scenes (as shown below), yet it can also serve you directly whenever you wish to convert an interactive Python session into a Python script.

 doctest.testsource(*module*, *name*)

Render an object's doctest as a script.

The *module* argument is a module object — or the dotted name of one — that contains the object whose doctests you care about. The *name* argument is that object's name within the module. What comes back is a string, holding the object's docstring rendered into a Python script just as `script_from_examples()` described above. As an example, should the module `a.py` hold a top-level function `f()`, then

```python
import a, doctest
print(doctest.testsource(a, "a.f"))

```

writes out a scripted form of the `f()` function's docstring, its doctests rendered as code and the remainder dropped into comments.

 doctest.debug(*module*, *name*, *pm=False*)

Run an object's doctests under the debugger.

Both the *module* and *name* arguments carry the same meaning they had for the `testsource()` function above. The Python script built from the named object's docstring is saved to a temporary file, which is then executed beneath the Python debugger, [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb).

For both the local and global execution context, a shallow copy of `module.__dict__` is employed.

Whether post-mortem debugging happens is governed by the optional *pm* argument. Give *pm* a true value and the script file executes outright, with the debugger stepping in only should the script die from an unhandled exception; when that occurs, post-mortem debugging starts up through [`pdb.post_mortem()`](https://docs.python.org/3.14/library/pdb.html#pdb.post_mortem), which is fed the traceback object of that unhandled exception. Leave *pm* unset or false, and the script runs beneath the debugger right from the outset, by way of a suitable [`exec()`](https://docs.python.org/3.14/library/functions.html#exec) call passed to [`pdb.run()`](https://docs.python.org/3.14/library/pdb.html#pdb.run).

 doctest.debug_src(*src*, *pm=False*, *globs=None*)

Run the doctests contained in a string under the debugger.

It mirrors the `debug()` function above, save that you supply a string of doctest examples straight away through the *src* argument.

The optional *pm* argument carries the very meaning it holds in the `debug()` function above.

The optional *globs* argument provides a dictionary serving as both the local and global execution context. Leave it out or pass `None` and an empty dictionary is used; supply one and a shallow copy of that dictionary is used.

The `DebugRunner` class together with the special exceptions it can raise matter mainly to authors of testing frameworks, so they get only an outline here. For the full picture, consult the source code and above all the `DebugRunner` docstring — which is itself a doctest!:

[Subject index](INDEX.md) · [Previous](debugging.md) · [Continue](doctest-debugrunner-class.md) · [Owning module, declaration or section: doctest](interactive-example-testing-overview.md) · [Owning module, declaration or section: Debugging](debugging.md)
