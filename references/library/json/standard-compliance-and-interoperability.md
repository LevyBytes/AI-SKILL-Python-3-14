# json — Standard Compliance and Interoperability

### Standard Compliance and Interoperability

[**RFC 7159**](https://datatracker.ietf.org/doc/html/rfc7159.html) and [ECMA-404](https://ecma-international.org/publications-and-standards/standards/ecma-404/) lay out the JSON format. What follows describes how closely this module follows the RFC. To keep things simple, `JSONEncoder` and `JSONDecoder` subclasses, along with any parameters not called out directly, are left out of consideration.

The module does not follow the RFC to the letter; it carries certain extensions that count as valid JavaScript yet not as valid JSON. Specifically:

- Infinite and NaN number values are accepted and output;

- An object may repeat a name, and where it does, only the final name-value pair's value is kept.

Given that the RFC lets RFC-compliant parsers take in input texts that themselves are not RFC-compliant, the deserializer here qualifies, technically, as RFC-compliant when run with its default settings.

[Subject index](INDEX.md) · [Previous](json-jsondecodeerror.md) · [Continue](character-encodings.md) · [Owning module, declaration or section: json](json-encoding-and-decoding-overview.md)
