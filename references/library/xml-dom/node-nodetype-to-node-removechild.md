# xml.dom: DOM node identity, relationships and child mutation

### Node Objects

Every constituent of an XML document is a subclass of `Node`.

 Node.nodeType

An integer denoting the type of the node. The `Node` object holds symbolic constants for these types: `ELEMENT_NODE`, `ATTRIBUTE_NODE`, `TEXT_NODE`, `CDATA_SECTION_NODE`, `ENTITY_NODE`, `PROCESSING_INSTRUCTION_NODE`, `COMMENT_NODE`, `DOCUMENT_NODE`, `DOCUMENT_TYPE_NODE`, `NOTATION_NODE`. This is a read-only attribute.

 Node.parentNode

This node's parent, or `None` when it is the document node. It is always either a `Node` object or `None`. With `Element` nodes the value is the enclosing element, save for the root element, where it is instead the `Document` object. With `Attr` nodes it is invariably `None`. This is a read-only attribute.

 Node.attributes

A `NamedNodeMap` holding attribute objects. Real values appear here only for elements; everything else yields `None` for this attribute. This is a read-only attribute.

 Node.previousSibling

The node sharing this node's parent that comes right before it. Take, for example, the element whose end-tag sits just ahead of the *self* element's start-tag. Since XML documents contain far more than just elements, that prior sibling might equally be text, a comment, or some other thing. When this node is its parent's first child, the attribute holds `None`. This is a read-only attribute.

 Node.nextSibling

The node sharing this node's parent that comes right after it. Compare `previousSibling`. When this node is its parent's last child, the attribute holds `None`. This is a read-only attribute.

 Node.childNodes

A list holding the nodes nested inside this node. This is a read-only attribute.

 Node.firstChild

This node's first child when it has any, otherwise `None`. This is a read-only attribute.

 Node.lastChild

This node's last child when it has any, otherwise `None`. This is a read-only attribute.

 Node.localName

Whatever follows the colon in the `tagName`, if a colon is present, or otherwise the whole `tagName`. The value is a string.

 Node.prefix

Whatever comes before the colon in the `tagName`, if a colon is present, or otherwise the empty string. The value is a string, or `None`.

 Node.namespaceURI

The namespace bound to the element's name. It will be either a string or `None`. This is a read-only attribute.

 Node.nodeName

What this means varies with the type of node; consult the DOM specification for specifics. The same information is always reachable through some other property, such as `tagName` for elements or `name` for attributes. Whatever the node type, this attribute holds either a string or `None`. This is a read-only attribute.

 Node.nodeValue

What this means varies with the type of node; consult the DOM specification for specifics. It parallels the case of `nodeName`. The value is a string or `None`.

 Node.hasAttributes()

Hand back `True` when the node carries any attributes.

 Node.hasChildNodes()

Hand back `True` when the node carries any child nodes.

 Node.isSameNode(*other*)

Hand back `True` when *other* points at the very same node as this one. This comes in handy especially for DOM implementations built on some kind of proxy scheme (where several objects might point at one node).

Note

The basis for this is a proposed DOM Level 3 API that remains at the “working draft” phase, yet this specific interface seems uncontentious. W3C revisions will not inevitably alter this method within the Python DOM interface (though if the W3C ships a new API for it, that too would be supported).

 Node.appendChild(*newChild*)

Attach a fresh child node onto the tail of this node's child list, handing back *newChild*. Should that node already sit in the tree, it gets detached beforehand.

 Node.insertBefore(*newChild*, *refChild*)

Place a fresh child node ahead of a child that already exists. *refChild* has to be a child of this node; otherwise [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised. *newChild* comes back. When *refChild* is `None`, *newChild* lands at the tail of the children's list.

 Node.removeChild(*oldChild*)

Detach a child node. *oldChild* has to be a child of this node; otherwise [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised. On success *oldChild* comes back. When *oldChild* sees no further use, call its `unlink()` method.

[Subject index](INDEX.md) · [Previous](dom-feature-support-and-document-creation.md) · [Continue](node-replacechild-to-node-clonenode.md) · [Owning module, declaration or section: xml.dom](xml-dom-the-document-object-model-api.md)
