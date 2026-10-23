# doctest - Basic API

### Basic API

`testmod()` and `testfile()` give you a straightforward way into doctest that will cover most ordinary needs. For a gentler walkthrough of this pair of functions, refer to the sections `Simple Usage: Checking Examples in Docstrings` and `Simple Usage: Checking Examples in a Text File`.

 `doctest.testfile(*filename*, *module_relative=True*, *name=None*, *package=None*, *globs=None*, *verbose=None*, *report=True*, *optionflags=0*, *extraglobs=None*, *raise_on_error=False*, *parser=DocTestParser()*, *encoding=None*)`

Every argument apart from *filename* is optional and ought to be passed by keyword.

Run the examples in the file called *filename*. Return `(failure_count, test_count)`.

The optional *module_relative* argument governs how the filename is read:

- When *module_relative* is `True` (the default), *filename* names an OS-independent module-relative path. That path defaults to being relative to the directory of the calling module; however, when the *package* argument is given, it becomes relative to that package instead. For OS-independence, *filename* ought to use `/` characters between path segments, and it must not be an absolute path (that is, it must not start with `/`).

- When *module_relative* is `False`, *filename* names an OS-specific path. Such a path may be either absolute or relative; relative ones are resolved against the current working directory.

The optional *name* argument supplies the test's name; by default, or when `None`, `os.path.basename(filename)` serves instead.

The optional *package* argument is a Python package, or the name of one, whose directory acts as the base directory for a module-relative filename. When no package is given, the directory of the calling module becomes the base directory for module-relative filenames. Supplying *package* when *module_relative* is `False` is an error.

The optional *globs* argument provides a dict to serve as the globals while examples run. A fresh shallow copy of that dict is made for the doctest, so its examples begin with a clean slate. By default, or when `None`, a new empty dict is used.

The optional *extraglobs* argument provides a dict that gets merged into the globals used while running examples. It behaves like [`dict.update()`](https://docs.python.org/3.14/library/stdtypes.html#dict.update): when *globs* and *extraglobs* share a key, the value from *extraglobs* wins in the merged dict. By default, or when `None`, no extra globals come into play. This advanced capability permits doctests to be parameterized. As an illustration, you can author a doctest against a base class using a generic class name, then reuse it to exercise any number of subclasses by handing in an *extraglobs* dict that maps the generic name onto the subclass under test.

The optional *verbose* argument prints a great deal of detail when true and only failures when false; by default, or when `None`, it is true exactly when `'-v'` appears in [`sys.argv`](https://docs.python.org/3.14/library/sys.html#sys.argv).

The optional *report* argument prints a closing summary when true, and prints nothing at the close otherwise. With verbose mode on, that summary is thorough; otherwise it is extremely terse (indeed empty when every test passed).

The optional *optionflags* argument (default value `0`) accepts the [bitwise OR](https://docs.python.org/3.14/reference/expressions.html#bitwise) of option flags. Consult the Option Flags section.

The optional *raise_on_error* argument defaults to false. When true, an exception gets raised at the first failure or unexpected exception in an example. This lets failures be debugged post-mortem. The default conduct is to keep running examples.

The optional *parser* argument names a `DocTestParser` (or subclass) to be used for pulling tests out of the files. It defaults to an ordinary parser (that is, `DocTestParser()`).

The optional *encoding* argument names an encoding to be used when converting the file to unicode.

 `doctest.testmod(*m=None*, *name=None*, *globs=None*, *verbose=None*, *report=True*, *optionflags=0*, *extraglobs=None*, *raise_on_error=False*, *exclude_empty=False*)`

All of the arguments are optional, and all but *m* ought to be passed by keyword.

Run the examples in docstrings of functions and classes reachable from module *m* (or module [`__main__`](https://docs.python.org/3.14/library/__main__.html#module-__main__) when *m* is not given or is `None`), beginning with `m.__doc__`.

It also runs examples reachable through dict `m.__test__`, when that exists. `m.__test__` maps names (strings) onto functions, classes, and strings; docstrings of functions and classes are scanned for examples, while strings are scanned directly, as though they were docstrings.

Only docstrings attached to objects that belong to module *m* get scanned.

Return `(failure_count, test_count)`.

The optional *name* argument supplies the module's name; by default, or when `None`, `m.__name__` serves instead.

The optional *exclude_empty* argument defaults to false. When true, objects that turn up no doctests are dropped from consideration. This default is a backward-compatibility hack, so that code still relying on `doctest.master.summarize` together with `testmod()` keeps producing output for objects that have no tests. On the newer `DocTestFinder` constructor, the *exclude_empty* argument defaults to true.

The optional *extraglobs*, *verbose*, *report*, *optionflags*, *raise_on_error*, and *globs* arguments behave just as they do for function `testfile()` above, except that here *globs* defaults to `m.__dict__`.

 doctest.run_docstring_examples(*f*, *globs*, *verbose=False*, *name='NoName'*, *compileflags=None*, *optionflags=0*)

Run the examples tied to object *f*; for instance, *f* might be a string, a module, a function, or a class object.

A shallow copy of the dictionary argument *globs* serves as the execution context.

The optional *name* argument appears in failure messages and defaults to `"NoName"`.

When the optional *verbose* argument is true, output gets produced even where there are no failures. By default, output appears only when an example fails.

The optional *compileflags* argument gives the collection of flags the Python compiler should apply while running the examples. By default, or when `None`, the flags are inferred to match the future features present in *globs*.

The optional *optionflags* argument behaves as it does for function `testfile()` above.

[Subject index](INDEX.md) · [Previous](warnings.md) · [Continue](doctest-docfilesuite-to-doctest-doctestsuite.md) · [Owning module, declaration or section: doctest](interactive-example-testing-overview.md)
