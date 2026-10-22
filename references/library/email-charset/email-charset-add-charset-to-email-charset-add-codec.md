# email.charset: `email.charset.add_charset()`, `email.charset.add_alias()`, `email.charset.add_codec()`

email.charset.add_charset(*charset*, *header_enc=None*, *body_enc=None*, *output_charset=None*)

Registers a character set's properties into the global registry.

The *charset* argument supplies the input character set, and it has to be a character set's canonical name.

The optional *header_enc* and *body_enc* each take one of: `charset.QP` for quoted-printable, `charset.BASE64` for base64 encoding, `charset.SHORTEST` to use whichever of quoted-printable or base64 ends up shorter, or `None` when no encoding applies. Only *header_enc* may be given `SHORTEST`. Absent any value, the fallback is `None`, meaning no encoding.

The optional *output_charset* names the character set the output ought to use. Whenever the `Charset.convert()` method runs, conversion moves from the input charset through Unicode and on to the output charset. By default, output stays in whatever character set the input came in as.

Each of *input_charset* and *output_charset* needs a Unicode codec entry within the module's character set-to-codec mapping; when a codec is unfamiliar to the module, register it through `add_codec()`. The [`codecs`](https://docs.python.org/3.14/library/codecs.html#module-codecs) module's documentation has fuller details.

A module-level global dictionary named `CHARSETS` houses the global character set registry.

 email.charset.add_alias(*alias*, *canonical*)

Registers an alias for a character set. The *alias* gives the alias name — for example `latin-1` — while *canonical* gives that character set's canonical name, such as `iso-8859-1`.

That global charset alias registry lives inside the module's global dictionary called `ALIASES`.

 email.charset.add_codec(*charset*, *codecname*)

Registers a codec capable of translating the specified character set's characters both into Unicode and back out of it.

Here *charset* holds a character set's canonical name. The *codecname* holds a Python codec's name, of the kind you would pass as the second argument to the [`encode()`](https://docs.python.org/3.14/library/stdtypes.html#str.encode) method on a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str).

[Subject index](INDEX.md) · [Previous](charset-body-encoding-and-comparison.md) · [Owning module, declaration or section: email.charset](email-charset-charset-class.md)
