# What's new in Python 3.14 / uuid - uuid

### uuid

- Support UUID versions 6, 7, and 8 through [`uuid6()`](https://docs.python.org/3.14/library/uuid.html#uuid.uuid6), [`uuid7()`](https://docs.python.org/3.14/library/uuid.html#uuid.uuid7), and [`uuid8()`](https://docs.python.org/3.14/library/uuid.html#uuid.uuid8) accordingly, per [**RFC 9562**](https://datatracker.ietf.org/doc/html/rfc9562.html). (Contributed by Bénédikt Tran in [gh-89083](https://github.com/python/cpython/issues/89083).)

- [`NIL`](https://docs.python.org/3.14/library/uuid.html#uuid.NIL) and [`MAX`](https://docs.python.org/3.14/library/uuid.html#uuid.MAX) can now be used to stand for the Nil and Max UUID formats defined by [**RFC 9562**](https://datatracker.ietf.org/doc/html/rfc9562.html). (Contributed by Nick Pope in [gh-128427](https://github.com/python/cpython/issues/128427).)

- Permit producing several UUIDs at once from the command-line by way of [`python -m uuid --count`](https://docs.python.org/3.14/library/uuid.html#cmdoption-uuid-count). (Contributed by Simon Legner in [gh-131236](https://github.com/python/cpython/issues/131236).)

### uuid

- [`uuid3()`](https://docs.python.org/3.14/library/uuid.html#uuid.uuid3) and [`uuid5()`](https://docs.python.org/3.14/library/uuid.html#uuid.uuid5) now both run roughly 40% faster on 16-byte names and 20% faster on 1024-byte names. Speed for longer names stays the same. (Contributed by Bénédikt Tran in [gh-128150](https://github.com/python/cpython/issues/128150).)

- [`uuid4()`](https://docs.python.org/3.14/library/uuid.html#uuid.uuid4) now runs roughly 30% faster. (Contributed by Bénédikt Tran in [gh-128150](https://github.com/python/cpython/issues/128150).)

[Subject index](INDEX.md) · [Previous source section](urllib.md) · [Next source section](webbrowser.md) · [Release/subject declaration](summary-release-highlights.md) · [Previous source section](textwrap.md) · [Next source section](zlib.md)
