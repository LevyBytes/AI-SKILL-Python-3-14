# What’s New in Python 2.3 / PEP 263: Source Code Encodings

### PEP 263: Source Code Encodings

It is now possible to mark Python source files as using one of various character set encodings. You declare an encoding by placing a comment in a specific format on either the first or the second line of the source file. A UTF-8 file, for instance, can be marked like so:

```python
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

```

When no such encoding declaration is present, 7-bit ASCII serves as the default encoding. Running or importing modules that hold string literals containing 8-bit characters yet carry no encoding declaration will cause Python 2.3 to raise a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning); under 2.4 the same situation becomes a syntax error.

Only Unicode string literals are influenced by the encoding declaration, and those literals get converted to Unicode according to the encoding you named. Keep in mind that Python identifiers stay limited to ASCII characters, so variable names containing characters beyond the ordinary alphanumerics are not allowed.

See also

[**PEP 263**](https://peps.python.org/pep-0263/) - Defining Python Source Code Encodings

Authored by Marc-André Lemburg and Martin von Löwis; the implementation came from Suzuki Hisao and Martin von Löwis.

[Subject index](INDEX.md) · [Previous source section](pep-255-simple-generators.md) · [Next source section](pep-273-importing-modules-from-zip-archives.md) · [Release/subject declaration](standard-set-type.md)
