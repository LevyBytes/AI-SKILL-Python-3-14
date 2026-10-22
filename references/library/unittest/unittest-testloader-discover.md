# unittest: `discover()`

discover(*start_dir*, *pattern='test*.py'*, *top_level_dir=None*)

Locate every test module by descending through subdirectories beneath the given start directory, and yield a TestSuite object that holds them. Only test files matching *pattern* get loaded. (Shell-style pattern matching is used.) Only module names that can be imported (that is, valid Python identifiers) get loaded.

Every test module has to be importable from the project's top level. When the start directory differs from the top level directory, then *top_level_dir* has to be given on its own.

When importing a module fails, say from a syntax error, that gets logged as one error and discovery keeps going. When the import failure stems from `SkipTest` being raised, it gets logged as a skip rather than an error.

When a package (a directory holding a file called `__init__.py`) turns up, that package gets checked for a `load_tests` function. Where one exists it gets invoked as `package.load_tests(loader, tests, pattern)`. Test discovery is careful to guarantee a package is checked for tests only once per invocation, even when the load_tests function itself invokes `loader.discover`.

Where `load_tests` exists, discovery does *not* descend into the package; `load_tests` takes on loading every test in the package.

The pattern is intentionally kept off the loader as an attribute so packages can carry on discovery on their own.

*top_level_dir* gets kept internally and serves as a default for any nested `discover()` calls. That is, when a package’s `load_tests` invokes `loader.discover()`, passing this argument is unnecessary.

*start_dir* may be a dotted module name in addition to a directory.

Added in version 3.2.

Changed in version 3.4: A module raising `SkipTest` during import is logged as a skip rather than an error.

*start_dir* can be a [namespace packages](https://docs.python.org/3.14/glossary.html#term-namespace-package).

Paths get sorted ahead of import so the run order stays consistent even when the underlying file system’s ordering does not hinge on file name.

Changed in version 3.5: Discovered packages now get inspected for `load_tests` whether or not their path lines up with *pattern*, since a package name can never satisfy the default pattern.

Changed in version 3.11: *start_dir* can not be a [namespace packages](https://docs.python.org/3.14/glossary.html#term-namespace-package). This had been broken ever since Python 3.7, and Python 3.11 formally drops it.

Changed in version 3.13: *top_level_dir* gets retained only for the span of the *discover* call.

Changed in version 3.14: *start_dir* may yet again be a [namespace package](https://docs.python.org/3.14/glossary.html#term-namespace-package).

These attributes of a `TestLoader` can be set up either through subclassing or by assignment on an instance:

 testMethodPrefix

A string holding the prefix of method names that get treated as test methods. Its default value is `'test'`.

This affects `getTestCaseNames()` and all the `loadTestsFrom*` methods.

 sortTestMethodsUsing

The function used to compare method names while sorting them within `getTestCaseNames()` and all the `loadTestsFrom*` methods.

 suiteClass

A callable object that assembles a test suite from a list of tests. The object it returns needs no methods. Its default value is the `TestSuite` class.

This affects all the `loadTestsFrom*` methods.

 testNamePatterns

A list of Unix shell-style wildcard test name patterns that test methods must match for inclusion in test suites (see the `-k` option).

Unless this attribute is `None` (the default), every test method bound for a test suite has to match one of the patterns in the list. Bear in mind that matching always goes through [`fnmatch.fnmatchcase()`](https://docs.python.org/3.14/library/fnmatch.html#fnmatch.fnmatchcase), so unlike patterns handed to the `-k` option, plain substring patterns will need converting with `*` wildcards.

This affects all the `loadTestsFrom*` methods.

Added in version 3.7.

[Subject index](INDEX.md) · [Previous](test-loader-case-and-method-discovery.md) · [Continue](unittest-testresult-class-to-unittest-testresult-starttest.md) · [Owning module, declaration or section: unittest.TestLoader](unittest-testloader-class.md) · [Owning module, declaration or section: Loading and running tests](unittest-testloader-class.md)
