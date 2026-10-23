# xml.etree.ElementTree - QName Objects

### QName Objects

 *class *xml.etree.ElementTree.QName(*text_or_uri*, *tag=None*)

QName wrapper. You can use this to wrap a QName attribute value so that namespaces are handled correctly on output. *text_or_uri* is a string holding the QName value, in the {uri}local form, or, when the tag argument is supplied, the URI portion of a QName. When *tag* is supplied, the first argument is read as a URI and this argument is read as a local name. `QName` instances are opaque.

[Subject index](INDEX.md) · [Previous](xml-tree-root-parsing-and-writing.md) · [Continue](xml-etree-elementtree-treebuilder-class.md) · [Owning module, declaration or section: xml.etree.ElementTree](xml-etree-elementtree-the-elementtree-xml-api.md)
