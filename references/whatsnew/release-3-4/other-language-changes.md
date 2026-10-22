# What's New In Python 3.4 / Other Language Changes — codecs, collections.abc, inspect, pydoc, weakref

### Other Language Changes

A handful of smaller adjustments to the core Python language:

- Unicode database updated to UCD version 6.3.

- [`min()`](https://docs.python.org/3.14/library/functions.html#min) and [`max()`](https://docs.python.org/3.14/library/functions.html#max) now take a *default* keyword-only argument, letting you state the value returned whenever the iterable under evaluation holds nothing. (Contributed by Julian Berman in [bpo-18111](https://bugs.python.org/issue?@action=redirect&bpo=18111).)

- Module objects are now [weakly referenceable](https://docs.python.org/3.14/library/weakref.html#mod-weakref).

- Module `__file__` attributes (along with related values) should from now on always hold absolute paths by default, the lone exception being `__main__.__file__` when a script gets run directly through a relative path. (Contributed by Brett Cannon in [bpo-18416](https://bugs.python.org/issue?@action=redirect&bpo=18416).)

- All the UTF-* codecs (UTF-7 aside) now turn away surrogates while encoding and while decoding unless the `surrogatepass` error handler applies, the carve-outs being the UTF-16 decoder (which takes valid surrogate pairs) plus the UTF-16 encoder (which, for non-BMP characters, produces them on output). (Contributed by Victor Stinner, Kang-Hao (Kenny) Lu and Serhiy Storchaka in [bpo-12892](https://bugs.python.org/issue?@action=redirect&bpo=12892).)

- New German EBCDIC [codec](https://docs.python.org/3.14/library/codecs.html#standard-encodings) `cp273`. (Contributed by Michael Bierenfeld and Andrew Kuchling in [bpo-1097797](https://bugs.python.org/issue?@action=redirect&bpo=1097797).)

- New Ukrainian [codec](https://docs.python.org/3.14/library/codecs.html#standard-encodings) `cp1125`. (Contributed by Serhiy Storchaka in [bpo-19668](https://bugs.python.org/issue?@action=redirect&bpo=19668).)

- [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).join() and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray).join() will now take any buffer object as an argument. (Contributed by Antoine Pitrou in [bpo-15958](https://bugs.python.org/issue?@action=redirect&bpo=15958).)

- For its *base* argument, the [`int`](https://docs.python.org/3.14/library/functions.html#int) constructor will now take any object carrying an `__index__` method. (Contributed by Mark Dickinson in [bpo-16772](https://bugs.python.org/issue?@action=redirect&bpo=16772).)

- Frame objects gain a [`clear()`](https://docs.python.org/3.14/reference/datamodel.html#frame.clear) method that drops every reference the frame holds to its local variables. (Contributed by Antoine Pitrou in [bpo-17934](https://bugs.python.org/issue?@action=redirect&bpo=17934).)

- [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) now registers as a [`Sequence`](https://docs.python.org/3.14/library/collections.abc.html#module-collections.abc), and works with the [`reversed()`](https://docs.python.org/3.14/library/functions.html#reversed) builtin. (Contributed by Nick Coghlan and Claudiu Popa in [bpo-18690](https://bugs.python.org/issue?@action=redirect&bpo=18690) and [bpo-19078](https://bugs.python.org/issue?@action=redirect&bpo=19078).)

- The signatures that [`help()`](https://docs.python.org/3.14/library/functions.html#help) reports have, in a number of cases, been reshaped and refined thanks to the arrival of Argument Clinic plus further work on the [`inspect`](https://docs.python.org/3.14/library/inspect.html#module-inspect) and [`pydoc`](https://docs.python.org/3.14/library/pydoc.html#module-pydoc) modules.

- [`__length_hint__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__length_hint__) now belongs to the formal language specification (see [**PEP 424**](https://peps.python.org/pep-0424/)). (Contributed by Armin Ronacher in [bpo-16148](https://bugs.python.org/issue?@action=redirect&bpo=16148).)

[Subject index](INDEX.md) · [Previous source section](pep-451-a-modulespec-type-for-the-import-system.md) · [Next source section](asyncio.md) · [Release/subject declaration](release-highlights.md)
