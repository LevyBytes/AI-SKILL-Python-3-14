# What’s New In Python 3.8 / urllib.parse - urllib.parse

### Notable changes in Python 3.8.10

### urllib.parse

When newline or tab characters appear inside portions of a URL, certain classes of attack become possible. In keeping with the WHATWG specification that revises [**RFC 3986**](https://datatracker.ietf.org/doc/html/rfc3986.html), the parser within [`urllib.parse`](https://docs.python.org/3.14/library/urllib.parse.html#module-urllib.parse) now removes the ASCII newline `\n`, `\r` and tab `\t` characters from the URL, heading off those attacks. Which characters get stripped is governed by a fresh module-level variable, `urllib.parse._UNSAFE_URL_BYTES_TO_REMOVE`. (See [bpo-43882](https://bugs.python.org/issue?@action=redirect&bpo=43882))

[Subject index](INDEX.md) · [Previous source section](macos-11-0-and-apple-silicon-mac-support.md) · [Next source section](changes-in-the-python-api.md) · [Release/subject declaration](assignment-expressions.md)
