# xml.etree.ElementTree: `xml.etree.ElementTree.XML()`, `xml.etree.ElementTree.XMLID()`

Builds a textual rendering of an XML element along with every one of its subelements. *element* is an `Element` instance. *encoding* [1] selects the output encoding (the default being US-ASCII). Supply `encoding="unicode"` to produce a Unicode string; without it, a bytestring results. *method* takes one of `"xml"`, `"html"` or `"text"` (defaulting to `"xml"`). The parameters *xml_declaration*, *default_namespace* and *short_empty_elements* behave just as they do in `ElementTree.write()`. The return value is a list of (possibly) encoded strings holding the XML data. No particular ordering is promised, apart from the guarantee that `b"".join(tostringlist(element)) == tostring(element)`.

Added in version 3.2.

Changed in version 3.4: Added the *short_empty_elements* parameter.

Changed in version 3.8: Added the *xml_declaration* and *default_namespace* parameters.

Changed in version 3.8: The `tostringlist()` function keeps whatever attribute order the user established.

 xml.etree.ElementTree.XML(*text*, *parser=None*)

Reads an XML fragment from a string literal. This routine is handy for embedding "XML literals" directly within Python source. *text* is a string that carries XML data. *parser* names an optional parser instance. When none is supplied, the default `XMLParser` parser applies. The return value is an `Element` instance.

 xml.etree.ElementTree.XMLID(*text*, *parser=None*)

Reads an XML fragment from a string literal and additionally hands back a dictionary mapping element id:s to their elements. *text* is a string that carries XML data. *parser* names an optional parser instance. When none is supplied, the default `XMLParser` parser applies. The return value is a tuple holding an `Element` instance together with a dictionary.

[Subject index](INDEX.md) · [Continue](xinclude-support.md) · [Owning module, declaration or section: xml.etree.ElementTree](xml-etree-elementtree-the-elementtree-xml-api.md) · [Owning module, declaration or section: Functions](xml-canonicalization-comments-and-debug-output.md) · [Owning module, declaration or section: xml.etree.ElementTree.tostringlist](xml-string-parsing-and-serialization.md) · [Preceding source contract and version conditions](xml-string-parsing-and-serialization.md)
