# Python 3.9.0 alpha 1 / library / functions and types

[bpo-36324](https://bugs.python.org/issue?@action=redirect&bpo=36324): The internal attributes belonging to statistics.NormalDist() are now private.

[bpo-37502](https://bugs.python.org/issue?@action=redirect&bpo=37502): Setting the buffers argument to None no longer makes pickle.loads() raise TypeError

[bpo-37479](https://bugs.python.org/issue?@action=redirect&bpo=37479): Should a subclass override `Enum.__str__`, that override is what `Enum.__format__` will call upon, no matter whether mixin classes happen to be in play.

[bpo-37251](https://bugs.python.org/issue?@action=redirect&bpo=37251): Removed the `__code__` check inside AsyncMock that wrongly treated function specs as async objects yet did not recognize classes defining `__await__` but lacking a `__code__` attribute as async objects.

[bpo-38066](https://bugs.python.org/issue?@action=redirect&bpo=38066): Made the internal asyncio.Stream methods feed_eof(), feed_data(), set_exception() and set_transport() hidden.

[bpo-18748](https://bugs.python.org/issue?@action=redirect&bpo=18748): To more closely match the `_io.IOBase` finalizer, the `_pyio.IOBase` destructor now stays inert whenever fetching the `closed` attribute fails.

[bpo-37206](https://bugs.python.org/issue?@action=redirect&bpo=37206): In function signatures, default values that cannot be rendered as Python objects are no longer mistakenly shown as `None`.

[bpo-12144](https://bugs.python.org/issue?@action=redirect&bpo=12144): See that cookies bearing an `expires` attribute get handled inside `CookieJar.make_cookies()`.

[bpo-37178](https://bugs.python.org/issue?@action=redirect&bpo=37178): math.perm() gained a single-argument form that behaves the same as math.factorial().

[bpo-37165](https://bugs.python.org/issue?@action=redirect&bpo=37165): Moved _collections._count_elements over to the Argument Clinic.

[bpo-34282](https://bugs.python.org/issue?@action=redirect&bpo=34282): Dropped the `Enum._convert` method, which had been deprecated back in 3.8.

[bpo-37150](https://bugs.python.org/issue?@action=redirect&bpo=37150): Now `argparse._ActionsContainer.add_argument` raises an error should someone mistakenly hand it the FileType class object in place of a FileType instance for the `type` argument.

[bpo-36871](https://bugs.python.org/issue?@action=redirect&bpo=36871): When checking a mock object against method calls, make sure the method signature is what gets used rather than the class constructor signature. Karthikeyan Singaravelan wrote the patch.

[bpo-38163](https://bugs.python.org/issue?@action=redirect&bpo=38163): Child mocks now figure out for themselves whether they are synchronous or asynchronous; asynchronous ones become AsyncMocks while synchronous ones turn into either MagicMock or Mock, according to the type of their parent.

[bpo-38108](https://bugs.python.org/issue?@action=redirect&bpo=38108): A synchronous magic method on an AsyncMock now hands back a MagicMock. An asynchronous magic method on a MagicMock now hands back an AsyncMock.

[bpo-38237](https://bugs.python.org/issue?@action=redirect&bpo=38237): The arguments accepted by the builtin pow function are now more descriptive and may additionally be supplied as keywords.

[bpo-33936](https://bugs.python.org/issue?@action=redirect&bpo=33936): With OpenSSL 1.1.0+, _hashlib no longer invokes the now-obsolete OpenSSL initialization function.

[bpo-38565](https://bugs.python.org/issue?@action=redirect&bpo=38565): A fresh cache_parameters() method was added for functools.lru_cache() so that pickling is better supported.

[bpo-36321](https://bugs.python.org/issue?@action=redirect&bpo=36321): A misspelled attribute was dropped. Its removal in 3.9 had already been flagged by the 3.8 changelog.

[bpo-38478](https://bugs.python.org/issue?@action=redirect&bpo=38478): Pablo Galindo patched a defect in `inspect.signature.bind()` whereby it broke when given a keyword argument bearing the same name as a positional-only parameter.

[bpo-38371](https://bugs.python.org/issue?@action=redirect&bpo=38371): Within `_tkinter.TkappType`, the `split()` method was deprecated in favor of `splitlist()`, whose behavior is more consistent and predictable.

[bpo-38006](https://bugs.python.org/issue?@action=redirect&bpo=38006): A local remove() function serving as the callback for weak references is defined by weakref.WeakValueDictionary. That function had been built with a closure. The implementation was changed to steer clear of the closure.

[bpo-37972](https://bugs.python.org/issue?@action=redirect&bpo=37972): Subscripts on the `unittest.mock.call` objects now share the same chaining mechanism as every other custom attribute, so that the following usage no longer triggers a `TypeError`:

`call().foo().__getitem__('bar')`

Patch by blhsing

[bpo-32554](https://bugs.python.org/issue?@action=redirect&bpo=32554): Having random.seed() invoke hash on arbitrary types is now deprecated.

[bpo-9938](https://bugs.python.org/issue?@action=redirect&bpo=9938): An optional `exit_on_error` keyword argument was added for `ArgumentParser`.

[bpo-14465](https://bugs.python.org/issue?@action=redirect&bpo=14465): Stefan Behnel contributed an xml.etree.ElementTree.indent() function for the pretty-printing of XML trees.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
