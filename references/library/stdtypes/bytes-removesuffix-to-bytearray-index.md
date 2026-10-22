# stdtypes: `bytes.removesuffix()`, `bytearray.removesuffix()`, `bytes.decode()`, `bytearray.decode()`, `bytes.endswith()`, `bytearray.endswith()`, `bytes.find()`, `bytearray.find()`, `bytes.index()`, `bytearray.index()`

bytes.removesuffix(*suffix*, */*)

 bytearray.removesuffix(*suffix*, */*)

When the binary data trails off with the *suffix* string and that *suffix* isn't empty, return `bytes[:-len(suffix)]`. If not, return a copy of the original binary data:

```python
>>> b'MiscTests'.removesuffix(b'Tests')
b'Misc'
>>> b'TmpDirMixin'.removesuffix(b'Tests')
b'TmpDirMixin'

```

The *suffix* may be any [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object).

Note

The bytearray flavour of this method works *not* in place — it consistently builds a fresh object, regardless of whether anything changed.

Added in version 3.9.

 bytes.decode(*encoding='utf-8'*, *errors='strict'*)

 bytearray.decode(*encoding='utf-8'*, *errors='strict'*)

Return the bytes decoded to a `str`.

*encoding* defaults to `'utf-8'`; see [Standard Encodings](https://docs.python.org/3.14/library/codecs.html#standard-encodings) for possible values.

*errors* dictates the treatment of decoding errors. With `'strict'` (the default), a [`UnicodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeError) exception gets raised. The alternatives are `'ignore'`, `'replace'`, plus any further name that has been registered through [`codecs.register_error()`](https://docs.python.org/3.14/library/codecs.html#codecs.register_error). See [Error Handlers](https://docs.python.org/3.14/library/codecs.html#error-handlers) for details.

To keep things fast, the *errors* value goes unchecked for validity unless an actual decoding error arises, [Python Development Mode](https://docs.python.org/3.14/library/devmode.html#devmode) is turned on, or a [debug build](https://docs.python.org/3.14/using/configure.html#debug-build) is in play.

Note

Handing the *encoding* argument to `str` lets you decode any [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) straight away, sparing you from building a throwaway `bytes` or `bytearray` object.

Changed in version 3.1: Added support for keyword arguments.

Changed in version 3.9: validation of the *errors* argument's value now happens under [Python Development Mode](https://docs.python.org/3.14/library/devmode.html#devmode) as well as [debug mode](https://docs.python.org/3.14/using/configure.html#debug-build).

 bytes.endswith(*suffix*[, *start*[, *end*]])

 bytearray.endswith(*suffix*[, *start*[, *end*]])

Return `True` when the binary data finishes with the given *suffix*, and otherwise `False`. *suffix* may also be a tuple of suffixes to test against. Supplying the optional *start* begins the test at that spot. Supplying the optional *end* halts the comparison at that spot.

The suffix(es) to search for may be any [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object).

 bytes.find(*sub*[, *start*[, *end*]])

 bytearray.find(*sub*[, *start*[, *end*]])

Return the smallest index in the data at which the subsequence *sub* turns up, so that *sub* falls inside the slice `s[start:end]`. The optional *start* and *end* arguments follow slice notation conventions. Return `-1` when *sub* isn't located.

For the subsequence you're after, any [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) is acceptable, as is an integer from 0 to 255.

Note

Reach for the `find()` method only when the position of *sub* is what you're after. When all you want is to learn whether *sub* is a substring, use the [`in`](https://docs.python.org/3.14/reference/expressions.html#in) operator:

```python
>>> b'Py' in b'Python'
True

```

Changed in version 3.3: An integer from 0 to 255 is now also taken as the subsequence.

 bytes.index(*sub*[, *start*[, *end*]])

 bytearray.index(*sub*[, *start*[, *end*]])

Like `find()`, but raise [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when the subsequence is not found.

For the subsequence you're after, any [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) is acceptable, as is an integer from 0 to 255.

Changed in version 3.3: An integer from 0 to 255 is now also taken as the subsequence.

[Subject index](INDEX.md) · [Previous](bytes-count-to-bytearray-removeprefix.md) · [Continue](bytes-join-to-bytearray-rindex.md) · [Owning module, declaration or section: Bytes and Bytearray Operations](bytes-count-to-bytearray-removeprefix.md)
