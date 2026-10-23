# os - File Names, Command Line Arguments, and Environment Variables

### File Names, Command Line Arguments, and Environment Variables

Within Python, file names, command line arguments, and environment variables get represented using the string type. On certain systems, decoding these strings to and from bytes has to happen before they are handed to the operating system. Python carries out this conversion via the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler) (see [`sys.getfilesystemencoding()`](https://docs.python.org/3.14/library/sys.html#sys.getfilesystemencoding)).

The [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler) get set up at Python startup by the [`PyConfig_Read()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Read) function: see the [`filesystem_encoding`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.filesystem_encoding) and [`filesystem_errors`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.filesystem_errors) members of [`PyConfig`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig).

Changed in version 3.1: On certain systems, conversion through the file system encoding can fail. When that happens, Python turns to the [surrogateescape encoding error handler](https://docs.python.org/3.14/library/codecs.html#surrogateescape), so undecodable bytes get swapped for a Unicode character U+DC*xx* during decoding, and those are turned back into the original byte during encoding.

The [file system encoding](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler) has to guarantee that it successfully decodes every byte below 128. Should the file system encoding not provide this guarantee, API functions may raise [`UnicodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeError).

See also the [locale encoding](https://docs.python.org/3.14/glossary.html#term-locale-encoding).

[Subject index](INDEX.md) · [Previous](os-error-to-os-name.md) · [Continue](python-utf-8-mode.md) · [Owning module, declaration or section: os](os-error-to-os-name.md)
