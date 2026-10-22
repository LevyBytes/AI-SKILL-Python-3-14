# What’s New in Python 2.0 / SAX2 Support — xml.sax.handler

### SAX2 Support

SAX lays out an event-driven interface for parsing XML. Working with SAX means authoring a SAX handler class. Such handler classes derive from the various classes SAX supplies and override several methods that the XML parser then invokes. For instance, the [`startElement()`](https://docs.python.org/3.14/library/xml.sax.handler.html#xml.sax.handler.ContentHandler.startElement) and [`endElement()`](https://docs.python.org/3.14/library/xml.sax.handler.html#xml.sax.handler.ContentHandler.endElement) methods fire for each opening and closing tag the parser meets, the [`characters()`](https://docs.python.org/3.14/library/xml.sax.handler.html#xml.sax.handler.ContentHandler.characters) method fires for each run of character data, and so on.

The benefit of the event-driven style is that the entire document never needs to sit in memory all at once, which is important when you’re working through truly enormous documents. That said, the SAX handler class can become quite intricate if you intend to alter the document’s structure in some elaborate fashion.

For instance, the small example program below sets up a handler that emits a message for each opening and closing tag, then uses it to parse the file `hamlet.xml`:

```python
from xml import sax

class SimpleHandler(sax.ContentHandler):
    def startElement(self, name, attrs):
        print 'Start of element:', name, attrs.keys()

    def endElement(self, name):
        print 'End of element:', name

# Create a parser object
parser = sax.make_parser()

# Tell it what handler to use
handler = SimpleHandler()
parser.setContentHandler( handler )

# Parse a file!
parser.parse( 'hamlet.xml' )

```

For more details, see the Python documentation or the XML HOWTO at [https://pyxml.sourceforge.net/topics/howto/xml-howto.html](https://pyxml.sourceforge.net/topics/howto/xml-howto.html).

[Subject index](INDEX.md) · [Previous source section](xml-modules.md) · [Next source section](dom-support.md) · [Release/subject declaration](introduction.md)
