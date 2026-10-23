# urllib.parse`urllib.parse` - Parse URLs into components

### `urllib.parse` - Parse URLs into components

**Source code:** [Lib/urllib/parse.py](https://github.com/python/cpython/tree/3.14/Lib/urllib/parse.py)

---

This module provides a uniform way to split Uniform Resource Locator (URL) strings into their pieces (the addressing scheme, the network location, the path, and so on), to reassemble those pieces into a URL string again, and—given a “base URL”—to turn a “relative URL” into an absolute one.

Its design follows the internet RFC governing Relative Uniform Resource Locators. The URL schemes it understands are `file`, `ftp`, `gopher`, `hdl`, `http`, `https`, `imap`, `itms-services`, `mailto`, `mms`, `news`, `nntp`, `prospero`, `rsync`, `rtsp`, `rtsps`, `rtspu`, `sftp`, `shttp`, `sip`, `sips`, `snews`, `svn`, `svn+ssh`, `telnet`, `wais`, `ws`, and `wss`.

**CPython implementation detail:** Including the `itms-services` URL scheme may cause an app to fail Apple’s App Store review for the macOS and iOS App Stores. Support for the `itms-services` scheme is unconditionally dropped on iOS; on macOS it *may* be dropped when CPython is compiled with the [`--with-app-store-compliance`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-app-store-compliance) option.

Functions in the `urllib.parse` module split into two broad groups: URL parsing and URL quoting. The sections that follow describe each group thoroughly.

The functions here still use the deprecated term `netloc` (or `net_loc`), a term that came from [**RFC 1808**](https://datatracker.ietf.org/doc/html/rfc1808.html). That term has since been superseded by [**RFC 3986**](https://datatracker.ietf.org/doc/html/rfc3986.html), which put forward `authority` as its successor. `netloc` is kept around for backward compatibility.

[Subject index](INDEX.md) · [Continue](url-parsing.md)
