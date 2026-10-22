# email.utils: `email.utils.mktime_tz()`, `email.utils.formatdate()`, `email.utils.format_datetime()`, `email.utils.decode_rfc2231()`, `email.utils.encode_rfc2231()`, `email.utils.collapse_rfc2231_value()`, `email.utils.decode_params()`

`email.utils.mktime_tz(*tuple*)`

Convert a 10-tuple of the kind `parsedate_tz()` produces into a UTC timestamp — that is, seconds counted from the Epoch. When the tuple's timezone entry is `None`, local time is assumed.

`email.utils.formatdate(*timeval=None*, *localtime=False*, *usegmt=False*)`

Hands back a date string formatted per [**RFC 2822**](https://datatracker.ietf.org/doc/html/rfc2822.html), for example:

```python
Fri, 09 Nov 2001 01:08:47 -0000

```

When provided, the optional *timeval* is a floating-point time value of the kind [`time.gmtime()`](https://docs.python.org/3.14/library/time.html#time.gmtime) and [`time.localtime()`](https://docs.python.org/3.14/library/time.html#time.localtime) accept; leave it off and the current time fills in.

The optional *localtime* flag, set `True`, reads *timeval* and produces a date keyed to the local timezone in place of UTC, duly factoring in daylight saving time. Its default of `False` means UTC applies.

The optional *usegmt* flag, set `True`, emits a date string whose timezone reads as the ascii string `GMT` rather than a numeric `-0000`. Certain protocols (HTTP among them) require this, and it takes effect solely while *localtime* is `False`. It defaults to `False`.

`email.utils.format_datetime(*dt*, *usegmt=False*)`

Behaves as `formatdate` does, save that what you feed in is a [`datetime`](https://docs.python.org/3.14/library/datetime.html#module-datetime) instance. A naive datetime is read as “UTC with no information about the source timezone”, so the customary `-0000` stands in for the timezone. An aware `datetime` instead supplies the numeric timezone offset. Where it is an aware timezone whose offset is zero, you may set *usegmt* to `True`, and then the string `GMT` replaces that numeric offset. This gives you a route to producing standards-compliant HTTP date headers.

Added in version 3.3.

`email.utils.decode_rfc2231(*s*)`

Decode the string *s* in line with [**RFC 2231**](https://datatracker.ietf.org/doc/html/rfc2231.html).

`email.utils.encode_rfc2231(*s*, *charset=None*, *language=None*)`

Encode the string *s* in line with [**RFC 2231**](https://datatracker.ietf.org/doc/html/rfc2231.html). The optional *charset* and *language*, when present, name the character set and the language to apply. Provide neither and *s* comes back exactly as it went in. Provide *charset* but not *language*, and encoding proceeds with an empty string standing in for *language*.

`email.utils.collapse_rfc2231_value(*value*, *errors='replace'*, *fallback_charset='us-ascii'*)`

Where a header parameter has been encoded in [**RFC 2231**](https://datatracker.ietf.org/doc/html/rfc2231.html) form, [`Message.get_param`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message.get_param) might give you a 3-tuple holding the character set, the language, and the value. `collapse_rfc2231_value()` folds that down into a unicode string. The optional *errors* flows through to the *errors* argument on [`str`](https://docs.python.org/3.14/library/stdtypes.html#str)'s [`encode()`](https://docs.python.org/3.14/library/stdtypes.html#str.encode) method and defaults to `'replace'`. The optional *fallback_charset* picks the character set to fall back on whenever Python doesn't recognize the one named in the [**RFC 2231**](https://datatracker.ietf.org/doc/html/rfc2231.html) header; it defaults to `'us-ascii'`.

As a convenience, when the *value* you pass `collapse_rfc2231_value()` isn't a tuple, it should be a string, and that string comes back unquoted.

`email.utils.decode_params(*params*)`

Decode a parameters list in line with [**RFC 2231**](https://datatracker.ietf.org/doc/html/rfc2231.html). The *params* argument is a sequence of 2-tuples whose members take the form `(content-type, string-value)`.

Footnotes

[Subject index](INDEX.md) · [Previous](email-utils-localtime-to-email-utils-parsedate-to-datetime.md) · [Continue](../ensurepip/ensurepip-bootstrapping-the-pip-installer.md) · [Owning module, declaration or section: email.utils](email-utils-localtime-to-email-utils-parsedate-to-datetime.md)
