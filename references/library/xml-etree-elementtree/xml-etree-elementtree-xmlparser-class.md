# xml.etree.ElementTree: `xml.etree.ElementTree.XMLParser`

### XMLParser Objects

 *class *xml.etree.ElementTree.XMLParser(***, *target=None*, *encoding=None*)

This class forms the module's low-level building block. It draws on [`xml.parsers.expat`](https://docs.python.org/3.14/library/pyexpat.html#module-xml.parsers.expat) for efficient, event-based XML parsing. You can feed it XML data piece by piece through the `feed()` method, and parsing events get mapped to a push API by firing callbacks on the *target* object. When *target* is left out, the default `TreeBuilder` steps in. When *encoding* [1] is supplied, that value takes precedence over the encoding named in the XML file.

Changed in version 3.8: The parameters became [keyword-only](https://docs.python.org/3.14/glossary.html#keyword-only-parameter). Support for the *html* argument was dropped.

[Subject index](INDEX.md) · [Previous](xml-tree-builder-events-and-canonical-writer.md) · [Continue](xml-parser-feed-close-and-flush.md) · [Owning module, declaration or section: xml.etree.ElementTree](xml-etree-elementtree-the-elementtree-xml-api.md)
