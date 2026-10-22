# Language and standard library pending removal in future versions: typing._UnionGenericAlias compatibility; unittest.IsolatedAsyncioTestCase; urllib.parse deprecated functions; wsgiref; xml.etree.ElementTree; sys._clear_type_cache()

Implementing [`typing.Union`](https://docs.python.org/3.14/library/typing.html#typing.Union) no longer relies on the internal class `typing._UnionGenericAlias`. So that anyone depending on this private class keeps working, a compatibility shim stays in place through at least Python 3.17. (Contributed by Jelle Zijlstra in [gh-105499](https://github.com/python/cpython/issues/105499).)

- [`unittest.IsolatedAsyncioTestCase`](https://docs.python.org/3.14/library/unittest.html#unittest.IsolatedAsyncioTestCase): handing back any value other than `None` from a test case is now deprecated.

- [`urllib.parse`](https://docs.python.org/3.14/library/urllib.parse.html#module-urllib.parse) deprecated functions: [`urlparse()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.urlparse) instead

  - `splitattr()`

  - `splithost()`

  - `splitnport()`

  - `splitpasswd()`

  - `splitport()`

  - `splitquery()`

  - `splittag()`

  - `splittype()`

  - `splituser()`

  - `splitvalue()`

  - `to_bytes()`

- [`wsgiref`](https://docs.python.org/3.14/library/wsgiref.html#module-wsgiref): partial writes from `SimpleHandler.stdout.write()` ought to be avoided.

- [`xml.etree.ElementTree`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#module-xml.etree.ElementTree): checking the truth value of an [`Element`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element) is now deprecated. A later release will have it always yield `True`. Reach instead for explicit `len(elem)` or `elem is not None` tests.

- [`sys._clear_type_cache()`](https://docs.python.org/3.14/library/sys.html#sys._clear_type_cache) is deprecated; reach for [`sys._clear_internal_caches()`](https://docs.python.org/3.14/library/sys.html#sys._clear_internal_caches) in its place.

- The internal class `typing._UnionGenericAlias` no longer backs the implementation of [`typing.Union`](https://docs.python.org/3.14/library/typing.html#typing.Union). So that anyone who depends on this private class keeps working, a compatibility shim will remain in place through at least Python 3.17. (Contributed by Jelle Zijlstra in [gh-105499](https://github.com/python/cpython/issues/105499).)

- [`unittest.IsolatedAsyncioTestCase`](https://docs.python.org/3.14/library/unittest.html#unittest.IsolatedAsyncioTestCase): returning anything other than `None` from a test case is deprecated.

- [`urllib.parse`](https://docs.python.org/3.14/library/urllib.parse.html#module-urllib.parse) deprecated functions: [`urlparse()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.urlparse) instead

  - `splitattr()`

  - `splithost()`

  - `splitnport()`

  - `splitpasswd()`

  - `splitport()`

  - `splitquery()`

  - `splittag()`

  - `splittype()`

  - `splituser()`

  - `splitvalue()`

  - `to_bytes()`

- [`wsgiref`](https://docs.python.org/3.14/library/wsgiref.html#module-wsgiref): `SimpleHandler.stdout.write()` ought never to perform partial writes.

- [`xml.etree.ElementTree`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#module-xml.etree.ElementTree): checking the truth value of an [`Element`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element) is deprecated. A later release will have it return `True` unconditionally. Favor an explicit `len(elem)` or `elem is not None` test in its place.

- [`sys._clear_type_cache()`](https://docs.python.org/3.14/library/sys.html#sys._clear_type_cache) is deprecated; turn to [`sys._clear_internal_caches()`](https://docs.python.org/3.14/library/sys.html#sys._clear_internal_caches) instead.

[Subject index](INDEX.md) · [Next source section](../../c-api-removals/python-3-15/pyimport-importmodulenoblock-through-initialization-getters.md) · [Preceding future-removal list and continued item](typing-text.md) · [Future-version schedule heading](argparse-through-importlib.md) · [Previous source section](ssl-options-and-protocols-threading-methods-typing-text.md)
