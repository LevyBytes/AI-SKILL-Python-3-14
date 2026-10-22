# Python 3.14.0 alpha 7 / library / email compat32 message

[gh-127794](https://github.com/python/cpython/issues/127794): Whenever headers get added to [`email.message.Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message) objects, whether through [`email.message.Message.__setitem__()`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message.__setitem__) or [`email.message.Message.add_header()`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message.add_header), the field name now undergoes validation per [**RFC 5322, Section 2.2**](https://datatracker.ietf.org/doc/html/rfc5322.html#section-2.2), and a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised should the field name hold any invalid characters.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
