# Python 3.9.0 alpha 3 / library / base64

[bpo-39351](https://bugs.python.org/issue?@action=redirect&bpo=39351): The aliases `base64.encodestring()` and `base64.decodestring()`, deprecated since Python 3.1, were removed; reach for [`base64.encodebytes()`](https://docs.python.org/3.14/library/base64.html#base64.encodebytes) and [`base64.decodebytes()`](https://docs.python.org/3.14/library/base64.html#base64.decodebytes) instead.

[bpo-39055](https://bugs.python.org/issue?@action=redirect&bpo=39055): When called with `validate=True`, [`base64.b64decode()`](https://docs.python.org/3.14/library/base64.html#base64.b64decode) now raises a binascii.Error should the input finish with a lone `\n`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
