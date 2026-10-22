# What's New In Python 3.11 / Standard Library — configparser, importlib.resources, locale, re, turtle, typing

### Standard Library

- These items in [`configparser`](https://docs.python.org/3.14/library/configparser.html#module-configparser) have carried a deprecation since Python 3.2. Their warnings were refreshed to flag a Python 3.12 removal:

  - the `configparser.SafeConfigParser` class

  - the `configparser.ParsingError.filename` property

  - the `configparser.RawConfigParser.readfp()` method

(Contributed by Hugo van Kemenade in [bpo-45173](https://bugs.python.org/issue?@action=redirect&bpo=45173).)

- Since Python 3.2, `configparser.LegacyInterpolation` has been deprecated in its docstring and is absent from the [`configparser`](https://docs.python.org/3.14/library/configparser.html#module-configparser) documentation. It now raises a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) and is slated for removal in Python 3.13. Reach for [`configparser.BasicInterpolation`](https://docs.python.org/3.14/library/configparser.html#configparser.BasicInterpolation) or [`configparser.ExtendedInterpolation`](https://docs.python.org/3.14/library/configparser.html#configparser.ExtendedInterpolation) instead. (Contributed by Hugo van Kemenade in [bpo-46607](https://bugs.python.org/issue?@action=redirect&bpo=46607).)

- Because they cannot reach resources sitting in package subdirectories, the legacy batch of [`importlib.resources`](https://docs.python.org/3.14/library/importlib.resources.html#module-importlib.resources) functions were deprecated in favor of the Python 3.9 replacements and face removal in some later Python release:

  - `importlib.resources.contents()`

  - `importlib.resources.is_resource()`

  - `importlib.resources.open_binary()`

  - `importlib.resources.open_text()`

  - `importlib.resources.read_binary()`

  - `importlib.resources.read_text()`

  - `importlib.resources.path()`

- Deprecation has hit the [`locale.getdefaultlocale()`](https://docs.python.org/3.14/library/locale.html#locale.getdefaultlocale) function, with removal due in Python 3.15. Switch to the [`locale.setlocale()`](https://docs.python.org/3.14/library/locale.html#locale.setlocale), [`locale.getpreferredencoding(False)`](https://docs.python.org/3.14/library/locale.html#locale.getpreferredencoding) and [`locale.getlocale()`](https://docs.python.org/3.14/library/locale.html#locale.getlocale) functions instead. (Contributed by Victor Stinner in [gh-90817](https://github.com/python/cpython/issues/90817).)

- Deprecation has hit the `locale.resetlocale()` function, with removal due in Python 3.13. Switch to `locale.setlocale(locale.LC_ALL, "")` instead. (Contributed by Victor Stinner in [gh-90817](https://github.com/python/cpython/issues/90817).)

- Tighter constraints now govern numeric group references and group names within [regular expressions](https://docs.python.org/3.14/library/re.html#re-syntax). A numeric reference may now consist solely of ASCII digits, while a group name in [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) patterns and replacement strings is limited to ASCII letters, digits and underscores. At this stage a deprecation warning fires for syntax that breaks these rules. (Contributed by Serhiy Storchaka in [gh-91760](https://github.com/python/cpython/issues/91760).)

- Inside the [`re`](https://docs.python.org/3.14/library/re.html#module-re) module, the `re.template()` function plus its companion `re.TEMPLATE` and `re.T` flags are deprecated, given that they went undocumented and served no clear role. Removal is set for Python 3.13. (Contributed by Serhiy Storchaka and Miro Hrončok in [gh-92728](https://github.com/python/cpython/issues/92728).)

- Deprecated as far back as Python 3.1, `turtle.settiltangle()` now raises a deprecation warning and faces removal in Python 3.13. Reach for [`turtle.tiltangle()`](https://docs.python.org/3.14/library/turtle.html#turtle.tiltangle) instead (which had been wrongly tagged deprecated earlier, and whose docstring is now fixed). (Contributed by Hugo van Kemenade in [bpo-45837](https://bugs.python.org/issue?@action=redirect&bpo=45837).)

- Present purely to bridge Python 2 and Python 3 code, [`typing.Text`](https://docs.python.org/3.14/library/typing.html#typing.Text) is now deprecated. No removal date is set yet, though users should lean on [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) instead anywhere they can. (Contributed by Alex Waygood in [gh-92332](https://github.com/python/cpython/issues/92332).)

- Building [`typing.TypedDict`](https://docs.python.org/3.14/library/typing.html#typing.TypedDict) types through the keyword argument syntax is now deprecated, with that support due to vanish in Python 3.13. (Contributed by Jingchen Ye in [gh-90224](https://github.com/python/cpython/issues/90224).)

- Deprecated and bound for removal in Python 3.13 is `webbrowser.MacOSX`, which carries no tests or docs and which [`webbrowser`](https://docs.python.org/3.14/library/webbrowser.html#module-webbrowser) itself never calls. (Contributed by Donghee Na in [bpo-42255](https://bugs.python.org/issue?@action=redirect&bpo=42255).)

- Returning anything other than the default `None` from a [`TestCase`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase) or [`IsolatedAsyncioTestCase`](https://docs.python.org/3.14/library/unittest.html#unittest.IsolatedAsyncioTestCase) test method is behavior that is now deprecated.

- These [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) functions, which were never formally documented, are deprecated and set for removal in Python 3.13:

  - `unittest.findTestCases()`

  - `unittest.makeSuite()`

  - `unittest.getTestCaseNames()`

Reach for these [`TestLoader`](https://docs.python.org/3.14/library/unittest.html#unittest.TestLoader) methods instead:

  - [`unittest.TestLoader.loadTestsFromModule()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestLoader.loadTestsFromModule)

  - [`unittest.TestLoader.loadTestsFromTestCase()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestLoader.loadTestsFromTestCase)

  - [`unittest.TestLoader.getTestCaseNames()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestLoader.getTestCaseNames)

(Contributed by Erlend E. Aasland in [bpo-5846](https://bugs.python.org/issue?@action=redirect&bpo=5846).)

- `unittest.TestProgram.usageExit()` carries a deprecation, set for removal in 3.13. (Contributed by Carlos Damázio in [gh-67048](https://github.com/python/cpython/issues/67048).)

[Subject index](INDEX.md) · [Previous source section](modules.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](pending-removal-in-python-3-12.md)
