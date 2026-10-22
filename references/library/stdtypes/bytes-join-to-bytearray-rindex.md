# stdtypes: `bytes.join()`, `bytearray.join()`, `bytes.partition()`, `bytearray.partition()`, `bytes.replace()`, `bytearray.replace()`, `bytes.rfind()`, `bytearray.rfind()`, `bytes.rindex()`, `bytearray.rindex()`

bytes.join(*iterable*, */*)

 bytearray.join(*iterable*, */*)

Return a bytes or bytearray object formed by joining together the binary data sequences found in *iterable*. Should *iterable* hold any values that aren't [bytes-like objects](https://docs.python.org/3.14/glossary.html#term-bytes-like-object), `str` objects included, a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised. Whatever is held in the bytes or bytearray object that supplies this method serves as the separator placed between elements.

 *static *bytes.maketrans(*from*, *to*, */*)

 *static *bytearray.maketrans(*from*, *to*, */*)

This static method produces a translation table for use with `bytes.translate()` that maps every character in *from* onto the character occupying the matching position in *to*; both *from* and *to* have to be [bytes-like objects](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) of equal length.

Added in version 3.1.

 bytes.partition(*sep*, */*)

 bytearray.partition(*sep*, */*)

Break the sequence at where *sep* first appears, then return a 3-tuple holding the portion ahead of the separator, the separator itself (or a bytearray copy of it), and the portion following the separator. Should the separator be absent, return a 3-tuple holding a copy of the original sequence trailed by two empty bytes or bytearray objects.

The separator to search for may be any [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object).

 bytes.replace(*old*, *new*, *count=-1*, */*)

 bytearray.replace(*old*, *new*, *count=-1*, */*)

Return a copy of the sequence in which every occurrence of the subsequence *old* has been swapped for *new*. When the optional *count* argument is supplied, only that first *count* of occurrences gets swapped.

The subsequence to search for and its replacement may be any [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object).

Note

The bytearray flavour of this method works *not* in place — it consistently builds a fresh object, regardless of whether anything changed.

 bytes.rfind(*sub*[, *start*[, *end*]])

 bytearray.rfind(*sub*[, *start*[, *end*]])

Return the largest index in the sequence at which the subsequence *sub* turns up, so that *sub* falls inside `s[start:end]`. The optional *start* and *end* arguments follow slice notation conventions. Return `-1` upon failure.

For the subsequence you're after, any [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) is acceptable, as is an integer from 0 to 255.

Changed in version 3.3: An integer from 0 to 255 is now also taken as the subsequence.

 bytes.rindex(*sub*[, *start*[, *end*]])

 bytearray.rindex(*sub*[, *start*[, *end*]])

[Subject index](INDEX.md) · [Previous](bytes-removesuffix-to-bytearray-index.md) · [Owning module, declaration or section: Bytes and Bytearray Operations](bytes-count-to-bytearray-removeprefix.md) · [Required continuation of the source contract](bytes-rindex-and-bytearray-rindex.md)
