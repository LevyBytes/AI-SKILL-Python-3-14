# doctest.DocTestFinder: `find()`

A worker class that pulls the `DocTest`s pertaining to some object out of its docstring along with the docstrings belonging to objects nested inside it. Modules, classes, functions, methods, staticmethods, classmethods, and properties are all valid sources from which `DocTest`s may be drawn.

Setting the optional *verbose* argument makes the finder show which objects it searched. Its default is `False`, meaning nothing is printed.

Through the optional *parser* argument you name the `DocTestParser` object — or any drop-in stand-in — that handles pulling doctests out of docstrings.

Should the optional *recurse* argument be false, `DocTestFinder.find()` looks at the supplied object alone and skips any objects nested within it.

When the optional *exclude_empty* argument is false, `DocTestFinder.find()` keeps tests even for objects whose docstrings are empty.

`DocTestFinder` defines the following method:

 find(*obj[, name][, module][, globs][, extraglobs]*)

Hand back a list of every `DocTest` defined either in *obj*'s docstring or in the docstrings of objects nested inside it.

The optional *name* argument gives the object's name, which then seeds the names built for the `DocTest`s that come back. Leave *name* out and `obj.__name__` is used instead.

The optional *module* parameter names the module in which the supplied object lives. Where it is omitted or `None`, the test finder tries to work out the right module on its own. The object's module serves these purposes:

- Serving as the fallback namespace whenever *globs* is left unspecified.

- Stopping the DocTestFinder from pulling DocTests out of objects brought in from other modules. (Nested objects whose module differs from *module* get skipped.)

- Locating the name of the file in which the object resides.

- Assisting in pinpointing the object's line number inside its file.

Pass *module* as `False` and no effort is made to locate the module. That is an obscure option, handy chiefly when testing doctest itself: with *module* set to `False`, or set to `None` yet impossible to detect automatically, every object is treated as a member of the (nonexistent) module, and so all nested objects are searched recursively for doctests.

Each `DocTest`'s globals come from merging *globs* with *extraglobs*, where bindings in *extraglobs* take precedence over those in *globs*. Every `DocTest` gets its own fresh shallow copy of the globals dictionary. Omit *globs* and it falls back to the module's [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#module.__dict__) when that exists, or to `{}` otherwise; omit *extraglobs* and it falls back to `{}`.

[Subject index](INDEX.md) · [Continue](doctest-doctestparser-class.md) · [Owning module, declaration or section: doctest](interactive-example-testing-overview.md) · [Owning module, declaration or section: doctest.DocTestFinder](doctest-doctestfinder-class.md) · [Owning module, declaration or section: DocTestFinder objects](doctest-doctestfinder-class.md) · [Preceding source contract and version conditions](doctest-doctestfinder-class.md)
