# xml.sax.handler - ErrorHandler Objects

### ErrorHandler Objects

Objects with this interface serve to receive error and warning information from the [`XMLReader`](https://docs.python.org/3.14/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader). Should you build an object that implements this interface and then register it with your `XMLReader`, the parser will invoke the methods on your object to report all warnings and errors. Three levels of errors are available: warnings, (possibly) recoverable errors, and unrecoverable errors. Every method takes a [`SAXParseException`](https://docs.python.org/3.14/library/xml.sax.html#xml.sax.SAXParseException) as its sole parameter. Errors and warnings may be turned into an exception by raising the passed-in exception object.

 ErrorHandler.error(*exception*)

Called when the parser runs into a recoverable error. If this method raises no exception, parsing may carry on, but the application should not expect further document information. Letting the parser carry on may permit additional errors to be found in the input document.

 ErrorHandler.fatalError(*exception*)

Called when the parser runs into an error it cannot recover from; parsing is expected to stop when this method returns.

 ErrorHandler.warning(*exception*)

Called when the parser hands minor warning information to the application. Parsing is expected to carry on when this method returns, and document information will keep being passed to the application. Raising an exception within this method will bring parsing to an end.

[Subject index](INDEX.md) · [Previous](entityresolver-resolveentity.md) · [Continue](lexicalhandler-comment-to-lexicalhandler-endcdata.md) · [Owning module, declaration or section: xml.sax.handler](xml-sax-handler-contenthandler-class.md)
