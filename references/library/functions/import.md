# Built-in Functions

__import__(*name*, *globals=None*, *locals=None*, *fromlist=()*, *level=0*)

Note

Unlike [`importlib.import_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.import_module), this is a low-level function that ordinary day-to-day Python work has no call for.

The [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) statement calls this function. You can swap it out — by importing the [`builtins`](https://docs.python.org/3.14/library/builtins.html#module-builtins) module and assigning to `builtins.__import__` — so as to alter the behavior of the `import` statement, yet this is **strongly** discouraged, since reaching for import hooks (see [**PEP 302**](https://peps.python.org/pep-0302/)) is normally the easier route to the same ends and avoids breaking code that relies on the default import implementation being active. Calling `__import__()` directly is likewise discouraged, with [`importlib.import_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.import_module) preferred instead.

This function brings in the module *name*, possibly drawing on the supplied *globals* and *locals* to work out how the name should be read within a package context. The *fromlist* supplies the names of objects or submodules to pull from the module identified by *name*. In the standard implementation the *locals* argument is ignored entirely, while *globals* serves solely to establish the package context of the [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) statement.

The *level* argument selects between absolute and relative imports. A value of `0` (the default) restricts the operation to absolute imports alone. When *level* is positive, it tells how many parent directories to look through, counted relative to the directory holding the module that called `__import__()` (consult [**PEP 328**](https://peps.python.org/pep-0328/) for the specifics).

Should the *name* variable take the shape `package.module`, what comes back by default is the top-level package (the portion of the name preceding the first dot), *not* the module that *name* designates. Supply a non-empty *fromlist* argument, though, and the module designated by *name* is returned instead.

To illustrate, the `import spam` statement yields bytecode that resembles this:

```python
spam = __import__('spam', globals(), locals(), [], 0)

```

Meanwhile the `import spam.ham` statement produces the following call:

```python
spam = __import__('spam.ham', globals(), locals(), [], 0)

```

Observe that `__import__()` hands back the toplevel module in this case, since that is precisely the object the [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) statement binds to a name.

By contrast, the `from spam.ham import eggs, sausage as saus` statement gives

```python
_temp = __import__('spam.ham', globals(), locals(), ['eggs', 'sausage'], 0)
eggs = _temp.eggs
saus = _temp.sausage

```

In this case `__import__()` returns the `spam.ham` module, and the names being imported are then pulled off that object and bound to their corresponding names.

When all you need is to load a module by name (perhaps one nested inside a package), reach for [`importlib.import_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.import_module).

Changed in version 3.3: Support for negative *level* values was dropped (and the default was shifted to 0 as part of this).

Changed in version 3.9: Whenever the [`-E`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-E) or [`-I`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-I) command line options are in effect, the [`PYTHONCASEOK`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONCASEOK) environment variable is now disregarded.

Footnotes

[Subject index](INDEX.md) · [Previous](zip.md) · [Owning module, declaration or section: Built-in Functions](INDEX.md)
