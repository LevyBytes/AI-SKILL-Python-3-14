# email.message.Message: `del_param()`, `set_type()`, `get_filename()`, `get_boundary()`, `set_boundary()`, `get_content_charset()`, `get_charsets()`, `get_content_disposition()`

When *replace* is `False` — its default — the header gets shifted to the tail of the header list. Set *replace* to `True` instead and the header is amended where it already sits.

Changed in version 3.4: `replace` keyword was added.

 del_param(*param*, *header='content-type'*, *requote=True*)

Strip the named parameter out of the *Content-Type* header entirely. That header is then rebuilt on the spot, now lacking both the parameter and its value. Quoting is applied to values wherever needed unless *requote* equals `False` (it defaults to `True`). The optional *header* lets you point at something other than *Content-Type*.

 set_type(*type*, *header='Content-Type'*, *requote=True*)

Assign the primary type together with the subtype on the *Content-Type* header. The *type* you pass has to be a string shaped like *maintype/subtype*; fail that and a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) results.

What this method does is swap out the *Content-Type* header while every parameter stays untouched. With *requote* set to `False`, the quoting already on the header is preserved as-is; otherwise (the default) the parameters get quoted.

Through the *header* argument you may name a different header to act on. Setting the *Content-Type* header also brings a *MIME-Version* header along with it.

Consider this a legacy method. Over on the [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage) class, the same job is handled by the `make_` and `add_` methods instead.

 get_filename(*failobj=None*)

Hand back the value held by the `filename` parameter on the message’s *Content-Disposition* header. Where that header carries no `filename` parameter, the method instead checks the `name` parameter over on the *Content-Type* header. With neither present, or the header itself absent, *failobj* comes back. Whatever string is returned arrives unquoted, following [`email.utils.unquote()`](https://docs.python.org/3.14/library/email.utils.html#email.utils.unquote).

 get_boundary(*failobj=None*)

Hand back the value sitting in the `boundary` parameter of the message’s *Content-Type* header; failing that — header gone or no `boundary` parameter on it — return *failobj*. As ever the string that comes back is unquoted, per [`email.utils.unquote()`](https://docs.python.org/3.14/library/email.utils.html#email.utils.unquote).

 set_boundary(*boundary*)

Point the `boundary` parameter on the *Content-Type* header at *boundary*. Should quoting be required, `set_boundary()` applies it to *boundary* every time. When the message object lacks a *Content-Type* header, a [`HeaderParseError`](https://docs.python.org/3.14/library/email.errors.html#email.errors.HeaderParseError) gets raised.

Be aware this method behaves a touch differently from dropping the former *Content-Type* header and inserting a fresh one carrying the new boundary through `add_header()`: `set_boundary()` keeps the *Content-Type* header in its original spot within the header list. That said, it makes *no* effort to retain whatever continuation lines the original *Content-Type* header may have held.

 get_content_charset(*failobj=None*)

Hand back the *Content-Type* header’s `charset` parameter, forced to lower case. Where no *Content-Type* header exists, or where it carries no `charset` parameter, *failobj* comes back instead.

Do note the contrast with `get_charset()`, which yields the [`Charset`](https://docs.python.org/3.14/library/email.charset.html#email.charset.Charset) instance tied to the message body’s default encoding.

 get_charsets(*failobj=None*)

Hand back a list of the character-set names appearing throughout the message. For a *multipart* message the list holds one entry per subpart in the payload; otherwise it is a list of length 1.

Every entry is a string drawn from the `charset` parameter on that subpart’s *Content-Type* header. Yet whenever a subpart lacks a *Content-Type* header, lacks a `charset` parameter, or sits outside the *text* main MIME type, the corresponding spot in the returned list holds *failobj*.

 get_content_disposition()

Hand back the message’s *Content-Disposition* header value lowercased and stripped of parameters, when such a header is present, or else `None`. Assuming the message conforms to [**RFC 2183**](https://datatracker.ietf.org/doc/html/rfc2183.html), the outcomes you can expect here are *inline*, *attachment*, or `None`.

Added in version 3.5.

[Subject index](INDEX.md) · [Continue](email-message-message-walk.md) · [Owning module, declaration or section: email.message.Message](email-message-message-class.md) · [Owning module, declaration or section: set_param](legacy-message-parameter-access-and-mutation.md) · [Preceding source contract and version conditions](legacy-message-parameter-access-and-mutation.md)
