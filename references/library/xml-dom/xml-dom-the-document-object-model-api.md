# xml.dom — `xml.dom` — The Document Object Model API

### `xml.dom` — The Document Object Model API

**Source code:** [Lib/xml/dom/__init__.py](https://github.com/python/cpython/tree/3.14/Lib/xml/dom/__init__.py)

---

The Document Object Model — commonly abbreviated “DOM” — is a language-neutral API from the World Wide Web Consortium (W3C) used to read and edit XML documents. An implementation of the DOM exposes an XML document in the form of a tree, or lets calling code assemble one of those trees from nothing. Access to that tree is then offered via a collection of objects exposing recognized interfaces.

For random-access scenarios the DOM proves enormously handy. With SAX you only ever see a single fragment of the document at any given moment. While positioned on one SAX element, the others are out of reach. While positioned on a text node, you cannot reach the element that contains it. Building a SAX application means you yourself must track where your program currently sits inside the document, somewhere within your own code. That bookkeeping is your responsibility, not SAX's. And whenever you must peek further ahead in the XML, there is simply no way to do so.

Certain tasks just cannot be done in an event-driven approach that lacks a tree to walk. Granted, you might assemble some kind of tree of your own as the SAX events fire, yet the DOM spares you from having to write all that. As a representation, the DOM is the standard tree form for XML data.

The W3C develops the Document Object Model incrementally, through what they call “levels.” Python's rendering of the API draws heavily on the DOM Level 2 recommendation.

A DOM application usually begins by parsing XML to produce a DOM. DOM Level 1 says nothing whatsoever about how that happens, and Level 2 only improves matters a little: a `DOMImplementation` object class exists that exposes `Document` creation methods, yet there is no implementation-neutral way to reach an XML reader/parser/Document builder. Nor is there any well-defined route to those methods short of already holding a `Document` object. Within Python, every DOM implementation supplies a `getDOMImplementation()` function. A Load/Store specification arrives with DOM Level 3, describing an interface to the reader, though the Python standard library does not yet ship it.

After obtaining a DOM document object, the pieces of your XML document become reachable through that object's attributes and methods. The DOM specification lays out those properties; this section of the manual covers how Python interprets that specification.

The W3C's specification lays out the DOM API for Java, ECMAScript, and OMG IDL. The Python binding given here rests largely on the IDL flavor of the specification, although strict conformance is not demanded (implementations may, if they wish, also support the strict IDL mapping). Refer to the Conformance section for a thorough treatment of the mapping rules.

See also

[Document Object Model (DOM) Level 2 Specification](https://www.w3.org/TR/2000/REC-DOM-Level-2-Core-20001113/)

The W3C recommendation that underpins the Python DOM API.

[Document Object Model (DOM) Level 1 Specification](https://www.w3.org/TR/REC-DOM-Level-1/)

The W3C recommendation defining the DOM that [`xml.dom.minidom`](https://docs.python.org/3.14/library/xml.dom.minidom.html#module-xml.dom.minidom) supports.

[Python Language Mapping Specification](https://www.omg.org/spec/PYTH/1.2/PDF)

This defines how OMG IDL maps onto Python.

[Subject index](INDEX.md) · [Continue](xml-dom-registerdomimplementation-to-xml-dom-xhtml-namespace.md)
