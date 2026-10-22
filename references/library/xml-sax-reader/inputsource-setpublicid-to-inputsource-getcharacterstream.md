# xml.sax.xmlreader — InputSource Objects

### InputSource Objects

 InputSource.setPublicId(*id*)

Sets the public identifier of this `InputSource`.

 InputSource.getPublicId()

Returns the public identifier of this `InputSource`.

 InputSource.setSystemId(*id*)

Sets the system identifier of this `InputSource`.

 InputSource.getSystemId()

Returns the system identifier of this `InputSource`.

 InputSource.setEncoding(*encoding*)

Sets the character encoding of this `InputSource`.

The encoding has to be a string that an XML encoding declaration would accept (refer to section 4.3.3 of the XML recommendation).

The encoding attribute of the `InputSource` gets ignored when the `InputSource` also carries a character stream.

 InputSource.getEncoding()

Get the character encoding of this InputSource.

 InputSource.setByteStream(*bytefile*)

Set the byte stream (a [binary file](https://docs.python.org/3.14/glossary.html#term-binary-file)) for this input source.

The SAX parser will disregard this when a character stream is also specified, but it will favor a byte stream over opening a URI connection on its own.

Should the application already know the byte stream's character encoding, it ought to declare it through the setEncoding method.

 InputSource.getByteStream()

Get the byte stream for this input source.

For this byte stream the getEncoding method hands back the character encoding, or `None` when it is unknown.

 InputSource.setCharacterStream(*charfile*)

Set the character stream (a [text file](https://docs.python.org/3.14/glossary.html#term-text-file)) for this input source.

When a character stream is specified, the SAX parser will disregard any byte stream and will not try to open a URI connection to the system identifier.

 InputSource.getCharacterStream()

Get the character stream for this input source.

[Subject index](INDEX.md) · [Previous](locator-getcolumnnumber-to-locator-getsystemid.md) · [Continue](attributes-getlength-to-attributes-getvalue.md)
