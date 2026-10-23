# What's New In Python 3.2 / Codecs - tarfile

### Codecs

Coverage arrived for the *cp720* Arabic DOS encoding ([bpo-1616979](https://bugs.python.org/issue?@action=redirect&bpo=1616979)).

The error handler argument is no longer disregarded by MBCS encoding. Under the default strict mode it raises an [`UnicodeDecodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeDecodeError) upon hitting a byte sequence it cannot decode and an [`UnicodeEncodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeEncodeError) for a character it cannot encode.

For decoding, the MBCS codec honours the `'strict'` and `'ignore'` error handlers, while for encoding it accepts `'strict'` and `'replace'`.

If you want to reproduce Python3.1 MBCS encoding behaviour, pick the `'ignore'` handler when decoding and the `'replace'` handler when encoding.

Under Mac OS X, Python reads command line arguments using `'utf-8'` instead of the locale encoding.

By default, [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile) applies `'utf-8'` encoding on Windows (rather than `'mbcs'`) along with the `'surrogateescape'` error handler everywhere across all operating systems.

[Subject index](INDEX.md) · [Previous source section](unicode.md) · [Next source section](documentation.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
