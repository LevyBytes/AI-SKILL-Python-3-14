# What's New In Python 3.3 / Other Language Changes — collections.abc, unicodedata

### Other Language Changes

A handful of more modest tweaks landed in the core Python language:

- Unicode name aliases plus named sequences are now handled. Each of [`unicodedata.lookup()`](https://docs.python.org/3.14/library/unicodedata.html#unicodedata.lookup) and `'\N{...}'` resolves name aliases these days, while `unicodedata.lookup()` additionally resolves named sequences.

(Contributed by Ezio Melotti in [bpo-12753](https://bugs.python.org/issue?@action=redirect&bpo=12753).)

- The bundled Unicode database was refreshed to UCD version 6.1.0

- Testing two [`range()`](https://docs.python.org/3.14/library/stdtypes.html#range) objects for equality now yields an outcome that mirrors whether the sequences those range objects produce are themselves equal. ([bpo-13201](https://bugs.python.org/issue?@action=redirect&bpo=13201))

- For [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) along with [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) objects, an integer in the 0-to-255 range is now permitted as the opening argument to the `count()`, `find()`, `rfind()`, `index()` and `rindex()` methods.

(Contributed by Petri Lehtinen in [bpo-12170](https://bugs.python.org/issue?@action=redirect&bpo=12170).)

- On [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) plus [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray), the `rjust()`, `ljust()`, and `center()` methods will now take a `bytearray` as the `fill` argument. (Contributed by Petri Lehtinen in [bpo-12380](https://bugs.python.org/issue?@action=redirect&bpo=12380).)

- Both [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) picked up fresh `copy()` and `clear()` methods ([bpo-10516](https://bugs.python.org/issue?@action=redirect&bpo=10516)). As a knock-on effect, a `clear()` method is now declared on [`MutableSequence`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.MutableSequence) as well ([bpo-11388](https://bugs.python.org/issue?@action=redirect&bpo=11388)).

- Spelling a raw bytes literal `rb"..."` is now valid, on par with `br"..."`.

(Contributed by Antoine Pitrou in [bpo-13748](https://bugs.python.org/issue?@action=redirect&bpo=13748).)

- [`dict.setdefault()`](https://docs.python.org/3.14/library/stdtypes.html#dict.setdefault) performs just a single lookup of the supplied key now, which renders it atomic alongside the built-in types.

(Contributed by Filip Gruszczyński in [bpo-13521](https://bugs.python.org/issue?@action=redirect&bpo=13521).)

- Whenever a call to a function fails to line up with that function's signature, the resulting error messages are now markedly better.

(Contributed by Benjamin Peterson.)

[Subject index](INDEX.md) · [Previous source section](visible-changes.md) · [Next source section](a-finer-grained-import-lock.md) · [Release/subject declaration](summary-release-highlights.md)
