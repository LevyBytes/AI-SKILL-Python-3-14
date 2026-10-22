# xml.dom — DOMImplementation Objects

### DOMImplementation Objects

By way of the `DOMImplementation` interface, an application can check whether the DOM it is working with supports specific features. With DOM Level 2 came the further capability of building fresh `Document` and `DocumentType` objects through the `DOMImplementation`.

 DOMImplementation.hasFeature(*feature*, *version*)

Hand back `True` when the feature named by the string pair *feature* and *version* is implemented.

 DOMImplementation.createDocument(*namespaceUri*, *qualifiedName*, *doctype*)

Hand back a fresh `Document` object (the DOM's root), carrying a child `Element` object that has the supplied *namespaceUri* and *qualifiedName*. For *doctype*, pass a `DocumentType` object that `createDocumentType()` produced, or `None`. Within the Python DOM API, you may also pass `None` for the first two arguments to signal that no child `Element` should be created.

 DOMImplementation.createDocumentType(*qualifiedName*, *publicId*, *systemId*)

Hand back a fresh `DocumentType` object wrapping the supplied *qualifiedName*, *publicId*, and *systemId* strings, which carry the data held in an XML document type declaration.

[Subject index](INDEX.md) · [Previous](objects-in-the-dom.md) · [Continue](node-nodetype-to-node-removechild.md) · [Owning module, declaration or section: xml.dom](xml-dom-the-document-object-model-api.md)
