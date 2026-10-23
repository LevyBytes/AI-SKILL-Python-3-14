# xml.sax.xmlreader - XMLReader Objects

### XMLReader Objects

The `XMLReader` interface backs the following methods:

 XMLReader.parse(*source*)

Process an input source, generating SAX events. As the *source* object you may supply a system identifier (a string that names the input source — usually a file name or else a URL), a [`pathlib.Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) or [path-like](https://docs.python.org/3.14/glossary.html#term-path-like-object) object, or even an `InputSource` object. Once `parse()` returns, the input is fully processed, and the parser object can be discarded or reset.

Changed in version 3.5: Added support of character streams.

Changed in version 3.8: Added support of path-like objects.

 XMLReader.getContentHandler()

Return the current [`ContentHandler`](https://docs.python.org/3.14/library/xml.sax.handler.html#xml.sax.handler.ContentHandler).

 XMLReader.setContentHandler(*handler*)

Set the current [`ContentHandler`](https://docs.python.org/3.14/library/xml.sax.handler.html#xml.sax.handler.ContentHandler). When no `ContentHandler` is set, content events will be thrown away.

 XMLReader.getDTDHandler()

Return the current [`DTDHandler`](https://docs.python.org/3.14/library/xml.sax.handler.html#xml.sax.handler.DTDHandler).

 XMLReader.setDTDHandler(*handler*)

Set the current [`DTDHandler`](https://docs.python.org/3.14/library/xml.sax.handler.html#xml.sax.handler.DTDHandler). When no `DTDHandler` is set, DTD events will be thrown away.

 XMLReader.getEntityResolver()

Return the current [`EntityResolver`](https://docs.python.org/3.14/library/xml.sax.handler.html#xml.sax.handler.EntityResolver).

 XMLReader.setEntityResolver(*handler*)

Set the current [`EntityResolver`](https://docs.python.org/3.14/library/xml.sax.handler.html#xml.sax.handler.EntityResolver). When no `EntityResolver` is set, attempts to resolve an external entity will end up opening the system identifier for the entity, and fail when it is unavailable.

 XMLReader.getErrorHandler()

Return the current [`ErrorHandler`](https://docs.python.org/3.14/library/xml.sax.handler.html#xml.sax.handler.ErrorHandler).

 XMLReader.setErrorHandler(*handler*)

Set the current error handler. With no [`ErrorHandler`](https://docs.python.org/3.14/library/xml.sax.handler.html#xml.sax.handler.ErrorHandler) in place, errors get raised as exceptions while warnings get printed.

 XMLReader.setLocale(*locale*)

Allow an application to set the locale for errors and warnings.

SAX parsers need not provide localization for errors and warnings; if, however, the requested locale lies beyond what they can support, a SAX exception must be raised. An application is free to ask for a locale change midway through a parse.

 XMLReader.getFeature(*featurename*)

Return the current setting for feature *featurename*. Should the feature go unrecognized, `SAXNotRecognizedException` is raised. The well-known featurenames appear in the module [`xml.sax.handler`](https://docs.python.org/3.14/library/xml.sax.handler.html#module-xml.sax.handler).

 XMLReader.setFeature(*featurename*, *value*)

Set the *featurename* to *value*. Should the feature go unrecognized, `SAXNotRecognizedException` is raised. Should the parser not support the feature or its setting, *SAXNotSupportedException* is raised.

 XMLReader.getProperty(*propertyname*)

Return the current setting for property *propertyname*. Should the property go unrecognized, a `SAXNotRecognizedException` is raised. The well-known propertynames appear in the module [`xml.sax.handler`](https://docs.python.org/3.14/library/xml.sax.handler.html#module-xml.sax.handler).

 XMLReader.setProperty(*propertyname*, *value*)

Set the *propertyname* to *value*. Should the property go unrecognized, `SAXNotRecognizedException` is raised. Should the parser not support the property or its setting, *SAXNotSupportedException* is raised.

[Subject index](INDEX.md) · [Previous](xml-sax-xmlreader-attributesnsimpl-class.md) · [Continue](incrementalparser-feed-to-incrementalparser-reset.md)
