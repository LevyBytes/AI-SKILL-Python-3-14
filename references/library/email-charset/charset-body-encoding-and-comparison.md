# email.charset.Charset: `get_body_encoding()`, `get_output_charset()`, `header_encode()`, `header_encode_lines()`, `body_encode()`, `__str__()`, `__eq__()`, `__ne__()`

input_charset

Holds the character set that was originally given. Widely used aliases get mapped onto their *official* email names — for instance, `latin_1` becomes `iso-8859-1`. When nothing is supplied, the default is 7-bit `us-ascii`.

 header_encoding

Whenever the character set needs encoding before an email header can carry it, this attribute takes the value `charset.QP` (meaning quoted-printable), `charset.BASE64` (meaning base64 encoding), or `charset.SHORTEST` to pick whichever of QP or BASE64 comes out shorter. If no such encoding is needed, the attribute holds `None`.

 body_encoding

This mirrors *header_encoding*, except it covers the encoding applied to the body of the mail message, and that can genuinely differ from whatever the header uses. Note that *body_encoding* will not accept `charset.SHORTEST`.

 output_charset

A number of character sets require conversion ahead of being placed into email headers or bodies. Where the *input_charset* falls into that group, this attribute names the character set into which the output is to be converted. In every other case it stays `None`.

 input_codec

Identifies the Python codec that converts the *input_charset* over to Unicode. Where no conversion codec is required, this attribute is `None`.

 output_codec

Identifies the Python codec that turns Unicode into the *output_charset*. Should no conversion codec be required, this attribute simply matches the value held by *input_codec*.

Beyond those, every `Charset` instance carries the methods below:

 get_body_encoding()

Yields the content transfer encoding that body encoding relies on.

What comes back is either the string `quoted-printable` or `base64`, whichever the chosen encoding dictates — or else a function, and when it is a function you invoke it passing one argument, namely the Message object under encoding. That function takes responsibility for setting the *Content-Transfer-Encoding* header to whatever value suits.

When *body_encoding* equals `QP` the result is the string `quoted-printable`; when it equals `BASE64` the result is the string `base64`; and in any remaining case the string `7bit` comes back.

 get_output_charset()

Return the output character set.

Provided the *output_charset* attribute is something other than `None`, that is what you get; failing that, *input_charset* is returned.

 header_encode(*string*)

Header-encode the string *string*.

Which encoding gets applied — base64 or quoted-printable — follows from the *header_encoding* attribute.

 header_encode_lines(*string*, *maxlengths*)

Header-encodes a *string*, but only after turning it into bytes beforehand.

It resembles `header_encode()`, the difference being that the string is packed to respect maximum line lengths dictated by the *maxlengths* argument. That argument has to be an iterator, and every item it yields supplies the next maximum line length in turn.

 body_encode(*string*)

Body-encode the string *string*.

The encoding selected here — whether base64 or quoted-printable — is governed by the *body_encoding* attribute.

On top of all that, the `Charset` class supplies several methods that back standard operations together with built-in functions.

 __str__()

Hands back *input_charset* rendered as a lowercase string. The name `__repr__()` simply aliases `__str__()`.

 __eq__(*other*)

Use this method to test whether a pair of `Charset` instances are equal.

 __ne__(*other*)

This method lets you check a pair of `Charset` instances for inequality.

For registering fresh entries in the global character set, alias, and codec registries, the `email.charset` module additionally offers the functions below:

[Subject index](INDEX.md) · [Previous](email-charset-charset-class.md) · [Continue](email-charset-add-charset-to-email-charset-add-codec.md) · [Owning module, declaration or section: email.charset](email-charset-charset-class.md) · [Owning module, declaration or section: email.charset.Charset](email-charset-charset-class.md)
