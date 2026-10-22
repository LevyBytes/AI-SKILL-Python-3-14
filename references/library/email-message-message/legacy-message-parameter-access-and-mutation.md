# email.message.Message: `get_param()`, `set_param()`

get_param(*param*, *failobj=None*, *header='content-type'*, *unquote=True*)

Yield, as a string, the value of the *Content-Type* header's parameter *param*. When the message carries no *Content-Type* header or no such parameter exists, *failobj* comes back (with `None` as the default).

The optional *header*, when supplied, names the message header to consult in place of *Content-Type*.

Parameter keys are always compared without regard to case. What comes back can be either a string or a 3-tuple should the parameter have been [**RFC 2231**](https://datatracker.ietf.org/doc/html/rfc2231.html) encoded. As a 3-tuple, the value's elements take the form `(CHARSET, LANGUAGE, VALUE)`. Note that both `CHARSET` and `LANGUAGE` may be `None`, and in that event you should regard `VALUE` as encoded in the `us-ascii` charset. `LANGUAGE` can usually be disregarded.

Should your application not mind whether [**RFC 2231**](https://datatracker.ietf.org/doc/html/rfc2231.html) encoding was applied to the parameter, collapsing of the parameter value is available: hand the return value from `get_param()` to [`email.utils.collapse_rfc2231_value()`](https://docs.python.org/3.14/library/email.utils.html#email.utils.collapse_rfc2231_value). That call yields a suitably decoded Unicode string where the value is a tuple, or the original string unquoted where it is not. For example:

```python
rawparam = msg.get_param('foo')
param = email.utils.collapse_rfc2231_value(rawparam)

```

Whatever the case, the parameter value (be it the string returned or the `VALUE` item within the 3-tuple) is always unquoted, except where *unquote* is set to `False`.

This counts as a legacy method. Within the [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage) class, the *params* property of the individual header objects that the header access methods return takes over its role.

 set_param(*param*, *value*, *header='Content-Type'*, *requote=True*, *charset=None*, *language=''*, *replace=False*)

Set a parameter within the *Content-Type* header. Where the parameter is already in the header, its value is overwritten with *value*. Where the *Content-Type* header has not yet been defined for this message, it is set to *text/plain* and the new parameter value is appended in keeping with [**RFC 2045**](https://datatracker.ietf.org/doc/html/rfc2045.html).

The optional *header* names an alternative header to *Content-Type*, and every parameter is quoted where needed unless the optional *requote* is `False` (the default being `True`).

When the optional *charset* is supplied, the parameter is encoded per [**RFC 2231**](https://datatracker.ietf.org/doc/html/rfc2231.html). The optional *language* gives the RFC 2231 language; its default is an empty string. Strings are what both *charset* and *language* ought to be.

[Subject index](INDEX.md) · [Previous](legacy-message-headers-and-content-parameters.md) · [Owning module, declaration or section: email.message.Message](email-message-message-class.md) · [Required continuation of the source contract](legacy-message-parameters-and-content-disposition.md)
