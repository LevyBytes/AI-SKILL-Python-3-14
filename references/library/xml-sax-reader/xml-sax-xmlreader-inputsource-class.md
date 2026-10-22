# xml.sax.xmlreader: `xml.sax.xmlreader.InputSource`

*class *xml.sax.xmlreader.InputSource(*system_id=None*)

Encapsulation of the information the `XMLReader` needs in order to read entities.

This class may carry details covering the public identifier, the system identifier, a byte stream (optionally bundled with character encoding information), and/or an entity's character stream.

Objects of this class get created by applications both to feed into the `XMLReader.parse()` method and to return from EntityResolver.resolveEntity.

An `InputSource` belongs to the application; the `XMLReader` is not permitted to alter `InputSource` objects the application passes to it, though it may make copies and alter those.

[Subject index](INDEX.md) · [Previous](xml-sax-xmlreader-locator-class.md) · [Continue](xml-sax-xmlreader-attributesimpl-class.md)
