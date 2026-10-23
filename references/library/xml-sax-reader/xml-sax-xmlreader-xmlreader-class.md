# xml.sax.xmlreader: `xml.sax.xmlreader.XMLReader`

## xml.sax.xmlreader - Interface for XML parsers??

### `xml.sax.xmlreader` - Interface for XML parsers

**Source code:** [Lib/xml/sax/xmlreader.py](https://github.com/python/cpython/tree/3.14/Lib/xml/sax/xmlreader.py)

---

The `XMLReader` interface is implemented by SAX parsers. They are realized within a Python module that has to expose a function `create_parser()`. With no arguments, [`xml.sax.make_parser()`](https://docs.python.org/3.14/library/xml.sax.html#xml.sax.make_parser) calls this function to build a new parser object.

 *class *xml.sax.xmlreader.XMLReader

Base class which can be inherited by SAX parsers.

[Subject index](INDEX.md) · [Continue](xml-sax-xmlreader-incrementalparser-class.md) · [Owning module, declaration or section: xml.sax](../xml-sax/xml-sax-make-parser-to-xml-sax-saxnotsupportedexception.md)
