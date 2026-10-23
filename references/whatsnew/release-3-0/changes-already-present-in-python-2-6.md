# What's New In Python 3.0 / Changes Already Present In Python 2.6 - abc, collections, collections.abc, fractions, io, numbers

[PEP 3110: Exception-Handling Changes](https://docs.python.org/3.14/whatsnew/2.6.html#pep-3110). With this release, the [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) *exc* `as` *var* form becomes the official spelling, while the older `except` *exc*, *var* construction is dropped. (Naturally, the `as` *var* portion stays optional whenever you like.)

- [PEP 3112: Byte Literals](https://docs.python.org/3.14/whatsnew/2.6.html#pep-3112). Writing a `b"..."` literal (along with the related spellings `b'...'`, `b"""..."""`, and `br"..."`) now yields an object whose type is [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

- [PEP 3116: New I/O Library](https://docs.python.org/3.14/whatsnew/2.6.html#pep-3116). Performing file I/O is now done through the [`io`](https://docs.python.org/3.14/library/io.html#module-io) module as the canonical approach. The built-in [`open()`](https://docs.python.org/3.14/library/functions.html#open) call has become a synonym for [`io.open()`](https://docs.python.org/3.14/library/io.html#io.open), gaining the extra keyword parameters `encoding`, `errors`, `newline`, and `closefd`. Bear in mind, too, that passing a bad `mode` value now triggers [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) rather than [`IOError`](https://docs.python.org/3.14/library/exceptions.html#IOError). You can reach the underlying binary stream behind a text stream through `f.buffer` (though keep in mind the text object keeps its own internal buffer to make encoding and decoding faster).

- [PEP 3118: Revised Buffer Protocol](https://docs.python.org/3.14/whatsnew/2.6.html#pep-3118). The former built-in `buffer()` has truly been dropped; its replacement, the new built-in [`memoryview()`](https://docs.python.org/3.14/library/stdtypes.html#memoryview), offers roughly the same capability.

- [PEP 3119: Abstract Base Classes](https://docs.python.org/3.14/whatsnew/2.6.html#pep-3119). Both the [`abc`](https://docs.python.org/3.14/library/abc.html#module-abc) module and the ABCs declared within the [`collections`](https://docs.python.org/3.14/library/collections.html#module-collections) module now occupy a noticeably larger place in the language, with native containers such as [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) and [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) satisfying the [`collections.MutableMapping`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.MutableMapping) and [`collections.MutableSequence`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.MutableSequence) ABCs in turn.

- [PEP 3127: Integer Literal Support and Syntax](https://docs.python.org/3.14/whatsnew/2.6.html#pep-3127). As noted earlier, only the revised octal spelling remains valid, and a notation for binary literals is now available too.

- [PEP 3129: Class Decorators](https://docs.python.org/3.14/whatsnew/2.6.html#pep-3129).

- [PEP 3141: A Type Hierarchy for Numbers](https://docs.python.org/3.14/whatsnew/2.6.html#pep-3141). The [`numbers`](https://docs.python.org/3.14/library/numbers.html#module-numbers) module gives ABCs yet another application, laying out what Python calls its “numeric tower”. Worth a mention as well is the fresh [`fractions`](https://docs.python.org/3.14/library/fractions.html#module-fractions) module, an implementation of [`numbers.Rational`](https://docs.python.org/3.14/library/numbers.html#numbers.Rational).

### Changes Already Present In Python 2.6

Because plenty of users very likely leap directly from Python 2.5 to Python 3.0, this part refreshes the reader on features that were first conceived for Python 3.0 but landed earlier in Python 2.6 through back-porting. Look to the matching parts of [What's New in Python 2.6](https://docs.python.org/3.14/whatsnew/2.6.html#whats-new-in-2-6) for fuller writeups.

- [PEP 343: The ?with? statement](https://docs.python.org/3.14/whatsnew/2.6.html#pep-0343). The [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement is a standard part of the language now and need no longer be imported from [`__future__`](https://docs.python.org/3.14/library/__future__.html#module-__future__). Take a look as well at [Writing Context Managers](https://docs.python.org/3.14/whatsnew/2.6.html#new-26-context-managers) and [The contextlib module](https://docs.python.org/3.14/whatsnew/2.6.html#new-module-contextlib).

- [PEP 366: Explicit Relative Imports From a Main Module](https://docs.python.org/3.14/whatsnew/2.6.html#pep-0366). This makes the [`-m`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-m) option more useful when the named module sits inside a package.

- [PEP 370: Per-user site-packages Directory](https://docs.python.org/3.14/whatsnew/2.6.html#pep-0370).

- [PEP 371: The multiprocessing Package](https://docs.python.org/3.14/whatsnew/2.6.html#pep-0371).

- [PEP 3101: Advanced String Formatting](https://docs.python.org/3.14/whatsnew/2.6.html#pep-3101). Note: the 2.6 writeup cites the [`format()`](https://docs.python.org/3.14/library/functions.html#format) method on both 8-bit and Unicode strings. Under 3.0, this method belongs to the [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) type alone (text strings backed by Unicode); the [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) type lacks it. The intent is to eventually establish this as the sole API for string formatting and to begin deprecating the `%` operator in Python 3.1.

- [PEP 3105: print As a Function](https://docs.python.org/3.14/whatsnew/2.6.html#pep-3105). This is a standard part of the language now and need no longer be imported from [`__future__`](https://docs.python.org/3.14/library/__future__.html#module-__future__). Fuller detail appeared above.

-

[Subject index](INDEX.md) · [Next source section](library-changes.md) · [Release/subject declaration](common-stumbling-blocks.md) · [Previous source section](removed-syntax.md)
