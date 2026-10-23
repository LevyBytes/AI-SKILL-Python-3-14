# xml.sax.xmlreader - IncrementalParser Objects

### IncrementalParser Objects

Instances of `IncrementalParser` offer the following additional methods:

 IncrementalParser.feed(*data*)

Process a chunk of *data*.

 IncrementalParser.close()

Assume the end of the document. That will verify well-formedness conditions checkable only at the end, fire handlers, and may release resources allocated while parsing.

 IncrementalParser.reset()

This method gets called after close has been called so as to reset the parser, making it ready to parse new documents. Calling parse or feed after close without first calling reset has undefined results.

[Subject index](INDEX.md) · [Previous](xmlreader-parse-to-xmlreader-setproperty.md) · [Continue](locator-getcolumnnumber-to-locator-getsystemid.md)
