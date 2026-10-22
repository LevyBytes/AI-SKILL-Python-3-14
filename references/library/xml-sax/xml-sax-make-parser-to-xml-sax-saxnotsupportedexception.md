# xml.sax — `xml.sax` — Support for SAX2 parsers

### `xml.sax` — Support for SAX2 parsers

**Source code:** [Lib/xml/sax/__init__.py](https://github.com/python/cpython/tree/3.14/Lib/xml/sax/__init__.py)

---

A set of modules implementing the Simple API for XML (SAX) interface for Python is supplied by the `xml.sax` package. The package itself offers the SAX exceptions plus the convenience functions that users of the SAX API will reach for most often.

Note

When the data you intend to parse is untrusted or unauthenticated, consult [XML security](https://docs.python.org/3.14/library/xml.html#xml-security).

Changed in version 3.7.1: To strengthen security, the SAX parser no longer handles general external entities by default. Previously, the parser opened network connections to retrieve remote files or pulled local files off the file system for DTD and entities. You can switch the feature back on through the [`setFeature()`](https://docs.python.org/3.14/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader.setFeature) method on the parser object together with the [`feature_external_ges`](https://docs.python.org/3.14/library/xml.sax.handler.html#xml.sax.handler.feature_external_ges) argument.

These are the convenience functions:

 xml.sax.make_parser(*parser_list=[]*)

Build and return a SAX [`XMLReader`](https://docs.python.org/3.14/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader) object. Whichever parser turns up first gets used. Should *parser_list* be supplied, it has to be an iterable of strings naming modules that expose a function called `create_parser()`. The modules named in *parser_list* take precedence over the modules in the default parser list.

Changed in version 3.8: Any iterable, not merely a list, is now accepted for the *parser_list* argument.

 xml.sax.parse(*filename_or_stream*, *handler*, *error_handler=handler.ErrorHandler()*)

Build a SAX parser and apply it to parse a document. That document, handed in via *filename_or_stream*, may be a filename or a file object. The *handler* parameter has to be a SAX [`ContentHandler`](https://docs.python.org/3.14/library/xml.sax.handler.html#xml.sax.handler.ContentHandler) instance. When *error_handler* is supplied, it must be a SAX [`ErrorHandler`](https://docs.python.org/3.14/library/xml.sax.handler.html#xml.sax.handler.ErrorHandler) instance; when left out, `SAXParseException` will be raised on every error. No value is returned; the *handler* handed in must perform all the work.

 xml.sax.parseString(*string*, *handler*, *error_handler=handler.ErrorHandler()*)

Resembles `parse()`, except that it parses from a buffer *string* taken as a parameter. *string* must be a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) instance or a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object).

Changed in version 3.5: Added support of [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) instances.

Three classes of objects figure in a typical SAX application: readers, handlers and input sources. Here "Reader" is just another word for parser, that is, some chunk of code that reads the bytes or characters out of the input source and yields a stream of events. Those events are then dispatched to the handler objects, that is, the reader calls a method on the handler. A SAX application must therefore acquire a reader object, build or open the input sources, build the handlers, and wire all these objects together. As the closing preparation step, the reader is invoked to parse the input. While parsing runs, methods on the handler objects fire according to structural and syntactic events from the input data.

Only the interfaces of these objects matter; the application itself does not usually instantiate them. Because Python lacks any explicit concept of interface, they are presented formally as classes, yet applications may employ implementations that do not derive from the supplied classes. The [`InputSource`](https://docs.python.org/3.14/library/xml.sax.reader.html#xml.sax.xmlreader.InputSource), [`Locator`](https://docs.python.org/3.14/library/xml.sax.reader.html#xml.sax.xmlreader.Locator), `Attributes`, `AttributesNS`, and [`XMLReader`](https://docs.python.org/3.14/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader) interfaces live in the module [`xml.sax.xmlreader`](https://docs.python.org/3.14/library/xml.sax.reader.html#module-xml.sax.xmlreader). The handler interfaces live in [`xml.sax.handler`](https://docs.python.org/3.14/library/xml.sax.handler.html#module-xml.sax.handler). For convenience, `InputSource` (frequently instantiated directly) along with the handler classes is also reachable from `xml.sax`. The description of these interfaces follows below.

Beyond these classes, `xml.sax` supplies the exception classes below.

 *exception *xml.sax.SAXException(*msg*, *exception=None*)

Wrap an XML error or warning. This class may hold basic error or warning information originating in either the XML parser or the application: it can be subclassed to add functionality or to introduce localization. Note that although the handlers declared in the [`ErrorHandler`](https://docs.python.org/3.14/library/xml.sax.handler.html#xml.sax.handler.ErrorHandler) interface get instances of this exception, actually raising the exception is not mandatory — it also works well as a container for information.

At instantiation, *msg* should be a human-readable description of the error. When supplied, the optional *exception* parameter should be `None` or an exception that the parsing code caught and is forwarding along as information.

This serves as the base class for the remaining SAX exception classes.

 *exception *xml.sax.SAXParseException(*msg*, *exception*, *locator*)

Subclass of `SAXException` raised on parse errors. Instances of this class get handed to the methods of the SAX [`ErrorHandler`](https://docs.python.org/3.14/library/xml.sax.handler.html#xml.sax.handler.ErrorHandler) interface to supply information about the parse error. This class backs the SAX [`Locator`](https://docs.python.org/3.14/library/xml.sax.reader.html#xml.sax.xmlreader.Locator) interface in addition to the `SAXException` interface.

 *exception *xml.sax.SAXNotRecognizedException(*msg*, *exception=None*)

Subclass of `SAXException` raised when a SAX [`XMLReader`](https://docs.python.org/3.14/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader) meets an unrecognized feature or property. SAX applications and extensions may put this class to similar use.

 *exception *xml.sax.SAXNotSupportedException(*msg*, *exception=None*)

Subclass of `SAXException` raised when a SAX [`XMLReader`](https://docs.python.org/3.14/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader) is asked to enable an unsupported feature, or to set a property to a value the implementation does not support. SAX applications and extensions may put this class to similar use.

See also

[SAX: The Simple API for XML](http://www.saxproject.org/)

This site is the central point for defining the SAX API. A Java implementation plus online documentation are offered there. You will also find links to implementations along with historical information.

Module [`xml.sax.handler`](https://docs.python.org/3.14/library/xml.sax.handler.html#module-xml.sax.handler)

Definitions of the interfaces for application-provided objects.

Module [`xml.sax.saxutils`](https://docs.python.org/3.14/library/xml.sax.utils.html#module-xml.sax.saxutils)

Convenience functions for use in SAX applications.

Module [`xml.sax.xmlreader`](https://docs.python.org/3.14/library/xml.sax.reader.html#module-xml.sax.xmlreader)

Definitions of the interfaces for parser-provided objects.

[Subject index](INDEX.md) · [Previous](xml-sax-support-for-sax2-parsers.md) · [Continue](saxexception-getmessage-to-saxexception-getexception.md)
