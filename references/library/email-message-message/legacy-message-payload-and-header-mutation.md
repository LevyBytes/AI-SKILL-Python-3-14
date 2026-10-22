# email.message.Message: `set_payload()`, `set_charset()`, `get_charset()`, `__len__()`, `__contains__()`, `__getitem__()`, `__setitem__()`, `__delitem__()`, `keys()`, `values()`, `items()`, `get()`

set_payload(*payload*, *charset=None*)

Assign the complete message object's payload to *payload*. Upholding the payload invariants falls to the client. The optional *charset* establishes the message's default character set; consult `set_charset()` for the specifics.

This counts as a legacy method. Within the [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage) class, [`set_content()`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage.set_content) takes over its role.

 set_charset(*charset*)

Assign the payload's character set to *charset*, which may be a [`Charset`](https://docs.python.org/3.14/library/email.charset.html#email.charset.Charset) instance (refer to [`email.charset`](https://docs.python.org/3.14/library/email.charset.html#module-email.charset)), a string that names a character set, or `None`. A string gets turned into a `Charset` instance. With *charset* given as `None`, the `charset` parameter is stripped from the *Content-Type* header (leaving the message otherwise untouched). Any other input triggers a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

When no *MIME-Version* header is already present, one gets added. When no *Content-Type* header is already present, one gets added carrying a value of *text/plain*. No matter whether the *Content-Type* header is already there, its `charset` parameter is assigned *charset.output_charset*. Where *charset.input_charset* and *charset.output_charset* are not the same, the payload undergoes re-encoding to the *output_charset*. When no *Content-Transfer-Encoding* header is already present, the payload is transfer-encoded, where needed, with the given [`Charset`](https://docs.python.org/3.14/library/email.charset.html#email.charset.Charset), and a header bearing the right value gets added. When a *Content-Transfer-Encoding* header is already present, the payload is taken to already be encoded correctly under that *Content-Transfer-Encoding* and stays unchanged.

This counts as a legacy method. Within the [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage) class, the *charset* parameter of the [`email.message.EmailMessage.set_content()`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage.set_content) method takes over its role.

 get_charset()

Yield the [`Charset`](https://docs.python.org/3.14/library/email.charset.html#email.charset.Charset) instance tied to the message's payload.

This counts as a legacy method. Within the [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage) class it consistently yields `None`.

The methods that follow provide a mapping-like interface for reaching the message's [**RFC 2822**](https://datatracker.ietf.org/doc/html/rfc2822.html) headers. Keep in mind that a few semantic distinctions set these methods apart from an ordinary mapping (that is, dictionary) interface. To illustrate, a dictionary holds no duplicate keys, yet here duplicate message headers can occur. Likewise, dictionaries promise no particular ordering for the keys that `keys()` hands back, whereas in a `Message` object headers always come back in the order they had in the original message or in the order they were later added to it. Whenever a header is deleted and afterward re-added, it always lands at the end of the header list.

These semantic distinctions are deliberate and lean toward greatest convenience.

Keep in mind that, in every case, any envelope header the message holds stays out of the mapping interface.

Within a model built from bytes, any header values that (against the RFCs) carry non-ASCII bytes are, once fetched through this interface, presented as [`Header`](https://docs.python.org/3.14/library/email.header.html#email.header.Header) objects whose charset is `unknown-8bit`.

 __len__()

Yield the overall count of headers, duplicates included.

 __contains__(*name*)

Yield `True` when the message object carries a field called *name*. The match ignores case, and *name* should leave off the trailing colon. Backs the `in` operator, for instance:

```python
if 'message-id' in myMessage:
   print('Message-ID:', myMessage['message-id'])

```

 __getitem__(*name*)

Yield the value held by the named header field. *name* should leave off the colon field separator. With the header absent, `None` comes back; a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) is never raised.

Keep in mind that when the named field shows up more than once among the message's headers, which of those field values comes back is undefined. Turn to the `get_all()` method to obtain the values of every one of the named headers present.

 __setitem__(*name*, *val*)

Place a header on the message with field name *name* and value *val*. The field gets appended after the message's existing fields.

Keep in mind this does *not* overwrite or remove any existing header sharing the same name. If you mean to guarantee that the new header is the sole one in the message bearing field name *name*, remove the field beforehand, for instance:

```python
del msg['subject']
msg['subject'] = 'Python roolz!'

```

 __delitem__(*name*)

Remove every occurrence of the field named *name* from the message's headers. When the named field is not among the headers, no exception is raised.

 keys()

Yield a list holding all of the message's header field names.

 values()

Yield a list holding all of the message's field values.

 items()

Yield a list of 2-tuples that hold all of the message's field headers paired with their values.

 get(*name*, *failobj=None*)

Yield the value held by the named header field. This matches [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) save that the optional *failobj* comes back when the named header is absent (with `None` as the default).

A few more handy methods follow:

[Subject index](INDEX.md) · [Previous](legacy-message-serialization-and-payload-access.md) · [Continue](legacy-message-headers-and-content-parameters.md) · [Owning module, declaration or section: email.message.Message](email-message-message-class.md)
