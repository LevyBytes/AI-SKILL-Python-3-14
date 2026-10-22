# email.charset: `email.charset.Charset`

# Email.Charset

### `email.charset`: Representing character sets

**Source code:** [Lib/email/charset.py](https://github.com/python/cpython/tree/3.14/Lib/email/charset.py)

---

You'll find this module belongs to the older (`Compat32`) email API. Under the newer API, nothing but the aliases table gets consulted.

Everything that follows in this section reproduces the module's documentation as it originally stood.

A `Charset` class lives in this module, standing in for character sets and for the conversions between them inside email messages; alongside it come a character set registry plus a handful of helper methods that let you work with that registry. Several other modules belonging to the [`email`](https://docs.python.org/3.14/library/email.html#module-email) package make use of `Charset` instances.

Pull this class in out of the `email.charset` module.

 *class *email.charset.Charset(*input_charset=DEFAULT_CHARSET*)

Associates each character set with its corresponding email properties.

For any particular character set, this class reports what email demands of that set. It throws in helper routines too, letting you convert from one character set to another whenever the matching codecs happen to be present. Hand it a character set and it tries as hard as it can to tell you how that set should appear within an email message while staying RFC-compliant.

Some character sets, when they appear in email headers or bodies, have to be encoded by way of quoted-printable or base64. Others have to be converted entirely, since email forbids them outright.

The optional *input_charset* behaves as spelled out further down, and it is forced to lower case every time. Once its aliases have been normalized, the value doubles as a key into the character set registry, where the header encoding, body encoding, and output conversion codec for that set are looked up. Say *input_charset* comes in as `iso-8859-1`: then quoted-printable handles both headers and bodies, and no output conversion codec is called for. Should *input_charset* instead be `euc-jp`, base64 encodes the headers, the bodies stay unencoded, and the output text is converted out of the `euc-jp` character set into the `iso-2022-jp` character set.

Each `Charset` instance exposes the data attributes listed here:

[Subject index](INDEX.md) · [Continue](charset-body-encoding-and-comparison.md)
