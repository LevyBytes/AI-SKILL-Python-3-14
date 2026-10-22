# base64 — Security Considerations

### Security Considerations

[**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html) gained a fresh security considerations section (section 12); going over that security section is advisable for any code you put into production.

See also

Module [`binascii`](https://docs.python.org/3.14/library/binascii.html#module-binascii)

A helper module that holds the ASCII-to-binary and binary-to-ASCII conversions.

[**RFC 1521**](https://datatracker.ietf.org/doc/html/rfc1521.html) - MIME (Multipurpose Internet Mail Extensions), Part One, which covers the mechanisms that specify and describe how internet message bodies are formatted

It is Section 5.2, “Base64 Content-Transfer-Encoding,” that sets out what the base64 encoding is.

[ISO 32000-2 Portable document format - Part 2: PDF 2.0](https://pdfa.org/resource/iso-32000-2/)

It is Section 7.4.3, “ASCII85Decode Filter,” that sets out the Ascii85 encoding employed in PDF and PostScript - covering the output character set together with how data length is held onto by way of zero-padding and partial output groups.

[ZeroMQ RFC 32/Z85](https://rfc.zeromq.org/spec/32/)

Its “Formal Specification” section lays out the character set that Z85 relies on.

[Subject index](INDEX.md) · [Previous](base64-decode-to-base64-encodebytes.md) · [Owning module, declaration or section: base64](base64-base16-base32-base64-base85-data-encodings.md)
