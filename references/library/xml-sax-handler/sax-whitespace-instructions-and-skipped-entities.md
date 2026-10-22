# xml.sax.handler: `ContentHandler.ignorableWhitespace()`, `ContentHandler.processingInstruction()`, `ContentHandler.skippedEntity()`

ContentHandler.ignorableWhitespace(*whitespace*)

Receive notification of ignorable whitespace in element content.

To report each chunk of ignorable whitespace, Validating Parsers must apply this method (refer to section 2.10 of the W3C XML 1.0 recommendation): non-validating parsers may apply it as well when they are able to parse and use content models.

A SAX parser may deliver all contiguous whitespace within one chunk, or it may divide it across several chunks; even so, every character within any single event must originate from the same external entity, so that the Locator yields useful information.

 ContentHandler.processingInstruction(*target*, *data*)

Receive notification of a processing instruction.

The Parser will call this method once for each processing instruction encountered: note that processing instructions may appear before or after the main document element.

A SAX parser should never report an XML declaration (XML 1.0, section 2.8) or a text declaration (XML 1.0, section 4.3.1) by means of this method.

 ContentHandler.skippedEntity(*name*)

Receive notification of a skipped entity.

For each entity skipped, the Parser invokes this method once. A non-validating processor may skip entities whose declarations it has not seen (because, for instance, the entity was declared in an external DTD subset). Any processor may skip external entities, contingent on the values of the `feature_external_ges` and the `feature_external_pes` properties.

[Subject index](INDEX.md) · [Previous](sax-locator-document-and-character-events.md) · [Continue](dtdhandler-notationdecl-to-dtdhandler-unparsedentitydecl.md) · [Owning module, declaration or section: xml.sax.handler](xml-sax-handler-contenthandler-class.md) · [Owning module, declaration or section: ContentHandler Objects](sax-locator-document-and-character-events.md)
