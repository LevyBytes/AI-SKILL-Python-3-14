# xml.sax.xmlreader: `xml.sax.xmlreader.IncrementalParser`

*class *xml.sax.xmlreader.IncrementalParser

In certain situations, parsing an input source all at once is undesirable, and feeding chunks of the document as they become available is preferable. Note that the reader will normally not read the whole file either, but read it in chunks too; even so, `parse()` won't return until the whole document has been processed. Hence these interfaces should be used whenever the blocking behaviour of `parse()` is undesirable.

Once the parser has been instantiated, it stands ready to start accepting data from the feed method right away. After parsing wraps up with a call to close, the reset method must be invoked to make the parser ready to take new data, whether from feed or via the parse method.

Note that these methods must *not* be invoked while parsing is underway, in other words once parse has been called and before its return.

By default, as a convenience to SAX 2.0 driver writers, the class additionally implements the XMLReader interface's parse method by means of the feed, close and reset methods belonging to the IncrementalParser interface.

[Subject index](INDEX.md) · [Previous](xml-sax-xmlreader-xmlreader-class.md) · [Continue](xml-sax-xmlreader-locator-class.md)
