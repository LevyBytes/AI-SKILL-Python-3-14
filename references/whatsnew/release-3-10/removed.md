# What's New In Python 3.10 / Removed - asyncio, asyncio-api-index, collections, collections.abc, html.parser

### Removed

- The special methods `__int__`, `__float__`, `__floordiv__`, `__mod__`, `__divmod__`, `__rfloordiv__`, `__rmod__` and `__rdivmod__` on the [`complex`](https://docs.python.org/3.14/library/functions.html#complex) class are gone. Each of them only ever raised a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). (Contributed by Serhiy Storchaka in [bpo-41974](https://bugs.python.org/issue?@action=redirect&bpo=41974).)

- The `ParserBase.error()` method, which lived in the private, undocumented `_markupbase` module, has been dropped. The sole subclass of `ParserBase` is [`html.parser.HTMLParser`](https://docs.python.org/3.14/library/html.parser.html#html.parser.HTMLParser), and its own `error()` had already been pulled back in Python 3.5. (Contributed by Berker Peksag in [bpo-31844](https://bugs.python.org/issue?@action=redirect&bpo=31844).)

- The `unicodedata.ucnhash_CAPI` attribute, an internal PyCapsule object, has been deleted. Its companion private `_PyUnicode_Name_CAPI` structure now lives in the internal C API. (Contributed by Victor Stinner in [bpo-42157](https://bugs.python.org/issue?@action=redirect&bpo=42157).)

- The `parser` module — deprecated back in 3.9 once the project moved to the new PEG parser — is gone, and so are the C source and header files that only the old parser used, among them `node.h`, `parser.h`, `graminit.h` and `grammar.h`.

- The Public C API functions `PyParser_SimpleParseStringFlags`, `PyParser_SimpleParseStringFlagsFilename`, `PyParser_SimpleParseFileFlags` and `PyNode_Compile`, deprecated in 3.9 after the move to the new PEG parser, have been removed.

- The `formatter` module, deprecated since Python 3.4, has been removed. It was largely obsolete, rarely used, and untested. Removal had first been planned for Python 3.6, but such cleanups waited until Python 2.7 reached EOL. Anyone still depending on it should lift whatever classes they need into their own code. (Contributed by Donghee Na and Terry J. Reedy in [bpo-42299](https://bugs.python.org/issue?@action=redirect&bpo=42299).)

- The `PyModule_GetWarningsModule()` function has been removed; it lost all purpose once the `_warnings` module was turned into a builtin module back in 2.6. (Contributed by Hai Shi in [bpo-42599](https://bugs.python.org/issue?@action=redirect&bpo=42599).)

- The deprecated aliases for the [Collections Abstract Base Classes](https://docs.python.org/3.14/library/collections.abc.html#collections-abstract-base-classes) have been dropped from the [`collections`](https://docs.python.org/3.14/library/collections.html#module-collections) module. (Contributed by Victor Stinner in [bpo-37324](https://bugs.python.org/issue?@action=redirect&bpo=37324).)

- Following its Python 3.8 deprecation, the `loop` parameter is gone from most of [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio)'s [high-level API](https://docs.python.org/3.14/library/asyncio-api-index.html). Several reasons drove the change:

  1.

It makes the high-level API leaner.

  2.

Since Python 3.7, high-level API functions already pick up the running event loop of the current thread on their own. Handing the event loop to the API is unnecessary in the usual cases.

  3.

Threading an event loop through calls is bug-prone, particularly once loops are running across separate threads.

Keep in mind that `loop` is still honored by the low-level API. Refer to Changes in the Python API for samples showing how to update existing code.

(Contributed by Yurii Karabas, Andrew Svetlov, Yury Selivanov and Kyle Stanley in [bpo-42392](https://bugs.python.org/issue?@action=redirect&bpo=42392).)

[Subject index](INDEX.md) · [Previous source section](deprecated.md) · [Next source section](porting-to-python-3-10.md) · [Release/subject declaration](summary-release-highlights.md)
