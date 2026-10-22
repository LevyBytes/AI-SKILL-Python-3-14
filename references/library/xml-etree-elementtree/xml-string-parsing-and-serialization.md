# xml.etree.ElementTree: XML parsing, element construction and serialization

xml.etree.ElementTree.fromstring(*text*, *parser=None*)

Parses an XML section out of a string constant. Behaves the same as `XML()`. *text* is a string holding XML data. *parser* is an optional parser instance. When none is supplied, the standard `XMLParser` parser applies. Hands back an `Element` instance.

 xml.etree.ElementTree.fromstringlist(*sequence*, *parser=None*)

Parses an XML document out of a sequence of string fragments. *sequence* is a list or another sequence holding XML data fragments. *parser* is an optional parser instance. When none is supplied, the standard `XMLParser` parser applies. Hands back an `Element` instance.

Added in version 3.2.

 xml.etree.ElementTree.indent(*tree*, *space=' '*, *level=0*)

Appends whitespace to the subtree so the tree appears visually indented. You can use this to produce pretty-printed XML output. *tree* may be an Element or ElementTree. *space* is the whitespace string placed in for each indentation level, defaulting to two space characters. To indent partial subtrees that sit within an already indented tree, supply the starting indentation level as *level*.

Added in version 3.9.

 xml.etree.ElementTree.iselement(*element*)

Tests whether an object looks like a valid element object. *element* is an element instance. Returns `True` when this is an element object.

 xml.etree.ElementTree.iterparse(*source*, *events=None*, *parser=None*)

Parses an XML section into an element tree step by step, keeping the user informed of progress as it goes. *source* is a filename or [file object](https://docs.python.org/3.14/glossary.html#term-file-object) holding XML data. *events* is a sequence of events to relay back. The events that are supported are the strings `"start"`, `"end"`, `"comment"`, `"pi"`, `"start-ns"` and `"end-ns"` (the "ns" events serve to obtain detailed namespace information). When *events* is left out, only `"end"` events are relayed. *parser* is an optional parser instance. When none is supplied, the standard `XMLParser` parser applies. *parser* must derive from `XMLParser` and may use only the default `TreeBuilder` as a target. Hands back an [iterator](https://docs.python.org/3.14/glossary.html#term-iterator) yielding `(event, elem)` pairs; it carries a `root` attribute pointing at the root element of the resulting XML tree after *source* has been read in full. The iterator provides the `close()` method that shuts the internal file object when *source* is a filename.

Bear in mind that even though `iterparse()` assembles the tree step by step, it performs blocking reads against *source* (or the file it identifies). Consequently, it is a poor fit for applications in which blocking reads are impossible. When parsing must be entirely non-blocking, turn to `XMLPullParser`.

Note

`iterparse()` only promises that it has encountered the ">" character of a starting tag at the moment it emits a "start" event, so although the attributes are defined, the contents of the text and tail attributes remain undefined at that stage. This holds equally for the element children, which may or may not be there yet.

When you require a fully populated element, watch for "end" events instead.

Deprecated since version 3.4: The *parser* argument.

Changed in version 3.8: The `comment` and `pi` events were added.

Changed in version 3.13: Added the `close()` method.

 xml.etree.ElementTree.parse(*source*, *parser=None*)

Parses an XML section into an element tree. The *source* argument is a filename or file object holding XML data. *parser* is an optional parser instance. When none is supplied, the standard `XMLParser` parser applies. Hands back an `ElementTree` instance.

 xml.etree.ElementTree.ProcessingInstruction(*target*, *text=None*)

PI element factory. This factory function builds a special element that gets serialized as an XML processing instruction. *target* is a string holding the PI target. *text* is a string holding the PI contents, when supplied. Hands back an element instance representing a processing instruction.

Be aware that `XMLParser` passes over processing instructions in the input rather than building PI objects from them. An `ElementTree` ends up with processing instruction nodes only when they have been added into the tree by means of one of the `Element` methods.

 xml.etree.ElementTree.register_namespace(*prefix*, *uri*)

Registers a namespace prefix. The registry is global, and whatever existing mapping there may be for either the supplied prefix or the namespace URI gets dropped. Here *prefix* denotes a namespace prefix, while *uri* denotes a namespace uri. Tags plus attributes belonging to this namespace will be serialized using the supplied prefix wherever that is feasible.

Added in version 3.2.

 xml.etree.ElementTree.SubElement(*parent*, *tag*, *attrib={}*, ***extra*)

Subelement factory. This function builds an element instance and attaches it to an element that already exists.

The element name, the attribute names, and the attribute values may each take the form of either bytestrings or Unicode strings. Here *parent* denotes the parent element, *tag* denotes the subelement name, and *attrib* denotes an optional dictionary holding element attributes. *extra* holds additional attributes provided as keyword arguments. Hands back an element instance.

 xml.etree.ElementTree.tostring(*element*, *encoding='us-ascii'*, *method='xml'*, ***, *xml_declaration=None*, *default_namespace=None*, *short_empty_elements=True*)

Produces a string rendering of an XML element together with all of its subelements. *element* is an `Element` instance. *encoding* [1] is the output encoding (the default being US-ASCII). Pass `encoding="unicode"` to produce a Unicode string (a bytestring is produced otherwise). *method* is one of `"xml"`, `"html"` or `"text"` (the default being `"xml"`). *xml_declaration*, *default_namespace* and *short_empty_elements* carry the same meaning they do in `ElementTree.write()`. Hands back an (optionally) encoded string holding the XML data.

Changed in version 3.4: Added the *short_empty_elements* parameter.

Changed in version 3.8: Added the *xml_declaration* and *default_namespace* parameters.

Changed in version 3.8: The `tostring()` function now keeps attributes in the order the user laid them out.

 xml.etree.ElementTree.tostringlist(*element*, *encoding='us-ascii'*, *method='xml'*, ***, *xml_declaration=None*, *default_namespace=None*, *short_empty_elements=True*)

[Subject index](INDEX.md) · [Previous](xml-canonicalization-comments-and-debug-output.md) · [Owning module, declaration or section: xml.etree.ElementTree](xml-etree-elementtree-the-elementtree-xml-api.md) · [Owning module, declaration or section: Functions](xml-canonicalization-comments-and-debug-output.md) · [Required continuation of the source contract](xml-etree-elementtree-xml-to-xml-etree-elementtree-xmlid.md)
