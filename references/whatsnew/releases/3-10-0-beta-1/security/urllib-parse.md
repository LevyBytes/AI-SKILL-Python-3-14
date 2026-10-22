# Python 3.10.0 beta 1 / security / urllib parse

[bpo-43882](https://bugs.python.org/issue?@action=redirect&bpo=43882): Having newline or tab characters within portions of a URL might enable certain kinds of attacks.

In keeping with the governing URL specification from WHATWG, [`urllib.parse()`](https://docs.python.org/3.14/library/urllib.parse.html#module-urllib.parse) now strips ASCII newlines and tabs out of URLs, which blocks such attacks.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
