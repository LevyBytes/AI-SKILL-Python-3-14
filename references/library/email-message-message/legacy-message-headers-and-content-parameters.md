# email.message.Message: `get_all()`, `add_header()`, `replace_header()`, `get_content_type()`, `get_content_maintype()`, `get_content_subtype()`, `get_default_type()`, `set_default_type()`, `get_params()`

get_all(*name*, *failobj=None*)

Yield a list of every value for the field named *name*. When the message holds no such named headers, *failobj* comes back (with `None` as the default).

 add_header(*_name*, *_value*, ***_params*)

Extended header setting. This method works much like `__setitem__()` apart from letting you supply extra header parameters via keyword arguments. *_name* is the header field being added and *_value* is the *primary* value for that header.

For every entry in the keyword argument dictionary *_params*, the key serves as the parameter name, with underscores swapped for dashes (because dashes can't appear in Python identifiers). Ordinarily the parameter is added as `key="value"` unless the value is `None`, in which case only the key gets added. Where the value carries non-ASCII characters, you can express it as a three tuple shaped `(CHARSET, LANGUAGE, VALUE)`, in which `CHARSET` is a string naming the charset that encodes the value, `LANGUAGE` can typically be left as `None` or the empty string (consult [**RFC 2231**](https://datatracker.ietf.org/doc/html/rfc2231.html) for the remaining options), and `VALUE` is the string value holding the non-ASCII code points. When no three tuple is supplied yet the value carries non-ASCII characters, it is encoded automatically in [**RFC 2231**](https://datatracker.ietf.org/doc/html/rfc2231.html) format using a `CHARSET` of `utf-8` together with a `LANGUAGE` of `None`.

Here's an example:

```python
msg.add_header('Content-Disposition', 'attachment', filename='bud.gif')

```

This will add a header that looks like

```python
Content-Disposition: attachment; filename="bud.gif"

```

An example with non-ASCII characters:

```python
msg.add_header('Content-Disposition', 'attachment',
               filename=('iso-8859-1', '', 'Fußballer.ppt'))

```

Which produces

```python
Content-Disposition: attachment; filename*="iso-8859-1''Fu%DFballer.ppt"

```

 replace_header(*_name*, *_value*)

Replace a header. Swap out the first header in the message that matches *_name*, keeping both the header order and the field-name case. When no matching header turns up, a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) is raised.

 get_content_type()

Yield the message's content type. The string returned is forced to lower case in the shape *maintype/subtype*. Where the message carried no *Content-Type* header, the default type supplied by `get_default_type()` comes back. Because [**RFC 2045**](https://datatracker.ietf.org/doc/html/rfc2045.html) holds that messages always carry a default type, `get_content_type()` will always hand back a value.

[**RFC 2045**](https://datatracker.ietf.org/doc/html/rfc2045.html) sets a message's default type as *text/plain*, save when it sits within a *multipart/digest* container, where it becomes *message/rfc822*. Where the *Content-Type* header carries an invalid type specification, [**RFC 2045**](https://datatracker.ietf.org/doc/html/rfc2045.html) requires the default type to be *text/plain*.

 get_content_maintype()

Yield the message's main content type. This is the *maintype* portion of the string that `get_content_type()` returns.

 get_content_subtype()

Yield the message's sub-content type. This is the *subtype* portion of the string that `get_content_type()` returns.

 get_default_type()

Yield the default content type. The majority of messages carry a default content type of *text/plain*, apart from those that are subparts of *multipart/digest* containers. Those subparts carry a default content type of *message/rfc822*.

 set_default_type(*ctype*)

Assign the default content type. *ctype* ought to be either *text/plain* or *message/rfc822*, though that is not enforced. The default content type is not kept in the *Content-Type* header.

 get_params(*failobj=None*, *header='content-type'*, *unquote=True*)

Yield the message's *Content-Type* parameters as a list. Each element of the list returned is a 2-tuple of key/value pairs, split at the `'='` sign. The key sits on the left side of the `'='`, while the value sits on the right. Where a parameter lacks any `'='` sign, an empty string serves as its value; in every other case the value follows the description in `get_param()` and is unquoted when the optional *unquote* is `True` (its default).

The optional *failobj* is the object handed back when there is no *Content-Type* header. The optional *header* is the header searched in place of *Content-Type*.

This counts as a legacy method. Within the [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage) class, the *params* property of the individual header objects that the header access methods return takes over its role.

[Subject index](INDEX.md) · [Previous](legacy-message-payload-and-header-mutation.md) · [Continue](legacy-message-parameter-access-and-mutation.md) · [Owning module, declaration or section: email.message.Message](email-message-message-class.md)
