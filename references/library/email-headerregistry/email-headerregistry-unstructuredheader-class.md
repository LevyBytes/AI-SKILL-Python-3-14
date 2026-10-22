# email.headerregistry — `email.headerregistry`: Custom Header Objects

*class *email.headerregistry.UnstructuredHeader

Within [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html), an “unstructured” header is the default header kind. Whenever a header has no syntax specified for it, it counts as unstructured. The textbook case of an unstructured header is the *Subject* header.

Under [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html), an unstructured header amounts to a stretch of arbitrary text drawn from the ASCII character set. [**RFC 2047**](https://datatracker.ietf.org/doc/html/rfc2047.html), though, supplies an [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html) compatible scheme for representing non-ASCII text as ASCII characters inside a header value. When a *value* holding encoded words reaches the constructor, the `UnstructuredHeader` parser turns those encoded words into unicode by applying the [**RFC 2047**](https://datatracker.ietf.org/doc/html/rfc2047.html) rules governing unstructured text. The parser leans on heuristics in an effort to decode some non-compliant encoded words. Defects get recorded in those situations, together with defects for problems like invalid characters showing up within the encoded words or the non-encoded text.

This header type adds no further attributes.

[Subject index](INDEX.md) · [Previous](email-headerregistry-baseheader-fold.md) · [Continue](email-headerregistry-dateheader-class.md) · [Owning module, declaration or section: email.headerregistry](email-headerregistry-baseheader-class.md)
