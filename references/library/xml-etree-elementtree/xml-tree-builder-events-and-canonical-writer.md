# xml.etree.ElementTree.TreeBuilder: `close()`, `data()`, `end()`, `start()`, `comment()`, `pi()`, `doctype()`, `start_ns()`, `end_ns()`, `xml.etree.ElementTree.C14NWriterTarget`

close()

Flushes the builder buffers and gives back the toplevel document element. The return value is an `Element` instance.

 data(*data*)

Adds text to the current element. *data* is a string. It should be either a bytestring or a Unicode string.

 end(*tag*)

Closes the current element. *tag* is the element name. The return value is the closed element.

 start(*tag*, *attrs*)

Opens a new element. The element name comes from *tag*. A dictionary of element attributes comes from *attrs*. The return value is the opened element.

 comment(*text*)

Creates a comment carrying the given *text*. When `insert_comments` is true, this also adds it to the tree.

Added in version 3.8.

 pi(*target*, *text*)

Creates a process instruction carrying the given *target* name and *text*. When `insert_pis` is true, this also adds it to the tree.

Added in version 3.8.

On top of that, a custom `TreeBuilder` object may supply the following methods:

 doctype(*name*, *pubid*, *system*)

Handles a doctype declaration. The doctype name comes from *name*. The public identifier comes from *pubid*. The system identifier comes from *system*. This method does not appear on the default `TreeBuilder` class.

Added in version 3.2.

 start_ns(*prefix*, *uri*)

Fires every time the parser runs into a new namespace declaration, ahead of the `start()` callback for the opening element that introduces it. *prefix* is `''` for the default namespace and otherwise the declared namespace prefix name. *uri* is the namespace URI.

Added in version 3.8.

 end_ns(*prefix*)

Fires after the `end()` callback of an element that declared a namespace prefix mapping, carrying the name of the *prefix* that has left scope.

Added in version 3.8.

 *class *`xml.etree.ElementTree.C14NWriterTarget(write, *, with_comments=False, strip_text=False, rewrite_prefixes=False, qname_aware_tags=None, qname_aware_attrs=None, exclude_attrs=None, exclude_tags=None)`

A [C14N 2.0](https://www.w3.org/TR/xml-c14n2/) writer. Its arguments match those of the `canonicalize()` function. Rather than building a tree, this class turns the callback events straight into a serialised form by way of the *write* function.

Added in version 3.8.

[Subject index](INDEX.md) · [Previous](xml-etree-elementtree-treebuilder-class.md) · [Continue](xml-etree-elementtree-xmlparser-class.md) · [Owning module, declaration or section: xml.etree.ElementTree](xml-etree-elementtree-the-elementtree-xml-api.md) · [Owning module, declaration or section: xml.etree.ElementTree.TreeBuilder](xml-etree-elementtree-treebuilder-class.md) · [Owning module, declaration or section: TreeBuilder Objects](xml-etree-elementtree-treebuilder-class.md)
