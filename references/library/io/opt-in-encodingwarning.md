# io - Opt-in EncodingWarning

### Opt-in EncodingWarning

Added in version 3.10: Consult [**PEP 597**](https://peps.python.org/pep-0597/) for further details.

To track down spots where the default locale encoding gets used, you can turn on the [`-X warn_default_encoding`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) command line option or assign the [`PYTHONWARNDEFAULTENCODING`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONWARNDEFAULTENCODING) environment variable; either causes an [`EncodingWarning`](https://docs.python.org/3.14/library/exceptions.html#EncodingWarning) to be raised whenever the default encoding is in use.

Should you be offering an API that calls [`open()`](https://docs.python.org/3.14/library/functions.html#open) or `TextIOWrapper` and forwards `encoding=None` as a parameter, `text_encoding()` lets the API's callers receive an [`EncodingWarning`](https://docs.python.org/3.14/library/exceptions.html#EncodingWarning) whenever they omit an `encoding`. Still, do think about defaulting to UTF-8 (that is, `encoding="utf-8"`) for any new APIs.

[Subject index](INDEX.md) · [Previous](text-encoding.md) · [Continue](io-default-buffer-size-to-io-unsupportedoperation.md) · [Owning module, declaration or section: io](io-core-tools-for-working-with-streams.md)
