# What's New In Python 3.3 / email / Other API Changes - datetime, email.parser, email.utils

#### Other API Changes

A new [`BytesHeaderParser`](https://docs.python.org/3.14/library/email.parser.html#email.parser.BytesHeaderParser) joins the [`parser`](https://docs.python.org/3.14/library/email.parser.html#module-email.parser) module, pairing with [`HeaderParser`](https://docs.python.org/3.14/library/email.parser.html#email.parser.HeaderParser) so the Bytes API is now whole.

New utility functions:

- [`format_datetime()`](https://docs.python.org/3.14/library/email.utils.html#email.utils.format_datetime): hand it a [`datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime) and it returns a string laid out for an email header.

- [`parsedate_to_datetime()`](https://docs.python.org/3.14/library/email.utils.html#email.utils.parsedate_to_datetime): take a date string out of an email header and turn it into an aware [`datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime); should the offset read `-0000`, you get a naive `datetime` instead.

- [`localtime()`](https://docs.python.org/3.14/library/email.utils.html#email.utils.localtime): Called bare, it hands back the present local moment as an aware [`datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime) carrying the local [`timezone`](https://docs.python.org/3.14/library/datetime.html#datetime.timezone). Pass it an aware `datetime` and it rewrites that into an aware `datetime` set to the local `timezone`.

[Subject index](INDEX.md) · [Previous source section](email-provisional-policy-with-new-header-api.md) · [Next source section](ftplib.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](email-policy-framework.md)
