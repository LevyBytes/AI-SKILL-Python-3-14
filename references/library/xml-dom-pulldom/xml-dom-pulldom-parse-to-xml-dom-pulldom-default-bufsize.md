# xml.dom.pulldom: `xml.dom.pulldom.parse()`, `xml.dom.pulldom.parseString()`, `xml.dom.pulldom.default_bufsize`

xml.dom.pulldom.parse(*stream_or_string*, *parser=None*, *bufsize=None*)

Give back a `DOMEventStream` produced from the input you pass. The *stream_or_string* can be a file name or a file-like object. When *parser* is supplied, it has to be an [`XMLReader`](https://docs.python.org/3.14/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader) object. The function replaces that parser's document handler and turns namespace support on; any further parser setup, like configuring an entity resolver, has to be in place beforehand.

Where your XML lives in a string already, reach for the `parseString()` function in its place:

 xml.dom.pulldom.parseString(*string*, *parser=None*)

Give back a `DOMEventStream` standing in for the (Unicode) *string*.

 xml.dom.pulldom.default_bufsize

The fallback value taken by the *bufsize* parameter of `parse()`.

You may reset this variable's value ahead of any `parse()` call, and the updated value will be honored.

[Subject index](INDEX.md) · [Previous](xml-dom-pulldom-sax2dom-class.md) · [Continue](xml-dom-pulldom-domeventstream-class.md) · [Owning module, declaration or section: xml.dom.pulldom](xml-dom-pulldom-support-for-building-partial-dom-trees.md)
