# email.message.EmailMessage: `as_string()`, `__str__()`, `as_bytes()`, `__bytes__()`, `is_multipart()`, `set_unixfrom()`, `get_unixfrom()`, `__len__()`, `__contains__()`, `__getitem__()`, `__setitem__()`

as_string(*unixfrom=False*, *maxheaderlen=None*, *policy=None*)

Produce the whole message flattened into a string. If the optional *unixfrom* is true, the returned string carries the envelope header. The default for *unixfrom* is `False`. To stay compatible with the base [`Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message) class, *maxheaderlen* is allowed, though it defaults to `None`, signifying that the policy's [`max_line_length`](https://docs.python.org/3.14/library/email.policy.html#email.policy.Policy.max_line_length) governs the line length by default. You can supply the *policy* argument to replace the default policy taken from the message instance. Because the given *policy* is handed to the [`Generator`](https://docs.python.org/3.14/library/email.generator.html#email.generator.Generator), this lets you steer some of the formatting the method emits.

If defaults must be supplied to finish converting the message to a string, flattening can prompt modifications to the `EmailMessage` (MIME boundaries, for instance, might be created or altered).

Be aware that this method exists for convenience and might not be the best route for serializing messages in your own application, particularly when several messages are involved. Consult [`email.generator.Generator`](https://docs.python.org/3.14/library/email.generator.html#email.generator.Generator) for a more adaptable serialization API. Be aware too that this method only emits messages serialized as “7 bit clean” whenever [`utf8`](https://docs.python.org/3.14/library/email.policy.html#email.policy.EmailPolicy.utf8) is `False`, which is the default.

Changed in version 3.6: where *maxheaderlen* goes unspecified, the default switched from 0 over to the *max_line_length* value taken from the policy.

 __str__()

Equivalent to `as_string(policy=self.policy.clone(utf8=True))`. Lets `str(msg)` yield a string that holds the serialized message in human-readable form.

Changed in version 3.4: this method was reworked to apply `utf8=True`, so it now emits an [**RFC 6531**](https://datatracker.ietf.org/doc/html/rfc6531.html)-like message representation rather than serving as a plain alias for `as_string()`.

 as_bytes(*unixfrom=False*, *policy=None*)

Produce the whole message flattened into a bytes object. If the optional *unixfrom* is true, the returned string carries the envelope header. The default for *unixfrom* is `False`. You can supply the *policy* argument to replace the default policy taken from the message instance. Because the given *policy* is handed to the [`BytesGenerator`](https://docs.python.org/3.14/library/email.generator.html#email.generator.BytesGenerator), this lets you steer some of the formatting the method emits.

If defaults must be supplied to finish converting the message to a string, flattening can prompt modifications to the `EmailMessage` (MIME boundaries, for instance, might be created or altered).

Be aware that this method exists for convenience and might not be the best route for serializing messages in your own application, particularly when several messages are involved. Consult [`email.generator.BytesGenerator`](https://docs.python.org/3.14/library/email.generator.html#email.generator.BytesGenerator) for a more adaptable serialization API.

 __bytes__()

Equivalent to `as_bytes()`. Allows `bytes(msg)` to produce a bytes object containing the serialized message.

 is_multipart()

Yield `True` when the message's payload is a list of sub-`EmailMessage` objects, and otherwise yield `False`. Whenever `is_multipart()` yields `False`, the payload ought to be a string object (possibly a CTE encoded binary payload). Keep in mind that `is_multipart()` yielding `True` does not always imply that “msg.get_content_maintype() == ‘multipart’” will yield the `True`. As an example, `is_multipart` will yield `True` whenever the `EmailMessage` carries the type `message/rfc822`.

 set_unixfrom(*unixfrom*)

Assign the message's envelope header to *unixfrom*, which ought to be a string. (Refer to [`mboxMessage`](https://docs.python.org/3.14/library/mailbox.html#mailbox.mboxMessage) for a short account of this header.)

 get_unixfrom()

Yield the message's envelope header. Falls back to `None` when the envelope header was never assigned.

The methods below provide the mapping-like interface for reaching the message's headers. Bear in mind there are a few semantic distinctions between these methods and an ordinary mapping (that is, dictionary) interface. As an example, a dictionary holds no duplicate keys, yet duplicate message headers can occur here. Likewise, dictionaries promise no particular order for the keys that `keys()` returns, but in an `EmailMessage` object the headers always come back in the order they showed up in the original message, or the order in which they were later added. A header that is deleted and then re-added is always tacked onto the end of the header list.

Those semantic distinctions are deliberate and lean toward convenience for the most frequent use cases.

Bear in mind that in every case the mapping interface omits any envelope header the message holds.

 __len__()

Yield the overall count of headers, duplicates included.

 __contains__(*name*)

Yield `True` when the message object holds a field called *name*. Matching ignores case and *name* leaves off the trailing colon. Backs the `in` operator. As an example:

```python
if 'message-id' in myMessage:
   print('Message-ID:', myMessage['message-id'])

```

 __getitem__(*name*)

Yield the value of the named header field. *name* leaves off the colon field separator. When the header is absent, `None` comes back; a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) is never raised.

Bear in mind that when the named field shows up more than once among the message's headers, precisely which of those field values comes back is undefined. Turn to the `get_all()` method to obtain the values of every extant header called *name*.

With the standard policies in play (those other than `compat32`), what comes back is an instance of some subclass of [`email.headerregistry.BaseHeader`](https://docs.python.org/3.14/library/email.headerregistry.html#email.headerregistry.BaseHeader).

 __setitem__(*name*, *val*)

Append a header to the message having field name *name* plus value *val*. That field goes onto the end of the message's existing headers.

Bear in mind this does *not* overwrite or remove any existing header bearing the same name. Should you wish to guarantee that the new header is the sole one in the message with field name *name*, remove the field beforehand, e.g.:

```python
del msg['subject']
msg['subject'] = 'Python roolz!'

```

Should the [`policy`](https://docs.python.org/3.14/library/email.policy.html#module-email.policy) mark certain headers as unique (as the standard policies do), this method can raise a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) whenever you try to assign a value to such a header that already exists. That behavior is deliberate for the sake of consistency, but you should not rely on it, since we might decide in the future to have such assignments automatically delete the existing header.

[Subject index](INDEX.md) · [Previous](email-message-emailmessage-class.md) · [Continue](email-message-header-deletion-and-default-type.md) · [Owning module, declaration or section: email.message](email-message-emailmessage-class.md) · [Owning module, declaration or section: email.message.EmailMessage](email-message-emailmessage-class.md)
