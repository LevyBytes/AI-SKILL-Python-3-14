# Python 3.13.0 beta 1 / library / email compat32 message

[gh-80361](https://github.com/python/cpython/issues/80361): Resolves a TypeError raised by [`email.message.Message.get_payload()`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message.get_payload) whenever the charset carries [**RFC 2231**](https://datatracker.ietf.org/doc/html/rfc2231.html) encoding.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
