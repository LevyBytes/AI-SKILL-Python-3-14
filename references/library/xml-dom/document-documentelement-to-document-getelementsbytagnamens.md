# xml.dom — Document Objects

### Document Objects

A `Document` stands for a whole XML document — its elements, attributes, processing instructions, comments, and so on. Bear in mind that it inherits properties from `Node`.

 Document.documentElement

The single root element of the document, of which there is only one.

 Document.createElement(*tagName*)

Build and return a new element node. Creating the element does not place it into the document. Inserting it is something you do yourself, using another method like `insertBefore()` or `appendChild()`.

 Document.createElementNS(*namespaceURI*, *tagName*)

Build and return a new element carrying a namespace. The *tagName* is allowed to carry a prefix. Creating the element does not place it into the document. Inserting it is something you do yourself, using another method like `insertBefore()` or `appendChild()`.

 Document.createTextNode(*data*)

Build and return a text node holding the data given as an argument. Like the other creation methods, this one leaves the node out of the tree.

 Document.createComment(*data*)

Build and return a comment node holding the data given as an argument. Like the other creation methods, this one leaves the node out of the tree.

 Document.createProcessingInstruction(*target*, *data*)

Build and return a processing instruction node holding the *target* and *data* given as arguments. Like the other creation methods, this one leaves the node out of the tree.

 Document.createAttribute(*name*)

Build and return an attribute node. No particular element gets tied to the attribute node by this method. To put the freshly built attribute instance to use, call `setAttributeNode()` on the right `Element` object.

 Document.createAttributeNS(*namespaceURI*, *qualifiedName*)

Build and return an attribute node carrying a namespace. The *tagName* is allowed to carry a prefix. No particular element gets tied to the attribute node by this method. To put the freshly built attribute instance to use, call `setAttributeNode()` on the right `Element` object.

 Document.getElementsByTagName(*tagName*)

Look through every descendant (immediate children, their children, and so on) bearing a given element type name.

 Document.getElementsByTagNameNS(*namespaceURI*, *localName*)

Look through every descendant (immediate children, their children, and so on) bearing a given namespace URI and localname. The localname is whatever portion of the namespace trails the prefix.

[Subject index](INDEX.md) · [Previous](documenttype-publicid-to-documenttype-notations.md) · [Continue](element-tagname-to-element-setattributens.md) · [Owning module, declaration or section: xml.dom](xml-dom-the-document-object-model-api.md)
