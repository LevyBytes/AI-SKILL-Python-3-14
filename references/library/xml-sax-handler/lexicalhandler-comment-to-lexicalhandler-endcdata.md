# xml.sax.handler — LexicalHandler Objects

### LexicalHandler Objects

Optional SAX2 handler for lexical events.

This handler serves to acquire lexical information about an XML document. Such lexical information spans details about the document encoding in use along with XML comments embedded inside the document, together with section boundaries marking the DTD and marking any CDATA sections. One uses the lexical handlers exactly as one uses content handlers.

Set the LexicalHandler of an XMLReader by applying the setProperty method with the property identifier `'http://xml.org/sax/properties/lexical-handler'`.

 LexicalHandler.comment(*content*)

Reports a comment located anywhere within the document (the DTD included, as well as outside the document element).

 LexicalHandler.startDTD(*name*, *public_id*, *system_id*)

Reports where the DTD declarations begin whenever an associated DTD accompanies the document.

 LexicalHandler.endDTD()

Reports the end of DTD declaration.

 LexicalHandler.startCDATA()

Reports the start of a CDATA marked section.

Whatever the CDATA marked section contains gets reported by way of the characters handler.

 LexicalHandler.endCDATA()

Reports the end of a CDATA marked section.

[Subject index](INDEX.md) · [Previous](errorhandler-error-to-errorhandler-warning.md) · [Owning module, declaration or section: xml.sax.handler](xml-sax-handler-contenthandler-class.md)
