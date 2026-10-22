# xml.dom: DOM exception categories and document constraints

### Exceptions

Just one exception, `DOMException`, is laid out by the DOM Level 2 recommendation, alongside several constants that let an application work out which category of error took place. Each `DOMException` instance comes with a [`code`](https://docs.python.org/3.14/library/code.html#module-code) attribute holding the value that matches the particular exception.

Those constants are made available by the Python DOM interface, which goes further and broadens the exception set so that every exception code the DOM lays down has its own dedicated exception. An implementation is required to raise whichever specific exception fits, and each one supplies the matching value in its [`code`](https://docs.python.org/3.14/library/code.html#module-code) attribute.

`*exception *xml.dom.DOMException`

The parent exception class from which every specific DOM exception derives. You cannot create an instance of this class on its own.

`*exception *xml.dom.DomstringSizeErr`

Thrown if a given stretch of text won't fit within a string. No Python DOM implementation is known to use it, though you might encounter it coming from DOM implementations built in languages other than Python.

`*exception *xml.dom.HierarchyRequestErr`

Thrown if you try to place a node somewhere its node type is not permitted.

`*exception *xml.dom.IndexSizeErr`

Thrown when an index or size argument handed to a method is below zero or runs past the permitted range.

`*exception *xml.dom.InuseAttributeErr`

Thrown if you try to add an `Attr` node that already sits somewhere else within the document.

`*exception *xml.dom.InvalidAccessErr`

Thrown when the object beneath does not back the parameter or operation in question.

`*exception *xml.dom.InvalidCharacterErr`

You get this exception whenever a string argument holds a character that the XML 1.0 recommendation forbids in the setting where it appears. As an illustration, trying to build an `Element` node whose element type name includes a space will trigger the error.

`*exception *xml.dom.InvalidModificationErr`

Thrown if you try to alter a node's type.

`*exception *xml.dom.InvalidStateErr`

Thrown if you reach for an object that has not been defined or can no longer be used.

`*exception *xml.dom.NamespaceErr`

Should you try to modify any object in a manner the [Namespaces in XML](https://www.w3.org/TR/REC-xml-names/) recommendation disallows, this exception comes up.

`*exception *xml.dom.NotFoundErr`

The exception for when a node is absent from the context being referenced. To illustrate, `NamedNodeMap.removeNamedItem()` raises it whenever the node you supply isn't found in the map.

`*exception *xml.dom.NotSupportedErr`

Thrown if the implementation offers no support for the kind of object or operation you asked for.

`*exception *xml.dom.NoDataAllowedErr`

This comes up if you give data to a node that has no support for holding any.

`*exception *xml.dom.NoModificationAllowedErr`

Thrown whenever you try to change an object that forbids changes (read-only nodes being one such case).

`*exception *xml.dom.SyntaxErr`

Thrown if the string you provide is invalid or not permitted.

[Subject index](INDEX.md) · [Continue](xml-dom-wrongdocumenterr.md) · [Owning module, declaration or section: xml.dom](xml-dom-the-document-object-model-api.md)
