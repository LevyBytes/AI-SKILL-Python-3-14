# xml.dom — Module Contents

### Module Contents

These functions live in `xml.dom`:

 xml.dom.registerDOMImplementation(*name*, *factory*)

Associate the *factory* callable with the name *name*. That factory should yield an object satisfying the `DOMImplementation` interface. Depending on what suits the particular implementation, the factory may hand back the very same object on every invocation, or a fresh one each time (for example, when that implementation allows some customization).

 xml.dom.getDOMImplementation(*name=None*, *features=()*)

Hand back an appropriate DOM implementation. The *name* is either a well-known name, the module name of a DOM implementation, or `None`. When it is something other than `None`, the matching module is imported and, if that import works, a `DOMImplementation` object is returned. When no name is supplied and the environment variable `PYTHON_DOM` happens to be set, that variable points to the implementation to use.

When no name is supplied, the implementations on hand are surveyed to locate one offering the requested feature set. Should none turn up, an [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) is raised. Each entry in the features list has to be a `(feature, version)` pair, and these get handed to the `hasFeature()` method on the `DOMImplementation` objects that are available.

A handful of convenience constants come along too:

 xml.dom.EMPTY_NAMESPACE

The marker signaling that a DOM node carries no namespace. You commonly see it as a node's `namespaceURI`, or supply it as the *namespaceURI* argument to a namespaces-aware method.

 xml.dom.XML_NAMESPACE

The namespace URI tied to the reserved prefix `xml`, per [Namespaces in XML](https://www.w3.org/TR/REC-xml-names/) (section 4).

 xml.dom.XMLNS_NAMESPACE

The namespace URI used for namespace declarations, per [Document Object Model (DOM) Level 2 Core Specification](https://www.w3.org/TR/DOM-Level-2-Core/core.html) (section 1.1.8).

 xml.dom.XHTML_NAMESPACE

The XHTML namespace URI as set out by [XHTML 1.0: The Extensible HyperText Markup Language](https://www.w3.org/TR/xhtml1/) (section 3.1.1).

Beyond those, `xml.dom` ships a base `Node` class together with the DOM exception classes. None of the methods or attributes laid out by the DOM specification are actually implemented by the `Node` class this module supplies; that work falls to concrete DOM implementations. What this module's `Node` class does supply are the constants that feed the `nodeType` attribute on concrete `Node` objects; per the DOM specifications, those constants sit on the class itself rather than at module scope.

[Subject index](INDEX.md) · [Previous](xml-dom-the-document-object-model-api.md) · [Continue](objects-in-the-dom.md) · [Owning module, declaration or section: xml.dom](xml-dom-the-document-object-model-api.md)
