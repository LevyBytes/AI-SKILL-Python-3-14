# email.policy: `email.policy.EmailPolicy`, `header_max_count()`, `header_source_parse()`, `header_store_parse()`, `header_fetch_parse()`, `fold()`, `fold_binary()`

*class *email.policy.EmailPolicy(***kw*)

This concrete `Policy` delivers behavior meant to be entirely in line with the present email RFCs. Those take in (though are not restricted to) [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html), [**RFC 2047**](https://datatracker.ietf.org/doc/html/rfc2047.html), and the current MIME RFCs.

This policy introduces fresh algorithms for header parsing and folding. Headers, rather than plain strings, become `str` subclasses carrying attributes that vary with the kind of field. The parsing and folding algorithm fully implement [**RFC 2047**](https://datatracker.ietf.org/doc/html/rfc2047.html) and [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html).

For the `message_factory` attribute, the default value is [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage).

On top of the settable attributes listed earlier that hold for all policies, this policy contributes these further attributes:

Added in version 3.6: [1]

 utf8

When `False`, adhere to [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html), accommodating non-ASCII characters in headers by encoding them into “encoded words”. When `True`, adhere to [**RFC 6532**](https://datatracker.ietf.org/doc/html/rfc6532.html) and apply `utf-8` encoding to headers. Messages built this way may be handed to SMTP servers offering the `SMTPUTF8` extension ([**RFC 6531**](https://datatracker.ietf.org/doc/html/rfc6531.html)).

 refold_source

When a header’s value in the `Message` object came from a [`parser`](https://docs.python.org/3.14/library/email.parser.html#module-email.parser) (rather than having been assigned by a program), this attribute states whether a generator ought to refold that value as it converts the message back into serialized form. The available values are:

| `none` | all source values use original folding |
| --- | --- |
| `long` | any source value carrying a line that exceeds `max_line_length` in length gets refolded |
| `all` | all values are refolded. |

It defaults to `long`.

 header_factory

A callable that receives a pair of arguments — `name` plus `value` — in which `name` denotes a header field name while `value` denotes an unfolded header field value, and that gives back a string subclass standing for that header. A default `header_factory` (refer to [`headerregistry`](https://docs.python.org/3.14/library/email.headerregistry.html#module-email.headerregistry)) ships with the package and handles custom parsing for the assorted address and date [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html) header field types, plus the principal MIME header field stypes. Further custom parsing support is planned for the future.

 content_manager

An object carrying at least two methods: get_content and set_content. Whenever the [`get_content()`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage.get_content) or [`set_content()`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage.set_content) method of an [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage) object runs, it invokes the matching method of this object, handing it the message object as the first argument plus whatever arguments or keywords it itself received as extra arguments. By default `content_manager` points at [`raw_data_manager`](https://docs.python.org/3.14/library/email.contentmanager.html#email.contentmanager.raw_data_manager).

Added in version 3.4.

This class supplies the concrete implementations below for the abstract methods of `Policy`:

 header_max_count(*name*)

Hands back the value of the [`max_count`](https://docs.python.org/3.14/library/email.headerregistry.html#email.headerregistry.BaseHeader.max_count) attribute belonging to the specialized class that represents the header carrying the given name.

 header_source_parse(*sourcelines*)

Everything up to the ‘`:`’ is parsed as the name and handed back without change. The value comes from trimming leading whitespace off what remains of the first line, splicing together all the lines that follow, and clipping off any trailing carriage return or linefeed characters.

 header_store_parse(*name*, *value*)

The name comes back unaltered. Where the supplied value carries a `name` attribute that matches *name* without regard to case, the value comes back unaltered. Otherwise *name* and *value* go to `header_factory`, and the header object it produces is returned as the value. In that situation a `ValueError` is raised if the supplied value holds CR or LF characters.

 header_fetch_parse(*name*, *value*)

Where the value carries a `name` attribute, it comes back to unaltered. Otherwise *name*, together with *value* stripped of any CR or LF characters, go to the `header_factory`, and the header object it produces is returned. Any surrogateescaped bytes are converted into the unicode unknown-character glyph.

 fold(*name*, *value*)

The `refold_source` policy setting governs header folding. A value counts as a ‘source value’ precisely when it lacks a `name` attribute (carrying a `name` attribute marks it as a header object of some kind). Where a source value must be refolded per the policy, it becomes a header object by handing *name* together with *value* stripped of any CR and LF characters to the `header_factory`. A header object is folded by invoking its `fold` method with the current policy.

Source values get broken into lines via [`splitlines()`](https://docs.python.org/3.14/library/stdtypes.html#str.splitlines). Where the value is not to be refolded, the lines are spliced back together with the `linesep` drawn from the policy and returned. The exception is lines that carry non-ascii binary data. There the value is refolded no matter the `refold_source` setting, which makes the binary data get CTE encoded under the `unknown-8bit` charset.

 fold_binary(*name*, *value*)

Identical to `fold()` where `cte_type` is `7bit`, except that the value returned is bytes.

Where `cte_type` is `8bit`, non-ASCII binary data is turned back into bytes. Headers carrying binary data are not refolded, no matter the `refold_header` setting, since there is no way to tell whether that binary data is made of single byte characters or multibyte characters.

The `EmailPolicy` instances below supply defaults fitted to particular application domains. Note that down the road the behavior of these instances (the `HTTP` instance in particular) may be tuned to track the RFCs relevant to their domains even more closely.

[Subject index](INDEX.md) · [Previous](base-policy-header-parsing-and-folding.md) · [Continue](email-policy-default-to-email-policy-strict.md) · [Owning module, declaration or section: email.policy](email-policy-policy-objects.md)
