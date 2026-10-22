# xml.parsers.expat: Processing-instruction, syntax, character and encoding errors

xml.parsers.expat.errors.XML_ERROR_MISPLACED_XML_PI

An XML declaration turned up at a position other than the beginning of the input data.

 xml.parsers.expat.errors.XML_ERROR_NO_ELEMENTS

No elements are present in the document (every XML document is required to hold exactly one top-level element)..

 xml.parsers.expat.errors.XML_ERROR_NO_MEMORY

Internally, Expat failed to allocate the memory it needed.

 xml.parsers.expat.errors.XML_ERROR_PARAM_ENTITY_REF

A reference to a parameter entity appeared in a spot where it isn't permitted.

 xml.parsers.expat.errors.XML_ERROR_PARTIAL_CHAR

A partial character turned up within the input.

 xml.parsers.expat.errors.XML_ERROR_RECURSIVE_ENTITY_REF

One entity reference held a further reference back to the very same entity — perhaps under another name, and perhaps by an indirect path.

 xml.parsers.expat.errors.XML_ERROR_SYNTAX

A syntax error of an unspecified kind came up.

 xml.parsers.expat.errors.XML_ERROR_TAG_MISMATCH

An end tag failed to correspond to the innermost open start tag.

 xml.parsers.expat.errors.XML_ERROR_UNCLOSED_TOKEN

A token (a start tag, say) stayed unclosed when the stream ended or when the following token appeared.

 xml.parsers.expat.errors.XML_ERROR_UNDEFINED_ENTITY

Something referenced an entity that had never been defined.

 xml.parsers.expat.errors.XML_ERROR_UNKNOWN_ENCODING

Expat offers no support for the document's encoding.

[Subject index](INDEX.md) · [Previous](expat-parse-and-document-structure-errors.md) · [Continue](cdata-encoding-and-namespace-errors.md) · [Owning module, declaration or section: xml.parsers.expat](expat-parser-factory-and-exception.md) · [Owning module, declaration or section: Expat error constants](expat-parse-and-document-structure-errors.md)
