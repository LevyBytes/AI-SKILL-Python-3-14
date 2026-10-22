# email.errors: Malformed headers, multipart structure and base64 defects

*exception *email.errors.MalformedHeaderDefect

A header surfaced that either lacked a colon or was malformed in some other way.

Deprecated since version 3.3: Across a number of Python releases now, this defect has gone unused.

 *exception *email.errors.MultipartInvariantViolationDefect

A message asserted that it was a *multipart*, yet no subparts turned up. Be aware that for a message carrying this defect, its [`is_multipart()`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message.is_multipart) method can return `False` even while its content type asserts *multipart*.

 *exception *email.errors.InvalidBase64PaddingDefect

While decoding a block of base64 encoded bytes, the padding came out wrong. Sufficient padding is supplied so the decode can run, but the bytes that result may be invalid.

 *exception *email.errors.InvalidBase64CharactersDefect

While decoding a block of base64 encoded bytes, characters lying outside the base64 alphabet came up. Such characters are skipped, but the bytes that result may be invalid.

 *exception *email.errors.InvalidBase64LengthDefect

While decoding a block of base64 encoded bytes, the count of non-padding base64 characters was invalid (one beyond a multiple of 4). The encoded block was left untouched.

 *exception *email.errors.InvalidDateDefect

Arises while decoding a date field that is invalid or cannot be parsed. The original value is left untouched.

[Subject index](INDEX.md) · [Previous](email-parse-errors-and-header-separator-defects.md) · [Owning module, declaration or section: email.errors](email-parse-errors-and-header-separator-defects.md)
