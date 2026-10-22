# xml.sax.saxutils: `xml.sax.saxutils.prepare_input_source()`

xml.sax.saxutils.prepare_input_source(*source*, *base=''*)

Given an input source together with an optional base URL, this function yields a fully resolved [`InputSource`](https://docs.python.org/3.14/library/xml.sax.reader.html#xml.sax.xmlreader.InputSource) object that is ready to read. You may hand the input source over as a string, a file-like object, or an `InputSource` object; parsers lean on this function to realize the polymorphic *source* argument of their [`parse()`](https://docs.python.org/3.14/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader.parse) method.

[Subject index](INDEX.md) · [Previous](xml-sax-saxutils-xmlfilterbase-class.md)
