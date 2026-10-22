# Python 3.10.0 alpha 2 / library / http cookiejar

[bpo-38976](https://bugs.python.org/issue?@action=redirect&bpo=38976): On every platform, the [`http.cookiejar`](https://docs.python.org/3.14/library/http.cookiejar.html#module-http.cookiejar) module can now read cookies stored in CURL-style cookiejar files via MozillaCookieJar. Up to now those records were quietly dropped whenever such a cookiejar was loaded.

The HTTP Only flag is also retained on the object now, and a later dump of the MozillaCookieJar instance writes it back to disk accurately.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
