# xml.parsers.expat`xml.parsers.expat` - Fast XML parsing using Expat

### `xml.parsers.expat` - Fast XML parsing using Expat

---

Note

If you need to parse untrusted or unauthenticated data, see [XML security](https://docs.python.org/3.14/library/xml.html#xml-security).

The `xml.parsers.expat` module is a Python interface onto the Expat non-validating XML parser. It exposes a single extension type, `xmlparser`, standing for the present state of an XML parser. Once an `xmlparser` object exists, you can assign handler functions to various attributes of the object. When an XML document is later handed to the parser, the handler functions get called for the character data and markup within the XML document.

Access to the Expat parser is provided by this module through the `pyexpat` module. Using the `pyexpat` module directly is deprecated.

This module provides one exception and one type object:

 *exception *xml.parsers.expat.ExpatError

Raised whenever Expat signals an error. The ExpatError Exceptions section has further detail on how to interpret Expat errors.

 *exception *xml.parsers.expat.error

Alias for `ExpatError`.

 xml.parsers.expat.XMLParserType

The type of the return values from the `ParserCreate()` function.

The `xml.parsers.expat` module contains two functions:

 xml.parsers.expat.ErrorString(*errno*)

Returns an explanatory string for a given error number *errno*.

 xml.parsers.expat.ParserCreate(*encoding=None*, *namespace_separator=None*)

Builds and returns a fresh `xmlparser` object. *encoding*, when given, has to be a string naming the encoding the XML data uses. Expat handles fewer encodings than Python does, and its set of encodings cannot be widened; it covers UTF-8, UTF-16, ISO-8859-1 (Latin1), and ASCII. When *encoding* [1] is supplied, it overrides the document's implicit or explicit encoding.

Parsers built via `ParserCreate()` are termed "root" parsers, in the sense that no parent parser is attached to them. Non-root parsers come from `parser.ExternalEntityParserCreate`.

Expat can optionally carry out XML namespace processing on your behalf, switched on by supplying a value for *namespace_separator*. That value has to be a one-character string; a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised when the string's length is illegal (`None` counts the same as leaving it out). With namespace processing turned on, element type names and attribute names that belong to a namespace get expanded. The element name handed to the element handlers `StartElementHandler` and `EndElementHandler` becomes the namespace URI joined to the namespace separator character joined to the local part of the name. When the namespace separator is a zero byte (`chr(0)`), the namespace URI and the local part are joined with no separator at all.

As an illustration, suppose *namespace_separator* is set to a space character (`' '`) and the document below is parsed:

```xml
<?xml version="1.0"?>
<root xmlns    = "http://default-namespace.org/"
      xmlns:py = "http://www.python.org/ns/">
  <py:elem1 />
  <elem2 xmlns="" />
</root>

```

`StartElementHandler` will receive the following strings for each element:

```python
http://default-namespace.org/ root
http://www.python.org/ns/ elem1
elem2

```

Because of constraints in the `Expat` library that `pyexpat` relies on, the `xmlparser` instance returned is usable for parsing only one XML document. Call `ParserCreate` per document to obtain a separate parser instance for each.

See also

[The Expat XML Parser](http://www.libexpat.org/)

Home page of the Expat project.

[Subject index](INDEX.md) · [Continue](expat-parsing-and-entity-protection-threshold.md)
