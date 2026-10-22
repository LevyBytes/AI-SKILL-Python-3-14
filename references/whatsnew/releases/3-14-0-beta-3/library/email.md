# Python 3.14.0 beta 3 / library / email

[gh-134151](https://github.com/python/cpython/issues/134151): [`email`](https://docs.python.org/3.14/library/email.html#module-email): A [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) within [`email.utils.decode_params()`](https://docs.python.org/3.14/library/email.utils.html#email.utils.decode_params) was fixed; it arose while sorting [**RFC 2231**](https://datatracker.ietf.org/doc/html/rfc2231.html) continuations holding an unnumbered section.

[gh-134152](https://github.com/python/cpython/issues/134152): [`email`](https://docs.python.org/3.14/library/email.html#module-email): Parsing of an email message ID carrying an invalid domain was fixed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
