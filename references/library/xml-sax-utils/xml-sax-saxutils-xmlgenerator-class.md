# xml.sax.saxutils: `xml.sax.saxutils.XMLGenerator`

*class *xml.sax.saxutils.XMLGenerator(*out=None*, *encoding='iso-8859-1'*, *short_empty_elements=False*)

This class implements the [`ContentHandler`](https://docs.python.org/3.14/library/xml.sax.handler.html#xml.sax.handler.ContentHandler) interface by writing SAX events back out into an XML document. Said another way, supplying an `XMLGenerator` as the content handler reconstructs whatever original document is under parse. *out* should be a file-like object whose default is *sys.stdout*. *encoding* names the output stream's encoding, defaulting to `'iso-8859-1'`. *short_empty_elements* controls how elements with no content are formatted: at `False` (the default) such an element emits as a paired start/end tag, while at `True` it emits as one self-closed tag.

Changed in version 3.2: Added the *short_empty_elements* parameter.

[Subject index](INDEX.md) · [Previous](xml-sax-saxutils-escape-to-xml-sax-saxutils-quoteattr.md) · [Continue](xml-sax-saxutils-xmlfilterbase-class.md)
