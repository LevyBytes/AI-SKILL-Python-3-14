# email.header: `email.header.Header`

# Email.Header

### `email.header`: Internationalized headers

**Source code:** [Lib/email/header.py](https://github.com/python/cpython/tree/3.14/Lib/email/header.py)

---

Belonging to the legacy (`Compat32`) email API, this module's work happens out of sight under the current API, where the dictionary-like API of the [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage) class quietly encodes and decodes headers. Beyond serving older code, it still earns its place whenever a program must take full charge of which character sets get used while headers are encoded.

The text that remains in this section is the module's original documentation.

The foundational standard laying out how email messages are formatted is [**RFC 2822**](https://datatracker.ietf.org/doc/html/rfc2822.html). It grew out of the earlier [**RFC 822**](https://datatracker.ietf.org/doc/html/rfc822.html) standard, which took hold back when nearly all email consisted of ASCII characters alone. As a specification, [**RFC 2822**](https://datatracker.ietf.org/doc/html/rfc2822.html) is written on the premise that email holds nothing but 7-bit ASCII characters.

Naturally, once email spread across the globe it took on an international character, so that language-specific character sets are now fair game inside email messages. Since the foundational standard still insists that messages travel as 7-bit ASCII alone, a whole batch of RFCs sprang up to spell out how email carrying non-ASCII characters gets encoded into [**RFC 2822**](https://datatracker.ietf.org/doc/html/rfc2822.html)-compliant form. Among these RFCs are [**RFC 2045**](https://datatracker.ietf.org/doc/html/rfc2045.html), [**RFC 2046**](https://datatracker.ietf.org/doc/html/rfc2046.html), [**RFC 2047**](https://datatracker.ietf.org/doc/html/rfc2047.html), and [**RFC 2231**](https://datatracker.ietf.org/doc/html/rfc2231.html). Support for these standards lives in the [`email`](https://docs.python.org/3.14/library/email.html#module-email) package's `email.header` and [`email.charset`](https://docs.python.org/3.14/library/email.charset.html#module-email.charset) modules.

Should you need non-ASCII characters in your email headers — in the *Subject* or *To* fields, perhaps — reach for the `Header` class and set the field on the [`Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message) object to a `Header` instance rather than handing it a plain string as the header value. Pull the `Header` class in from the `email.header` module. As an example:

```python
>>> from email.message import Message
>>> from email.header import Header
>>> msg = Message()
>>> h = Header('p\xf6stal', 'iso-8859-1')
>>> msg['Subject'] = h
>>> msg.as_string()
'Subject: =?iso-8859-1?q?p=F6stal?=\n\n'

```

See how, in that snippet, we asked for a non-ASCII character in the *Subject* field? It was done by building a `Header` instance and supplying the character set in which the byte string had been encoded. Then, as the resulting [`Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message) instance was flattened, the *Subject* field came out correctly [**RFC 2047**](https://datatracker.ietf.org/doc/html/rfc2047.html) encoded. A MIME-aware mail reader would render that header by way of the embedded ISO-8859-1 character.

The `Header` class is described below:

 *class *email.header.Header(*s=None*, *charset=None*, *maxlinelen=None*, *header_name=None*, *continuation_ws=' '*, *errors='strict'*)

Build a MIME-compliant header capable of holding strings drawn from several different character sets.

The optional *s* supplies the starting header value. With `None` (its default), no starting value is set, and you can add to the header afterward through `append()` method calls. While *s* may be a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) or [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) instance, check the `append()` documentation regarding the semantics.

The optional *charset* does double duty: it carries the same meaning as the *charset* argument of the `append()` method, and it also fixes the default character set for every later `append()` call that leaves *charset* out. When *charset* is absent from the constructor (its default), the `us-ascii` character set stands in both as *s*'s opening charset and as the default for the `append()` calls that follow.

You can state the maximum line length outright through *maxlinelen*. To trim that first line to a shorter limit — making room for the field header that *s* does not contain, *Subject* for instance — give the field's name in *header_name*. *maxlinelen* defaults to 78, while *header_name* defaults to `None`, which means it plays no part in sizing the first line of a long, split header.

The optional *continuation_ws* has to be folding whitespace that complies with [**RFC 2822**](https://datatracker.ietf.org/doc/html/rfc2822.html), and is most often either a space or a hard tab. It gets placed at the front of continuation lines. *continuation_ws* defaults to a lone space character.

The optional *errors* is handed off untouched to the `append()` method.

[Subject index](INDEX.md) · [Continue](email-header-header-append-to-email-header-header-ne.md)
