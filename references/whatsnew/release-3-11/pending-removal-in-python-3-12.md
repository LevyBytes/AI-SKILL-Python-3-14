# What's New In Python 3.11 / Pending Removal in Python 3.12 — typing

### Pending Removal in Python 3.12

These Python APIs picked up a deprecation in prior Python releases and are due for removal in Python 3.12.

The C APIs awaiting removal sit in their own section.

- The `asynchat` module

- The `asyncore` module

- The [entire distutils package](https://docs.python.org/3.14/whatsnew/3.10.html#distutils-deprecated)

- The `imp` module

- The [`typing.io`](https://docs.python.org/3.14/library/typing.html#typing.IO) namespace

- The [`typing.re`](https://docs.python.org/3.14/library/typing.html#typing.Pattern) namespace

- `cgi.log()`

- `importlib.find_loader()`

- `importlib.abc.Loader.module_repr()`

- `importlib.abc.MetaPathFinder.find_module()`

- `importlib.abc.PathEntryFinder.find_loader()`

- `importlib.abc.PathEntryFinder.find_module()`

- `importlib.machinery.BuiltinImporter.find_module()`

- `importlib.machinery.BuiltinLoader.module_repr()`

- `importlib.machinery.FileFinder.find_loader()`

- `importlib.machinery.FileFinder.find_module()`

- `importlib.machinery.FrozenImporter.find_module()`

- `importlib.machinery.FrozenLoader.module_repr()`

- `importlib.machinery.PathFinder.find_module()`

-

`importlib.machinery.WindowsRegistryFinder.find_module()`

- `importlib.util.module_for_loader()`

- `importlib.util.set_loader_wrapper()`

- `importlib.util.set_package_wrapper()`

- `pkgutil.ImpImporter`

- `pkgutil.ImpLoader`

- `pathlib.Path.link_to()`

- `sqlite3.enable_shared_cache()`

- `sqlite3.OptimizedUnicode()`

- `PYTHONTHREADDEBUG` environment variable

- These deprecated aliases within [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest):

>
| Deprecated alias | Method Name | Deprecated in |
| --- | --- | --- |
| `failUnless` | `assertTrue()` | 3.1 |
| `failIf` | `assertFalse()` | 3.1 |
| `failUnlessEqual` | `assertEqual()` | 3.1 |
| `failIfEqual` | `assertNotEqual()` | 3.1 |
| `failUnlessAlmostEqual` | `assertAlmostEqual()` | 3.1 |
| `failIfAlmostEqual` | `assertNotAlmostEqual()` | 3.1 |
| `failUnlessRaises` | `assertRaises()` | 3.1 |
| `assert_` | `assertTrue()` | 3.2 |
| `assertEquals` | `assertEqual()` | 3.2 |
| `assertNotEquals` | `assertNotEqual()` | 3.2 |
| `assertAlmostEquals` | `assertAlmostEqual()` | 3.2 |
| `assertNotAlmostEquals` | `assertNotAlmostEqual()` | 3.2 |
| `assertRegexpMatches` | `assertRegex()` | 3.2 |
| `assertRaisesRegexp` | `assertRaisesRegex()` | 3.2 |
| `assertNotRegexpMatches` | `assertNotRegex()` | 3.5 |

[Subject index](INDEX.md) · [Previous source section](standard-library.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](removed.md)
