# xml.parsers.expat: Reserved namespaces, parser state and amplification errors

xml.parsers.expat.errors.XML_ERROR_RESERVED_NAMESPACE_URI

Something tried to attach the URI belonging to one of the reserved namespace prefixes `xml` and `xmlns` onto a different namespace prefix.

 xml.parsers.expat.errors.XML_ERROR_INVALID_ARGUMENT

Python applications ought never to see this reported.

 xml.parsers.expat.errors.XML_ERROR_NO_BUFFER

Python applications ought never to see this reported.

 xml.parsers.expat.errors.XML_ERROR_AMPLIFICATION_LIMIT_BREACH

The cap on the input amplification factor (arising from DTD and entities) was exceeded.

 xml.parsers.expat.errors.XML_ERROR_NOT_STARTED

An effort to stop or suspend the parser happened before it had started.

Added in version 3.14.

Footnotes

[Subject index](INDEX.md) · [Previous](parameter-entity-and-reserved-prefix-errors.md) · [Owning module, declaration or section: xml.parsers.expat](expat-parser-factory-and-exception.md) · [Owning module, declaration or section: Expat error constants](expat-parse-and-document-structure-errors.md)
