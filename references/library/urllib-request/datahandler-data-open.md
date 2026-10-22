# urllib.request — DataHandler Objects

### DataHandler Objects

 DataHandler.data_open(*req*)

Read a data URL. A URL of this kind embeds its content directly inside the URL itself. [**RFC 2397**](https://datatracker.ietf.org/doc/html/rfc2397.html) defines the data URL syntax. This implementation disregards white space inside base64-encoded data URLs, allowing the URL to be wrapped within whatever source file holds it. And although certain browsers tolerate a base64-encoded data URL whose trailing padding is missing, this implementation instead raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when that happens.

[Subject index](INDEX.md) · [Previous](filehandler-file-open.md) · [Continue](ftphandler-ftp-open.md) · [Owning module, declaration or section: urllib.request](urllib-request-urlopen-to-urllib-request-build-opener.md)
