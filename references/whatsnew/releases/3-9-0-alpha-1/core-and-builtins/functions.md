# Python 3.9.0 alpha 1 / core and builtins / functions

[bpo-37330](https://bugs.python.org/issue?@action=redirect&bpo=37330): The functions [`open()`](https://docs.python.org/3.14/library/functions.html#open), [`io.open()`](https://docs.python.org/3.14/library/io.html#io.open), [`codecs.open()`](https://docs.python.org/3.14/library/codecs.html#codecs.open) and [`fileinput.FileInput`](https://docs.python.org/3.14/library/fileinput.html#fileinput.FileInput) will no longer take `'U'` (?universal newline?) within the file mode. That flag had been deprecated as far back as Python 3.3.

[bpo-36781](https://bugs.python.org/issue?@action=redirect&bpo=36781): A boolean-value fast path now optimizes [`sum()`](https://docs.python.org/3.14/library/functions.html#sum).

[bpo-19072](https://bugs.python.org/issue?@action=redirect&bpo=19072): The [`classmethod`](https://docs.python.org/3.14/library/functions.html#classmethod) decorator is now able to wrap further descriptors, property objects among them. This was adapted from a patch authored by Graham Dumpleton.

[bpo-37388](https://bugs.python.org/issue?@action=redirect&bpo=37388): Within development mode and a debug build, the *encoding* and *errors* arguments now undergo checking during string encoding and decoding operations. As examples: [`open()`](https://docs.python.org/3.14/library/functions.html#open), [`str.encode()`](https://docs.python.org/3.14/library/stdtypes.html#str.encode) and [`bytes.decode()`](https://docs.python.org/3.14/library/stdtypes.html#bytes.decode).

To favour the best performances by default, the *errors* argument receives a check only upon the first encoding/decoding error, while the *encoding* argument is occasionally disregarded for empty strings.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
