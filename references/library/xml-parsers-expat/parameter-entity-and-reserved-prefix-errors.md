# xml.parsers.expat: Parameter entities, parser suspension and reserved-prefix errors

xml.parsers.expat.errors.XML_ERROR_INCOMPLETE_PE

Markup inside a parameter entity was incomplete.

 xml.parsers.expat.errors.XML_ERROR_XML_DECL

There was no document element anywhere in the document.

 xml.parsers.expat.errors.XML_ERROR_TEXT_DECL

Parsing a text declaration within an external entity went wrong.

 xml.parsers.expat.errors.XML_ERROR_PUBLICID

The public id held characters that aren't permitted.

 xml.parsers.expat.errors.XML_ERROR_SUSPENDED

The operation was directed at a suspended parser, where it isn't permitted. Trying to feed more input or to halt the parser falls under this.

 xml.parsers.expat.errors.XML_ERROR_NOT_SUSPENDED

There was a try to resume the parser at a moment when it had not been suspended.

 xml.parsers.expat.errors.XML_ERROR_ABORTED

Python applications ought never to see this reported.

 xml.parsers.expat.errors.XML_ERROR_FINISHED

The operation targeted a parser that had already completed parsing its input, where it isn't permitted. This covers efforts to supply more input or to halt the parser.

 xml.parsers.expat.errors.XML_ERROR_SUSPEND_PE

 xml.parsers.expat.errors.XML_ERROR_RESERVED_PREFIX_XML

Something tried to undeclare the reserved namespace prefix `xml`, or to attach it to a different namespace URI.

 xml.parsers.expat.errors.XML_ERROR_RESERVED_PREFIX_XMLNS

Something tried to declare, or to undeclare, the reserved namespace prefix `xmlns`.

[Subject index](INDEX.md) · [Previous](cdata-encoding-and-namespace-errors.md) · [Continue](expat-namespace-and-parser-state-errors.md) · [Owning module, declaration or section: xml.parsers.expat](expat-parser-factory-and-exception.md) · [Owning module, declaration or section: Expat error constants](expat-parse-and-document-structure-errors.md)
