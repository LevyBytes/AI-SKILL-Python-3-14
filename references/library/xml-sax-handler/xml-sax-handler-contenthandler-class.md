# xml.sax.handler: `xml.sax.handler.ContentHandler`

## xml.sax.handler — Base classes for SAX handlers??

### `xml.sax.handler` — Base classes for SAX handlers

**Source code:** [Lib/xml/sax/handler.py](https://github.com/python/cpython/tree/3.14/Lib/xml/sax/handler.py)

---

Five categories of handlers are defined by the SAX API: content handlers, DTD handlers, error handlers, entity resolvers and lexical handlers. As a rule applications only have to implement the interfaces whose events matter to them; the interfaces can live in one object or be spread across several objects. So that every method receives a default implementation, handler implementations ought to derive from the base classes that the module `xml.sax.handler` supplies.

 *class *xml.sax.handler.ContentHandler

In SAX this is the primary callback interface, and the one that matters most to applications. The sequence of events on this interface follows the sequence of the information within the document.

[Subject index](INDEX.md) · [Continue](xml-sax-handler-dtdhandler-class.md)
