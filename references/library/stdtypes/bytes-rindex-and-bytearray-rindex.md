# bytes.rindex and bytearray.rindex

Behaves the same as `rfind()`, except it raises [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) whenever the subsequence *sub* cannot be located.

The subsequence you search for can be any [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) or an integer falling within 0 to 255.

Changed in version 3.3: An integer between 0 and 255 is now accepted as the subsequence too.

[Subject index](INDEX.md) · [Continue](bytes-rpartition-to-bytearray-lstrip.md) · [Owning module, declaration or section: bytes.rindex and bytearray.rindex](bytes-join-to-bytearray-rindex.md) · [Preceding source contract and version conditions](bytes-join-to-bytearray-rindex.md)
