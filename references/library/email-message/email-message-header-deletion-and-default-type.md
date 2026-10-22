# email.message.EmailMessage: `__delitem__()`, `keys()`, `values()`, `items()`, `get()`, `get_all()`, `add_header()`, `replace_header()`, `get_content_type()`, `get_content_maintype()`, `get_content_subtype()`, `get_default_type()`, `set_default_type()`

__delitem__(*name*)

Remove every occurrence of the field named *name* from the message's headers. No exception arises when the named field is absent from the headers.

 keys()

Yield a list of all the message's header field names.

 values()

Yield a list of all the message's field values.

 items()

Yield a list of 2-tuples holding all the message's field headers together with their values.

 get(*name*, *failobj=None*)

Yield the value of the named header field. This matches [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) except that the optional *failobj* comes back when the named header is absent (*failobj* defaults to `None`).

A few more handy header-related methods follow:

 get_all(*name*, *failobj=None*)

Yield a list of every value for the field called *name*. When no such named headers exist in the message, *failobj* comes back (defaults to `None`).

 add_header(*_name*, *_value*, ***_params*)

Extended header setting. This method resembles `__setitem__()` apart from the fact that extra header parameters may be supplied as keyword arguments. *_name* is the header field to append and *_value* is the *primary* value for that header.

For every entry in the keyword argument dictionary *_params*, the key serves as the parameter name, with underscores swapped for dashes (because dashes are not legal in Python identifiers). Ordinarily the parameter is appended as `key="value"`, unless the value is `None`, in which case the key alone is appended.

When the value holds non-ASCII characters, you can spell out the charset and language by giving the value as a three tuple shaped `(CHARSET, LANGUAGE, VALUE)`, where `CHARSET` is a string naming the charset used to encode the value, `LANGUAGE` may usually be set to `None` or the empty string (consult [**RFC 2231**](https://datatracker.ietf.org/doc/html/rfc2231.html) for additional options), and `VALUE` is the string value carrying non-ASCII code points. When no three tuple is given and the value holds non-ASCII characters, it is encoded automatically in [**RFC 2231**](https://datatracker.ietf.org/doc/html/rfc2231.html) format with a `CHARSET` of `utf-8` plus a `LANGUAGE` of `None`.

Here is an example:

```python
msg.add_header('Content-Disposition', 'attachment', filename='bud.gif')

```

This will add a header that looks like

```python
Content-Disposition: attachment; filename="bud.gif"

```

An example of the extended interface with non-ASCII characters:

```python
msg.add_header('Content-Disposition', 'attachment',
               filename=('iso-8859-1', '', 'Fußballer.ppt'))

```

 replace_header(*_name*, *_value*)

Swap out a header. Swap out the first header in the message that matches *_name*, keeping the original header's order and field-name case. Should no matching header turn up, raise a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError).

 get_content_type()

Yield the message's content type, forced to lower case in the form *maintype/subtype*. When the message has no *Content-Type* header, yield whatever `get_default_type()` returns. When the *Content-Type* header is invalid, yield `text/plain`.

(Per [**RFC 2045**](https://datatracker.ietf.org/doc/html/rfc2045.html), messages always carry a default type, so `get_content_type()` always yields a value. [**RFC 2045**](https://datatracker.ietf.org/doc/html/rfc2045.html) sets a message's default type at *text/plain* unless it sits inside a *multipart/digest* container, where it would instead be *message/rfc822*. When the *Content-Type* header carries an invalid type specification, [**RFC 2045**](https://datatracker.ietf.org/doc/html/rfc2045.html) requires the default type to be *text/plain*.)

 get_content_maintype()

Yield the message's main content type. This is the *maintype* portion of the string that `get_content_type()` returns.

 get_content_subtype()

Yield the message's sub-content type. This is the *subtype* portion of the string that `get_content_type()` returns.

 get_default_type()

Yield the default content type. Most messages carry a default content type of *text/plain*, with the exception of messages that are subparts of *multipart/digest* containers. Those subparts carry a default content type of *message/rfc822*.

 set_default_type(*ctype*)

Assign the default content type. *ctype* ought to be either *text/plain* or *message/rfc822*, though this is not enforced. Since the default content type is not held in the *Content-Type* header, it only influences what the `get_content_type` methods return when the message carries no *Content-Type* header.

[Subject index](INDEX.md) · [Previous](email-message-serialization-and-header-assignment.md) · [Continue](email-message-parameters-and-disposition.md) · [Owning module, declaration or section: email.message](email-message-emailmessage-class.md) · [Owning module, declaration or section: email.message.EmailMessage](email-message-emailmessage-class.md)
