# email.message.Message: `as_string()`, `__str__()`, `as_bytes()`, `__bytes__()`, `is_multipart()`, `set_unixfrom()`, `get_unixfrom()`, `attach()`, `get_payload()`

as_string(*unixfrom=False*, *maxheaderlen=0*, *policy=None*)

Flatten the whole message into a string and return it. Supplying a true value for the optional *unixfrom* causes the envelope header to appear in the resulting string; *unixfrom* is `False` by default. Because of backward compatibility, *maxheaderlen* starts at `0`, so a different value has to be set explicitly (and this method disregards the *max_line_length* value configured in the policy). Passing the *policy* argument lets you supersede the message instance's default policy. That route gives you a degree of control over the method's formatting, because the chosen *policy* is forwarded to the `Generator`.

When the message is flattened, the `Message` may be altered if defaults have to be supplied to finish converting it into a string (generating or adjusting MIME boundaries, for instance).

Bear in mind this method is offered for convenience and won't necessarily format the message exactly as you'd prefer. As one example, it does not, by default, perform the mangling of lines starting with `From` that the Unix mbox format calls for. If you need more control, create a [`Generator`](https://docs.python.org/3.14/library/email.generator.html#email.generator.Generator) instance and call its [`flatten()`](https://docs.python.org/3.14/library/email.generator.html#email.generator.Generator.flatten) method yourself. As an illustration:

```python
from io import StringIO
from email.generator import Generator
fp = StringIO()
g = Generator(fp, mangle_from_=True, maxheaderlen=60)
g.flatten(msg)
text = fp.getvalue()

```

Should the message object hold binary data that doesn't conform to the RFC standards' encoding, that non-compliant data is swapped for unicode "unknown character" code points. (Refer as well to `as_bytes()` and [`BytesGenerator`](https://docs.python.org/3.14/library/email.generator.html#email.generator.BytesGenerator).)

Changed in version 3.4: the *policy* keyword argument was added.

 __str__()

The same as `as_string()`. Makes `str(msg)` yield a string holding the formatted message.

 as_bytes(*unixfrom=False*, *policy=None*)

Flatten the entire message into a bytes object and return it. Supplying a true value for the optional *unixfrom* causes the envelope header to appear in the returned string; *unixfrom* is `False` by default. Passing the *policy* argument lets you supersede the message instance's default policy. That route gives you a degree of control over the method's formatting, because the chosen *policy* is forwarded to the `BytesGenerator`.

When the message is flattened, the `Message` may be altered if defaults have to be supplied to finish converting it into a string (generating or adjusting MIME boundaries, for instance).

Bear in mind this method is offered for convenience and won't necessarily format the message exactly as you'd prefer. As one example, it does not, by default, perform the mangling of lines starting with `From` that the Unix mbox format calls for. If you need more control, create a [`BytesGenerator`](https://docs.python.org/3.14/library/email.generator.html#email.generator.BytesGenerator) instance and call its [`flatten()`](https://docs.python.org/3.14/library/email.generator.html#email.generator.BytesGenerator.flatten) method yourself. As an illustration:

```python
from io import BytesIO
from email.generator import BytesGenerator
fp = BytesIO()
g = BytesGenerator(fp, mangle_from_=True, maxheaderlen=60)
g.flatten(msg)
text = fp.getvalue()

```

Added in version 3.4.

 __bytes__()

The same as `as_bytes()`. Makes `bytes(msg)` yield a bytes object holding the formatted message.

Added in version 3.4.

 is_multipart()

Yield `True` when the message's payload is a list of sub-`Message` objects, and `False` otherwise. Whenever `is_multipart()` yields `False`, you can expect the payload to be a string object (possibly a CTE encoded binary payload). (Be aware that `is_multipart()` yielding `True` does not in itself guarantee that "msg.get_content_maintype() == 'multipart'" will yield `True`. As an instance, `is_multipart` yields `True` when the `Message` carries type `message/rfc822`.)

 set_unixfrom(*unixfrom*)

Assign the message's envelope header to *unixfrom*, a value that ought to be a string.

 get_unixfrom()

Yield the message's envelope header. Falls back to `None` when the envelope header was never assigned.

 attach(*payload*)

Append the supplied *payload* to the existing payload, which prior to the call has to be `None` or a list of `Message` objects. Once the call finishes, the payload is invariably a list of `Message` objects. Should you instead wish to assign the payload a scalar object (a string, say), reach for `set_payload()`.

This counts as a legacy method. Within the [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage) class, [`set_content()`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage.set_content) together with the associated `make` and `add` methods takes over its role.

 get_payload(*i=None*, *decode=False*)

Yield the present payload, which is a list of `Message` objects whenever `is_multipart()` is `True`, or a string whenever `is_multipart()` is `False`. Should the payload be a list and you mutate that list object, you alter the message's payload directly.

Given the optional argument *i*, `get_payload()` yields the *i*-th element of the payload, numbering from zero, provided `is_multipart()` is `True`. An [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError) is raised whenever *i* is below 0 or at least as large as the count of items in the payload. Should the payload be a string (that is, `is_multipart()` is `False`) while *i* is supplied, a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised.

The optional *decode* serves as a flag stating whether the payload ought to be decoded, in line with the *Content-Transfer-Encoding* header. With `True` set and a non-multipart message, the payload is decoded if that header's value reads `quoted-printable` or `base64`. Under any other encoding, or with the *Content-Transfer-Encoding* header absent, the payload comes back unchanged (undecoded). The value returned is binary data in every one of these cases. With a multipart message and the *decode* flag set to `True`, what comes back is `None`. Should the payload be base64 yet be malformed (padding absent, characters falling outside the base64 alphabet), a fitting defect is appended to the message's defect property ([`InvalidBase64PaddingDefect`](https://docs.python.org/3.14/library/email.errors.html#email.errors.InvalidBase64PaddingDefect) or [`InvalidBase64CharactersDefect`](https://docs.python.org/3.14/library/email.errors.html#email.errors.InvalidBase64CharactersDefect), as the case may be).

With *decode* set to `False` (its default), the body comes back as a string and the *Content-Transfer-Encoding* is left undecoded. That said, when the *Content-Transfer-Encoding* is 8bit, the original bytes are decoded if possible via the `charset` named in the *Content-Type* header, applying the `replace` error handler. With no `charset` named, or with a `charset` the email package fails to recognize, the body is decoded against the default ASCII charset.

This counts as a legacy method. Within the [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage) class, [`get_content()`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage.get_content) along with [`iter_parts()`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage.iter_parts) takes over its role.

[Subject index](INDEX.md) · [Previous](email-message-message-class.md) · [Continue](legacy-message-payload-and-header-mutation.md) · [Owning module, declaration or section: email.message.Message](email-message-message-class.md)
