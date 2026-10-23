# xml.dom - Text and CDATASection Objects

### Text and CDATASection Objects

The `Text` interface stands for text within the XML document. When the parser and DOM implementation back the DOM's XML extension, stretches of text wrapped inside CDATA marked sections live in `CDATASection` objects. The two interfaces match exactly, save for the differing `nodeType` value each one reports.

These interfaces build on the `Node` interface. Holding child nodes is not allowed for them.

 Text.data

The text node's content as a string.

Note

That a node is a `CDATASection` does not imply the node stands for one whole CDATA marked section, merely that the node's content came from inside a CDATA section. Within the document tree, a lone CDATA section may end up spread across more than one node. Whether two neighboring `CDATASection` nodes belong to separate CDATA marked sections cannot be told.

[Subject index](INDEX.md) · [Previous](comment-data.md) · [Continue](processinginstruction-target-to-processinginstruction-data.md) · [Owning module, declaration or section: xml.dom](xml-dom-the-document-object-model-api.md)
