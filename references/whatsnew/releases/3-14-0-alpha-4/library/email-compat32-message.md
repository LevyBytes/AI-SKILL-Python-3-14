# Python 3.14.0 alpha 4 / library / email compat32 message

[gh-98188](https://github.com/python/cpython/issues/98188): Resolved a problem in [`email.message.Message.get_payload()`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message.get_payload) where decoding failed if the Content Transfer Encoding mechanism carried trailing whitespaces or extra junk text. Hui Liu wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
