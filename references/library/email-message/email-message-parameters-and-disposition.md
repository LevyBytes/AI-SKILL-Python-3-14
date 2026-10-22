# email.message.EmailMessage: `set_param()`, `del_param()`, `get_filename()`, `get_boundary()`, `set_boundary()`, `get_content_charset()`, `get_charsets()`, `is_attachment()`, `get_content_disposition()`

set_param(*param*, *value*, *header='Content-Type'*, *requote=True*, *charset=None*, *language=''*, *replace=False*)

Assign a parameter within the *Content-Type* header. Should the parameter already be present in the header, swap its value for *value*. When *header* is `Content-Type` (the default) and that header is not yet in the message, append it, give it the value *text/plain*, and tack on the new parameter value. The optional *header* names an alternative header to *Content-Type*.

When the value holds non-ASCII characters, you can spell out the charset and language with the optional *charset* and *language* parameters. The optional *language* names the [**RFC 2231**](https://datatracker.ietf.org/doc/html/rfc2231.html) language, defaulting to the empty string. Both *charset* and *language* ought to be strings. By default the `utf8` *charset* is used along with `None` for the *language*.

When *replace* is `False` (the default) the header shifts to the end of the header list. When *replace* is `True`, the header is updated in place.

Using the *requote* parameter alongside `EmailMessage` objects is deprecated.

Bear in mind that you can reach existing parameter values of headers through the [`params`](https://docs.python.org/3.14/library/email.headerregistry.html#email.headerregistry.ParameterizedMIMEHeader.params) attribute of the header value (as an example, `msg['Content-Type'].params['charset']`).

Changed in version 3.4: `replace` keyword was added.

 del_param(*param*, *header='content-type'*, *requote=True*)

Strip the named parameter entirely from the *Content-Type* header. The header gets re-written in place lacking the parameter and its value. The optional *header* names an alternative to *Content-Type*.

Using the *requote* parameter alongside `EmailMessage` objects is deprecated.

 get_filename(*failobj=None*)

Yield the value of the `filename` parameter of the message's *Content-Disposition* header. Should that header lack a `filename` parameter, the method instead looks for the `name` parameter on the *Content-Type* header. When neither turns up, or the header is missing, then *failobj* comes back. The returned string is always unquoted as per [`email.utils.unquote()`](https://docs.python.org/3.14/library/email.utils.html#email.utils.unquote).

 get_boundary(*failobj=None*)

Yield the value of the `boundary` parameter of the message's *Content-Type* header, or *failobj* when either the header is missing or it lacks a `boundary` parameter. The returned string is always unquoted as per [`email.utils.unquote()`](https://docs.python.org/3.14/library/email.utils.html#email.utils.unquote).

 set_boundary(*boundary*)

Assign the `boundary` parameter of the *Content-Type* header to *boundary*. `set_boundary()` always quotes *boundary* where necessary. A [`HeaderParseError`](https://docs.python.org/3.14/library/email.errors.html#email.errors.HeaderParseError) arises when the message object carries no *Content-Type* header.

Bear in mind that relying on this method differs subtly from removing the old *Content-Type* header and inserting a fresh one with the new boundary by way of `add_header()`, because `set_boundary()` keeps the position of the *Content-Type* header within the header list.

 get_content_charset(*failobj=None*)

Yield the `charset` parameter of the *Content-Type* header, forced to lower case. When there is no *Content-Type* header, or that header lacks a `charset` parameter, *failobj* comes back.

 get_charsets(*failobj=None*)

Yield a list holding the character set names found in the message. When the message is a *multipart*, the list holds one element per subpart in the payload; otherwise it is a list of length 1.

Every entry in the list is a string giving the value of the `charset` parameter in the *Content-Type* header for the corresponding subpart. When the subpart lacks a *Content-Type* header, lacks a `charset` parameter, or is not of the *text* main MIME type, that entry in the returned list becomes *failobj*.

 is_attachment()

Yield `True` when a *Content-Disposition* header exists and its (case insensitive) value is `attachment`, and `False` otherwise.

Changed in version 3.4.2: is_attachment has become a method rather than a property, to keep it consistent with [`is_multipart()`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message.is_multipart).

 get_content_disposition()

Yield the lowercased value (parameters excluded) of the message's *Content-Disposition* header when it has one, or else `None`. The values this method can produce are *inline*, *attachment*, or `None` when the message conforms to [**RFC 2183**](https://datatracker.ietf.org/doc/html/rfc2183.html).

Added in version 3.5.

The methods below concern examining and manipulating the content (payload) of the message.

[Subject index](INDEX.md) · [Previous](email-message-header-deletion-and-default-type.md) · [Continue](email-message-traversal-and-content-access.md) · [Owning module, declaration or section: email.message](email-message-emailmessage-class.md) · [Owning module, declaration or section: email.message.EmailMessage](email-message-emailmessage-class.md)
