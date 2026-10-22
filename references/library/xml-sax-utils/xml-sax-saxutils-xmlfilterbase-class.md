# xml.sax.saxutils: `xml.sax.saxutils.XMLFilterBase`

*class *xml.sax.saxutils.XMLFilterBase(*base*)

This class is designed to be positioned between an [`XMLReader`](https://docs.python.org/3.14/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader) and the event handlers of the client application. Out of the box it merely forwards requests upward to the reader and events downward to the handlers untouched, yet a subclass can override particular methods so as to reshape the event stream or the configuration requests in transit.

[Subject index](INDEX.md) · [Previous](xml-sax-saxutils-xmlgenerator-class.md) · [Continue](xml-sax-saxutils-prepare-input-source.md)
