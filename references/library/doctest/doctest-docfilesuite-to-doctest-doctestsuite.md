# doctest: `doctest.DocFileSuite()`, `doctest.DocTestSuite()`

### Unittest API

As the set of modules carrying doctests you maintain expands, you will want some means of running every one of their doctests in a systematic way. `doctest` supplies two functions for building [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) test suites out of modules and out of text files that hold doctests. So that they fit into `unittest` test discovery, add a [load_tests](https://docs.python.org/3.14/library/unittest.html#load-tests-protocol) function to your test module:

```python
import unittest
import doctest
import my_module_with_doctests

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(my_module_with_doctests))
    return tests

```

Two principal functions exist for assembling [`unittest.TestSuite`](https://docs.python.org/3.14/library/unittest.html#unittest.TestSuite) instances out of text files and out of modules that carry doctests:

 doctest.DocFileSuite(**paths*, *module_relative=True*, *package=None*, *setUp=None*, *tearDown=None*, *globs=None*, *optionflags=0*, *parser=DocTestParser()*, *encoding=None*)

Turn doctest tests drawn from one or more text files into a [`unittest.TestSuite`](https://docs.python.org/3.14/library/unittest.html#unittest.TestSuite).

The [`unittest.TestSuite`](https://docs.python.org/3.14/library/unittest.html#unittest.TestSuite) that comes back is meant to be driven by the unittest framework, and it runs the interactive examples found in each file. Should any example in any file fail, the synthesized unit test fails too, and a [`failureException`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.failureException) exception is raised that shows the name of the file holding the test together with a (sometimes approximate) line number. When every example within a file is skipped, the synthesized unit test ends up marked skipped as well.

Hand in one or more paths (as strings) to the text files you want examined.

You may supply options as keyword arguments:

The optional *module_relative* argument governs how the filenames in *paths* are read:

- When *module_relative* is `True` (the default), each filename in *paths* names an OS-independent module-relative path. That path defaults to being relative to the directory of the calling module; however, when the *package* argument is given, it becomes relative to that package instead. For OS-independence, every filename ought to use `/` characters between path segments, and it must not be an absolute path (that is, it must not start with `/`).

- When *module_relative* is `False`, each filename in *paths* names an OS-specific path. Such a path may be either absolute or relative; relative ones are resolved against the current working directory.

The optional *package* argument is a Python package, or the name of one, whose directory acts as the base directory for module-relative filenames in *paths*. When no package is given, the directory of the calling module becomes the base directory for module-relative filenames. Supplying *package* when *module_relative* is `False` is an error.

The optional *setUp* argument names a set-up function for the test suite. It runs ahead of the tests in each file. A `DocTest` object is passed to the *setUp* function. That *setUp* function can reach the test globals through the `globs` attribute of the test handed to it.

The optional *tearDown* argument names a tear-down function for the test suite. It runs after the tests in each file. A `DocTest` object is passed to the *tearDown* function. That *tearDown* function can reach the test globals through the `globs` attribute of the test handed to it.

The optional *globs* argument is a dictionary holding the starting global variables for the tests. A new copy of that dictionary is made for each test. By default, *globs* is a new empty dictionary.

The optional *optionflags* argument sets the default doctest options for the tests, formed by or-ing the individual option flags together. Consult the Option Flags section. See function `set_unittest_reportflags()` below for a superior way to configure reporting options.

The optional *parser* argument names a `DocTestParser` (or subclass) to be used for pulling tests out of the files. It defaults to an ordinary parser (that is, `DocTestParser()`).

The optional *encoding* argument names an encoding to be used when converting the file to unicode.

The global `__file__` gets added to the globals handed to doctests loaded from a text file via `DocFileSuite()`.

 doctest.DocTestSuite(*module=None*, *globs=None*, *extraglobs=None*, *test_finder=None*, *setUp=None*, *tearDown=None*, *optionflags=0*, *checker=None*)

Turn doctest tests for a module into a [`unittest.TestSuite`](https://docs.python.org/3.14/library/unittest.html#unittest.TestSuite).

The [`unittest.TestSuite`](https://docs.python.org/3.14/library/unittest.html#unittest.TestSuite) that comes back is meant to be driven by the unittest framework, and it runs each doctest in the module. Every docstring runs as its own separate unit test. Should any of the doctests fail, the synthesized unit test fails too, and a [`unittest.TestCase.failureException`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.failureException) exception gets raised, naming the file that holds the test along with an (occasionally rough) line number. When every one of the examples within a docstring gets skipped, the

The optional *module* argument supplies the module to be tested. It may be a module object or a (possibly dotted) module name. When left unspecified, the module that called this function is used.

The optional *globs* argument is a dictionary holding the starting global variables for the tests. A new copy of that dictionary is made for each test. By default, *globs* is the module's [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#module.__dict__).

The optional *extraglobs* argument supplies an additional set of global variables that gets merged into *globs*. By default, no extra globals are used.

The optional *test_finder* argument is the `DocTestFinder` object (or a drop-in replacement) employed to pull doctests out of the module.

The optional *setUp*, *tearDown*, and *optionflags* arguments are the same as for function `DocFileSuite()` above, though here they are invoked for each docstring.

This function relies on the same search technique as `testmod()`.

Changed in version 3.5: `DocTestSuite()` returns an empty [`unittest.TestSuite`](https://docs.python.org/3.14/library/unittest.html#unittest.TestSuite) when *module* holds no docstrings, rather than raising [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

Behind the scenes, `DocTestSuite()` builds a [`unittest.TestSuite`](https://docs.python.org/3.14/library/unittest.html#unittest.TestSuite) from `doctest.DocTestCase` instances, and `DocTestCase` is a subclass of [`unittest.TestCase`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase). `DocTestCase` is not documented here (it counts as an internal detail), but reading its code can resolve questions about the precise specifics of [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) integration.

In the same fashion, `DocFileSuite()` builds a [`unittest.TestSuite`](https://docs.python.org/3.14/library/unittest.html#unittest.TestSuite) from `doctest.DocFileCase` instances, and `DocFileCase` is a subclass of `DocTestCase`.

Hence both routes to creating a [`unittest.TestSuite`](https://docs.python.org/3.14/library/unittest.html#unittest.TestSuite) run instances of `DocTestCase`. That matters for a subtle reason: when you call `doctest` functions on your own, you can govern the `doctest` options in force directly, by handing option flags to `doctest` functions. Yet when you write a [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) framework, it is `unittest` that ultimately decides when and how the tests run. Typically the framework author wishes to govern `doctest` reporting options (say, e.g., as set by command line options), but no mechanism exists for routing options through `unittest` down to the `doctest` test runners.

On account of this, `doctest` additionally provides a concept of `doctest` reporting flags tailored to [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) support, through this function:

[Subject index](INDEX.md) · [Previous](doctest-testfile-to-doctest-run-docstring-examples.md) · [Continue](doctest-set-unittest-reportflags.md) · [Owning module, declaration or section: doctest](interactive-example-testing-overview.md)
