# xml.dom - Objects in the DOM

### Objects in the DOM

The authoritative reference for the DOM remains the W3C's DOM specification.

Be aware that DOM attributes can be handled as nodes as well, not only as plain strings. Needing to do that is quite uncommon, though, so this technique is not documented here yet.

| Interface | Section | Purpose |
| --- | --- | --- |
| `DOMImplementation` | DOMImplementation Objects | Interface to the underlying implementation. |
| `Node` | Node Objects | Base interface for most objects in a document. |
| `NodeList` | NodeList Objects | Interface for a sequence of nodes. |
| `DocumentType` | DocumentType Objects | Information about the declarations needed to process a document. |
| `Document` | Document Objects | Object which represents an entire document. |
| `Element` | Element Objects | Element nodes in the document hierarchy. |
| `Attr` | Attr Objects | Attribute value nodes on element nodes. |
| `Comment` | Comment Objects | Representation of comments in the source document. |
| `Text` | Text and CDATASection Objects | Nodes containing textual content from the document. |
| `ProcessingInstruction` | ProcessingInstruction Objects | Processing instruction representation. |

One more section covers the exceptions that the DOM defines for use in Python.

[Subject index](INDEX.md) · [Previous](xml-dom-registerdomimplementation-to-xml-dom-xhtml-namespace.md) · [Continue](dom-feature-support-and-document-creation.md) · [Owning module, declaration or section: xml.dom](xml-dom-the-document-object-model-api.md)
