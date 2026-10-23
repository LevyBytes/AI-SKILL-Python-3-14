# xml.dom - Element Objects

### Element Objects

`Element` derives from `Node`, and so picks up every attribute that class has.

 Element.tagName

The name of the element type. Within a document that uses namespaces it may contain colons. The value is a string.

 Element.getElementsByTagName(*tagName*)

Identical to the matching method on the `Document` class.

 Element.getElementsByTagNameNS(*namespaceURI*, *localName*)

Identical to the matching method on the `Document` class.

 Element.hasAttribute(*name*)

Hand back `True` when the element carries an attribute that *name* identifies.

 Element.hasAttributeNS(*namespaceURI*, *localName*)

Hand back `True` when the element carries an attribute that *namespaceURI* and *localName* identify.

 Element.getAttribute(*name*)

Hand back, as a string, the value of the attribute that *name* identifies. When no such attribute is present, an empty string comes back, just as though the attribute held no value.

 Element.getAttributeNode(*attrname*)

Hand back the `Attr` node for the attribute that *attrname* identifies.

 Element.getAttributeNS(*namespaceURI*, *localName*)

Hand back, as a string, the value of the attribute that *namespaceURI* and *localName* identify. When no such attribute is present, an empty string comes back, just as though the attribute held no value.

 Element.getAttributeNodeNS(*namespaceURI*, *localName*)

Hand back an attribute value as a node, given a *namespaceURI* and *localName*.

 Element.removeAttribute(*name*)

Drop an attribute by its name. When nothing matches, a `NotFoundErr` is raised.

 Element.removeAttributeNode(*oldAttr*)

Drop *oldAttr* from the attribute list and return it, when it is present. When *oldAttr* is absent, `NotFoundErr` is raised.

 Element.removeAttributeNS(*namespaceURI*, *localName*)

Drop an attribute by its name. Note that this takes a localName, not a qname. Nothing is raised when no attribute matches.

 Element.setAttribute(*name*, *value*)

Assign an attribute value from a string.

 Element.setAttributeNode(*newAttr*)

Attach a new attribute node onto the element, displacing an existing attribute where required when the `name` attribute lines up. Where such a displacement happens, the previous attribute node comes back. When *newAttr* is already in use, `InuseAttributeErr` is raised.

 Element.setAttributeNodeNS(*newAttr*)

Attach a new attribute node onto the element, displacing an existing attribute where required when the `namespaceURI` and `localName` attributes line up. Where such a displacement happens, the previous attribute node comes back. When *newAttr* is already in use, `InuseAttributeErr` is raised.

 Element.setAttributeNS(*namespaceURI*, *qname*, *value*)

Assign an attribute value from a string, given a *namespaceURI* and a *qname*. Keep in mind that a qname is the entire attribute name. That sets it apart from the above.

[Subject index](INDEX.md) · [Previous](document-documentelement-to-document-getelementsbytagnamens.md) · [Continue](attr-name-to-attr-value.md) · [Owning module, declaration or section: xml.dom](xml-dom-the-document-object-model-api.md)
