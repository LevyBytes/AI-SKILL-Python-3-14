# email.utils: Email address and date utility functions

# Email.Utils, Ensurepip

## Overview

Covers: email.utils: Miscellaneous utilities; ensurepip — Bootstrapping the pip installer.

## email.utils: Miscellaneous utilities

### `email.utils`: Miscellaneous utilities

**Source code:** [Lib/email/utils.py](https://github.com/python/cpython/tree/3.14/Lib/email/utils.py)

---

The `email.utils` module ships a handful of handy helpers:

`email.utils.localtime(*dt=None*)`

Hand back local time as an aware datetime object. Invoke it with no arguments and you get the present moment. Supply a [`datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime) instance as *dt* and it gets shifted into the local zone per the system time zone database. A naive *dt* — one whose `dt.tzinfo` is `None` — is taken to already be local time.

Added in version 3.3.

Deprecated since version 3.12, then dropped at version 3.14: the *isdst* parameter.

`email.utils.make_msgid(*idstring=None*, *domain=None*)`

Yields a string fit for use as a *Message-ID* header that conforms to [**RFC 2822**](https://datatracker.ietf.org/doc/html/rfc2822.html). When supplied, the optional *idstring* is a string that bolsters how unique the message id turns out to be. When supplied, the optional *domain* furnishes the part of the msgid following the ‘@’; left out, it falls back to the local hostname. You'd seldom need to override that fallback, though it can help in scenarios like building a distributed system that keeps one consistent domain name spanning several hosts.

Changed in version 3.2: Added the *domain* keyword.

Everything that follows belongs to the legacy (`Compat32`) email API. You won't need to call these by hand under the new API, because its header-parsing machinery already performs the parsing and formatting they offer for you.

`email.utils.quote(*str*)`

Give back a fresh string in which each backslash within *str* becomes two backslashes and each double quote becomes a backslash followed by a double quote.

`email.utils.unquote(*str*)`

Give back a fresh string that is an *unquoted* form of *str*. Should *str* both open and close with double quotes, those get peeled away; the same goes when it both opens and closes with angle brackets.

`email.utils.parseaddr(*address*, ***, *strict=True*)`

Break apart address — which ought to be the contents of some address-bearing field, *To* or *Cc* for instance — into its separate *realname* and *email address* pieces. It returns a tuple holding those, except when parsing fails, where you instead get the 2-tuple `('', '')`.

When *strict* is true, a strict parser is used that turns away malformed inputs.

Changed in version 3.13: An optional *strict* parameter was introduced, and malformed inputs are now turned away out of the box.

`email.utils.formataddr(*pair*, *charset='utf-8'*)`

Running counter to `parseaddr()`, this one accepts a 2-tuple shaped like `(realname, email_address)` and yields the string value fit for a *To* or *Cc* header. When the first member of *pair* is false, the second member comes back untouched.

The optional *charset* names the character set applied for [**RFC 2047**](https://datatracker.ietf.org/doc/html/rfc2047.html) encoding of the `realname` whenever that `realname` holds non-ASCII characters. It may be a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) instance or a [`Charset`](https://docs.python.org/3.14/library/email.charset.html#email.charset.Charset), and it defaults to `utf-8`.

Changed in version 3.3: Added the *charset* option.

`email.utils.getaddresses(*fieldvalues*, ***, *strict=True*)`

What this method gives back is a list of 2-tuples shaped exactly like those `parseaddr()` produces. The *fieldvalues* argument is a sequence of header field values, of the sort [`Message.get_all`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message.get_all) might hand you.

When *strict* is true, it employs a strict parser that turns away malformed inputs.

The brief example below collects every recipient on a message:

```python
from email.utils import getaddresses

tos = msg.get_all('to', [])
ccs = msg.get_all('cc', [])
resent_tos = msg.get_all('resent-to', [])
resent_ccs = msg.get_all('resent-cc', [])
all_recipients = getaddresses(tos + ccs + resent_tos + resent_ccs)

```

Changed in version 3.13: A *strict* optional parameter arrived, with malformed inputs rejected by default from then on.

`email.utils.parsedate(*date*)`

Tries to read a date by the conventions set out in [**RFC 2822**](https://datatracker.ietf.org/doc/html/rfc2822.html). Some mail programs, however, stray from that prescribed layout, so in those situations `parsedate()` does its best to guess the right answer. The *date* argument is a string carrying an [**RFC 2822**](https://datatracker.ietf.org/doc/html/rfc2822.html) date — `"Mon, 20 Nov 1995 19:12:08 -0500"`, say. On a successful parse, `parsedate()` hands back a 9-tuple ready to feed straight into [`time.mktime()`](https://docs.python.org/3.14/library/time.html#time.mktime); failing that, you get `None`. Bear in mind that positions 6, 7, and 8 of the resulting tuple carry nothing usable.

`email.utils.parsedate_tz(*date*)`

Does the same job as `parsedate()`, only it returns `None` or else a 10-tuple; the leading 9 entries form a tuple you can pass straight into [`time.mktime()`](https://docs.python.org/3.14/library/time.html#time.mktime), while the tenth gives the date's timezone offset away from UTC (the official name for Greenwich Mean Time) [1]. Should the input string lack any timezone, the final entry of the returned tuple is `0`, standing for UTC. Bear in mind that positions 6, 7, and 8 of the resulting tuple carry nothing usable.

`email.utils.parsedate_to_datetime(*date*)`

Running counter to `format_datetime()`, it does the same job as `parsedate()` but on success yields a [`datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime); otherwise a `ValueError` gets raised whenever *date* holds something invalid, such as an hour above 23 or a timezone offset falling outside -24 to 24 hours. When the input date carries a timezone of `-0000`, the `datetime` you receive is a naive `datetime`, and provided the date follows the RFCs it stands for a UTC time while saying nothing about the message's true originating timezone. For any other valid timezone offset on the input, the `datetime` is an aware `datetime` bearing the matching [`timezone`](https://docs.python.org/3.14/library/datetime.html#datetime.timezone) [`tzinfo`](https://docs.python.org/3.14/library/datetime.html#datetime.tzinfo).

Added in version 3.3.

[Subject index](INDEX.md) · [Continue](email-utils-mktime-tz-to-email-utils-decode-params.md)
