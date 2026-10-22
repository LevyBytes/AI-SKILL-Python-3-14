# What’s New in Python 2.3 / PEP 293: Codec Error Handling Callbacks — codecs

### PEP 293: Codec Error Handling Callbacks

Turning a Unicode string into a byte string can run into characters that have no encoding. Up to now, Python offered three ways to handle such errors: “strict” (which raises [`UnicodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeError)), “ignore” (which drops the character), and “replace” (which substitutes a question mark in the resulting string), and “strict” acted as the default. You might, however, want some other treatment of these errors — for example, dropping an XML character reference or an HTML entity reference into the converted output.

Python now ships a flexible framework letting you plug in distinct handling strategies. You register fresh error handlers via [`codecs.register_error()`](https://docs.python.org/3.14/library/codecs.html#codecs.register_error), and codecs then retrieve the handler through [`codecs.lookup_error()`](https://docs.python.org/3.14/library/codecs.html#codecs.lookup_error). There's a matching C API for codecs authored in C. The handler receives the relevant state — the string undergoing conversion, the spot in that string where the error showed up, and the destination encoding. From there the handler may raise an exception or hand back a substitute string.

Two more error handlers ship on top of this framework: “backslashreplace” renders unencodable characters using Python's backslash quoting, and “xmlcharrefreplace” outputs XML character references.

See also

[**PEP 293**](https://peps.python.org/pep-0293/) - Codec Error Handling Callbacks

Written and implemented by Walter Dörwald.

[Subject index](INDEX.md) · [Previous source section](pep-285-a-boolean-type.md) · [Next source section](pep-301-package-index-and-metadata-for-distutils.md) · [Release/subject declaration](standard-set-type.md)
