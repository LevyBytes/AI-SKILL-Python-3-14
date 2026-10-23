# library.orientation: Standard-library scope and organization

### The Python Standard Library

Where [The Python Language Reference](https://docs.python.org/3.14/reference/index.html#reference-index) sets out the precise syntax and semantics of the language itself, this library reference manual documents the standard library shipped alongside Python. It additionally covers a number of the optional pieces that Python distributions frequently bundle in.

The standard library that comes with Python is remarkably broad, supplying the wide assortment of facilities shown in the lengthy table of contents below. Within it sit built-in modules (coded in C) that expose system-level capabilities such as file I/O — things otherwise out of reach for Python programmers — alongside modules written in Python that deliver standardized answers to many recurring everyday programming problems. Several of these modules were deliberately built to promote and improve the portability of Python programs, hiding platform-specific quirks behind platform-neutral APIs.

On Windows, the Python installers typically bundle the complete standard library and frequently a good deal of extra material besides. On Unix-like systems Python tends to arrive as a set of packages, so pulling in some or all of the optional pieces may require the packaging tools that ship with the operating system.

Beyond the standard library itself, there is a lively pool of hundreds of thousands of components — ranging from standalone programs and modules to packages and complete application development frameworks — that you can fetch from the [Python Package Index](https://pypi.org).

- [Introduction](https://docs.python.org/3.14/library/intro.html)
  - [Notes on availability](https://docs.python.org/3.14/library/intro.html#notes-on-availability)

- [Built-in Functions](https://docs.python.org/3.14/library/functions.html)
- [Built-in Constants](https://docs.python.org/3.14/library/constants.html)
  - [Constants added by the `site` module](https://docs.python.org/3.14/library/constants.html#constants-added-by-the-site-module)

- [Built-in Types](https://docs.python.org/3.14/library/stdtypes.html)
  - [Truth Value Testing](https://docs.python.org/3.14/library/stdtypes.html#truth-value-testing)
  - [Boolean Operations - `and`, `or`, `not`](https://docs.python.org/3.14/library/stdtypes.html#boolean-operations-and-or-not)
  - [Comparisons](https://docs.python.org/3.14/library/stdtypes.html#comparisons)
  - [Numeric Types - `int`, `float`, `complex`](https://docs.python.org/3.14/library/stdtypes.html#numeric-types-int-float-complex)
  - [Boolean Type - `bool`](https://docs.python.org/3.14/library/stdtypes.html#boolean-type-bool)
  - [Iterator Types](https://docs.python.org/3.14/library/stdtypes.html#iterator-types)
  - [Sequence Types - `list`, `tuple`, `range`](https://docs.python.org/3.14/library/stdtypes.html#sequence-types-list-tuple-range)
  - [Text and Binary Sequence Type Methods Summary](https://docs.python.org/3.14/library/stdtypes.html#text-and-binary-sequence-type-methods-summary)
  - [Text Sequence Type - `str`](https://docs.python.org/3.14/library/stdtypes.html#text-sequence-type-str)
  - [Binary Sequence Types - `bytes`, `bytearray`, `memoryview`](https://docs.python.org/3.14/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview)
  - [Set Types - `set`, `frozenset`](https://docs.python.org/3.14/library/stdtypes.html#set-types-set-frozenset)
  - [Mapping Types - `dict`](https://docs.python.org/3.14/library/stdtypes.html#mapping-types-dict)
  - [Context Manager Types](https://docs.python.org/3.14/library/stdtypes.html#context-manager-types)
  - [Type Annotation Types - Generic Alias, Union](https://docs.python.org/3.14/library/stdtypes.html#type-annotation-types-generic-alias-union)
  - [Other Built-in Types](https://docs.python.org/3.14/library/stdtypes.html#other-built-in-types)
  - [Special Attributes](https://docs.python.org/3.14/library/stdtypes.html#special-attributes)
  - [Integer string conversion length limitation](https://docs.python.org/3.14/library/stdtypes.html#integer-string-conversion-length-limitation)

- [Built-in Exceptions](https://docs.python.org/3.14/library/exceptions.html)
  - [Exception context](https://docs.python.org/3.14/library/exceptions.html#exception-context)
  - [Inheriting from built-in exceptions](https://docs.python.org/3.14/library/exceptions.html#inheriting-from-built-in-exceptions)
  - [Base classes](https://docs.python.org/3.14/library/exceptions.html#base-classes)
  - [Concrete exceptions](https://docs.python.org/3.14/library/exceptions.html#concrete-exceptions)
  - [Warnings](https://docs.python.org/3.14/library/exceptions.html#warnings)
  - [Exception groups](https://docs.python.org/3.14/library/exceptions.html#exception-groups)
  - [Exception hierarchy](https://docs.python.org/3.14/library/exceptions.html#exception-hierarchy)

- [Thread Safety Guarantees](https://docs.python.org/3.14/library/threadsafety.html)
  - [Thread safety levels](https://docs.python.org/3.14/library/threadsafety.html#thread-safety-levels)
  - [Thread safety for list objects](https://docs.python.org/3.14/library/threadsafety.html#thread-safety-for-list-objects)
  - [Thread safety for dict objects](https://docs.python.org/3.14/library/threadsafety.html#thread-safety-for-dict-objects)
  - [Thread safety for set objects](https://docs.python.org/3.14/library/threadsafety.html#thread-safety-for-set-objects)
  - [Thread safety for bytearray objects](https://docs.python.org/3.14/library/threadsafety.html#thread-safety-for-bytearray-objects)
  - [Thread safety for memoryview objects](https://docs.python.org/3.14/library/threadsafety.html#thread-safety-for-memoryview-objects)

- [Text Processing Services](https://docs.python.org/3.14/library/text.html)
  - [`string` - Common string operations](https://docs.python.org/3.14/library/string.html)
  - [`string.templatelib` - Support for template string literals](https://docs.python.org/3.14/library/string.templatelib.html)
  - [`re` - Regular expression operations](https://docs.python.org/3.14/library/re.html)
  - [`difflib` - Helpers for computing deltas](https://docs.python.org/3.14/library/difflib.html)
  - [`textwrap` - Text wrapping and filling](https://docs.python.org/3.14/library/textwrap.html)
  - [`unicodedata` - Unicode Database](https://docs.python.org/3.14/library/unicodedata.html)
  - [`stringprep` - Internet String Preparation](https://docs.python.org/3.14/library/stringprep.html)
  - [`readline` - GNU readline interface](https://docs.python.org/3.14/library/readline.html)
  - [`rlcompleter` - Completion function for GNU readline](https://docs.python.org/3.14/library/rlcompleter.html)

- [Binary Data Services](https://docs.python.org/3.14/library/binary.html)
  - [`struct` - Interpret bytes as packed binary data](https://docs.python.org/3.14/library/struct.html)
  - [`codecs` - Codec registry and base classes](https://docs.python.org/3.14/library/codecs.html)

[Subject index](INDEX.md) · [Continue](data-type-module-routes.md)
