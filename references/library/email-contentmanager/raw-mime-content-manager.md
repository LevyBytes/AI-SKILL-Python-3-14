# email.contentmanager - Content Manager Instances

### Content Manager Instances

At present the email package ships just a single concrete content manager, `raw_data_manager`, though additional ones could appear later. `raw_data_manager` is the [`content_manager`](https://docs.python.org/3.14/library/email.policy.html#email.policy.EmailPolicy.content_manager) supplied by [`EmailPolicy`](https://docs.python.org/3.14/library/email.policy.html#email.policy.EmailPolicy) together with the policies derived from it.

 email.contentmanager.raw_data_manager

This content manager offers barely more than the interface that [`Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message) already exposes: it handles only text, raw byte strings, and `Message` objects. Even so, it carries real benefits over the base API: calling `get_content` on a text part yields a unicode string with no manual decoding required by the application, `set_content` exposes a broad set of knobs for managing the headers attached to a part and for managing the content transfer encoding, and it unlocks the assorted `add_` methods, which streamlines building multipart messages.

 email.contentmanager.get_content(*msg*, *errors='replace'*)

Hand back the part’s payload, given as a string when it is a `text` part, as an [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage) object for `message/rfc822` parts, or as a `bytes` object for every other non-multipart kind. Invoking this on a `multipart` raises a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError). When the part is a `text` part and *errors* has been supplied, it serves as the error handler while the payload is decoded to unicode. By default that error handler is `replace`.

 email.contentmanager.set_content(*msg*, *<'str'>*, *subtype="plain"*, *charset='utf-8'*, *cte=None*, *disposition=None*, *filename=None*, *cid=None*, *params=None*, *headers=None*)

 email.contentmanager.set_content(*msg*, *<'bytes'>*, *maintype*, *subtype*, *cte="base64"*, *disposition=None*, *filename=None*, *cid=None*, *params=None*, *headers=None*)

 email.contentmanager.set_content(*msg*, *<'EmailMessage'>*, *cte=None*, *disposition=None*, *filename=None*, *cid=None*, *params=None*, *headers=None*)

Attach headers and a payload onto *msg*:

Attach a *Content-Type* header whose value takes the `maintype/subtype` form.

- With `str`, the MIME `maintype` becomes `text`, and the subtype is set to *subtype* when that is given, falling back to `plain` otherwise.

- With `bytes`, the supplied *maintype* and *subtype* are used, and a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised when they have not been given.

- With [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage) objects, the maintype becomes `message`, and the subtype is set to *subtype* when supplied or `rfc822` otherwise. A *subtype* of `partial` triggers an error (you must use `bytes` objects to assemble `message/partial` parts).

When *charset* is given (which only applies to `str`), the string is encoded to bytes under the named character set. Its default is `utf-8`. Where the supplied *charset* is a recognized alias of a standard MIME charset name, the standard charset is substituted.

When *cte* is provided, the payload is encoded with the named content transfer encoding and the *Content-Transfer-Encoding* header is set to that value. The accepted *cte* values are `quoted-printable`, `base64`, `7bit`, `8bit`, and `binary`. Should the input not be encodable under the chosen encoding (for instance, requesting a *cte* of `7bit` for input holding non-ASCII values), a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised.

- With `str` objects, when *cte* is left unset the most compact encoding is chosen by heuristic. Ahead of encoding, [`str.splitlines()`](https://docs.python.org/3.14/library/stdtypes.html#str.splitlines) normalizes every line boundary so that each line of the payload ends with the active policy’s [`linesep`](https://docs.python.org/3.14/library/email.policy.html#email.policy.Policy.linesep) property (even when the original string lacked a trailing one).

- With `bytes` objects, an unset *cte* defaults to base64, and the newline translation just described is skipped.

- With [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage), in line with [**RFC 2046**](https://datatracker.ietf.org/doc/html/rfc2046.html), an error is raised when a *cte* of `quoted-printable` or `base64` is asked for with *subtype* `rfc822`, and for any *cte* besides `7bit` with *subtype* `external-body`. For `message/rfc822`, an unspecified *cte* defaults to `8bit`. For all remaining *subtype* values, `7bit` is used.

Note

A *cte* of `binary` is not yet functioning properly. The `EmailMessage` object that `set_content` produces is itself fine, yet [`BytesGenerator`](https://docs.python.org/3.14/library/email.generator.html#email.generator.BytesGenerator) fails to serialize it the right way.

When *disposition* is given, it becomes the value of the *Content-Disposition* header. When it is omitted but *filename* is given, the header is added with the value `attachment`. When neither *disposition* nor *filename* is supplied, the header is left off. The sole permitted *disposition* values are `attachment` and `inline`.

When *filename* is given, it becomes the value of the `filename` parameter on the *Content-Disposition* header.

When *cid* is given, a *Content-ID* header is added carrying *cid* as its value.

When *params* is given, its `items` method is iterated and the resulting `(key, value)` pairs assign extra parameters onto the *Content-Type* header.

When *headers* is given and is either a list of strings shaped like `headername: headervalue` or a list of `header` objects (told apart from strings by carrying a `name` attribute), those headers are appended to *msg*.

Footnotes

[Subject index](INDEX.md) · [Previous](mime-content-access-and-handler-registration.md) · [Continue](../email-encoders/email-encoders-encode-quopri-to-email-encoders-encode-noop.md) · [Owning module, declaration or section: email.contentmanager](email-contentmanager-contentmanager-class.md)
