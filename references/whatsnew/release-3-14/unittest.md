# What's new in Python 3.14 / unittest — unittest

### unittest

- By default, [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) output is now colored. You can govern this through [environment variables](https://docs.python.org/3.14/using/cmdline.html#using-on-controlling-color). (Contributed by Hugo van Kemenade in [gh-127221](https://github.com/python/cpython/issues/127221).)

- Discovery in unittest once more accepts a [namespace package](https://docs.python.org/3.14/glossary.html#term-namespace-package) for its start directory. That capability had been dropped back in Python 3.11. (Contributed by Jacob Walls in [gh-80958](https://github.com/python/cpython/issues/80958).)

- Several fresh methods landed in the [`TestCase`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase) class to deliver more specialized assertions.

  - [`assertHasAttr()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertHasAttr) and [`assertNotHasAttr()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertNotHasAttr) verify whether a given object carries a specific attribute.

  - [`assertIsSubclass()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertIsSubclass) and [`assertNotIsSubclass()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertNotIsSubclass) verify whether an object is a subclass of some class, or of one among a tuple of classes.

  - [`assertStartsWith()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertStartsWith), [`assertNotStartsWith()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertNotStartsWith), [`assertEndsWith()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertEndsWith) and [`assertNotEndsWith()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertNotEndsWith) verify whether a Unicode or byte string begins or finishes with specified strings.

(Contributed by Serhiy Storchaka in [gh-71339](https://github.com/python/cpython/issues/71339).)

[Subject index](INDEX.md) · [Previous source section](unicodedata.md) · [Next source section](urllib.md) · [Release/subject declaration](summary-release-highlights.md)
