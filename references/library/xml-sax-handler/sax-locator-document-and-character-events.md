# xml.sax.handler: SAX document, namespace, element and character callbacks

### ContentHandler Objects

To serve their application, users are expected to subclass `ContentHandler`. On the relevant events in the input document the parser calls the following methods:

 ContentHandler.setDocumentLocator(*locator*)

Invoked by the parser to hand the application a locator for pinpointing the origin of document events.

SAX parsers are strongly urged (though not strictly required) to provide a locator: if one is provided, it must be passed to the application by calling this method ahead of any of the other methods on the DocumentHandler interface.

By means of the locator the application can determine the end position of any document-related event, even when the parser reports no error. The application will commonly draw on this information to report its own errors (for instance character content that violates an application's business rules). What the locator returns is probably not adequate for use with a search engine.

Bear in mind that the locator returns accurate information only while the events on this interface are being invoked. At any other moment the application should not try to use it.

 ContentHandler.startDocument()

Receive notification of the beginning of a document.

The SAX parser will call this method only once, ahead of any other methods on this interface or on DTDHandler (apart from `setDocumentLocator()`).

 ContentHandler.endDocument()

Receive notification of the end of a document.

The SAX parser will call this method only once, and it will be the final method called during the parse. The parser shall not call this method until it has either given up parsing (because of an unrecoverable error) or arrived at the end of input.

 ContentHandler.startPrefixMapping(*prefix*, *uri*)

Begin the scope of a prefix-URI Namespace mapping.

Normal Namespace processing does not require the information from this event: when the `feature_namespaces` feature is on (the default), the SAX XML reader will automatically substitute prefixes for element and attribute names.

In some situations, though, applications must use prefixes within character data or attribute values, where automatic expansion is not safe; the `startPrefixMapping()` and `endPrefixMapping()` events hand the application the information it needs to expand prefixes in those contexts on its own, where necessary.

Bear in mind that `startPrefixMapping()` and `endPrefixMapping()` events are not guaranteed to be properly nested with respect to one another: every `startPrefixMapping()` event will happen before the corresponding `startElement()` event, and every `endPrefixMapping()` event will happen after the corresponding `endElement()` event, yet their order is not guaranteed.

 ContentHandler.endPrefixMapping(*prefix*)

End the scope of a prefix-URI mapping.

Consult `startPrefixMapping()` for details. Although this event always follows the corresponding `endElement()` event, no further guarantee covers the ordering among `endPrefixMapping()` events.

 ContentHandler.startElement(*name*, *attrs*)

Signals the start of an element in non-namespace mode.

As a string, the *name* parameter holds the element type's raw XML 1.0 name, while the *attrs* parameter carries an object of the [Attributes](https://docs.python.org/3.14/library/xml.sax.reader.html#attributes-objects) interface holding the element's attributes. The parser is free to re-use whatever object arrives as *attrs*; clinging to a reference is no dependable means of retaining a copy of the attributes. To retain such a copy, apply the [`copy()`](https://docs.python.org/3.14/library/copy.html#module-copy) method on the *attrs* object.

 ContentHandler.endElement(*name*)

Signals the end of an element in non-namespace mode.

The *name* parameter holds the name of the element type, exactly as with the `startElement()` event.

 ContentHandler.startElementNS(*name*, *qname*, *attrs*)

Signals the start of an element in namespace mode.

As a `(uri, localname)` tuple, the *name* parameter holds the name of the element type; the *qname* parameter holds whichever raw XML 1.0 name appeared in the source document, and the *attrs* parameter carries an instance of the [AttributesNS](https://docs.python.org/3.14/library/xml.sax.reader.html#attributes-ns-objects) interface holding the element's attributes. When no namespace is bound to the element, the *uri* component of *name* will be `None`. The parser is free to re-use whatever object arrives as *attrs*; clinging to a reference is no dependable means of retaining a copy of the attributes. To retain such a copy, apply the [`copy()`](https://docs.python.org/3.14/library/copy.html#module-copy) method on the *attrs* object.

Parsers may set the *qname* parameter to `None`, unless the `feature_namespace_prefixes` feature is activated.

 ContentHandler.endElementNS(*name*, *qname*)

Signals the end of an element in namespace mode.

The *name* parameter holds the name of the element type, exactly as with the `startElementNS()` method, and likewise the *qname* parameter.

 ContentHandler.characters(*content*)

Receive notification of character data.

To report each chunk of character data, the Parser invokes this method. A SAX parser may deliver all contiguous character data within one chunk, or it may divide it across several chunks; even so, every character within any single event must originate from the same external entity so that the Locator yields useful information.

*content* may be a string or bytes instance; the `expat` reader module always emits strings.

Note

For this method, the older SAX 1 interface that the Python XML Special Interest Group supplied relied on a more Java-like interface. Since few of the parsers used from Python took advantage of the older interface, the simpler signature was picked to supersede it. When porting old code onto the new interface, supply *content* rather than slicing content via the old *offset* and *length* parameters.

[Subject index](INDEX.md) · [Previous](sax-feature-and-property-constants.md) · [Continue](sax-whitespace-instructions-and-skipped-entities.md) · [Owning module, declaration or section: xml.sax.handler](xml-sax-handler-contenthandler-class.md)
