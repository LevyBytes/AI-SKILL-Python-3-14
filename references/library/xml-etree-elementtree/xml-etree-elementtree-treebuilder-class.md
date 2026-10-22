# xml.etree.ElementTree: `xml.etree.ElementTree.TreeBuilder`

### TreeBuilder Objects

 *class *xml.etree.ElementTree.TreeBuilder(*element_factory=None*, ***, *comment_factory=None*, *pi_factory=None*, *insert_comments=False*, *insert_pis=False*)

Generic element structure builder. This builder turns a stream of start, data, end, comment and pi method calls into a well-formed element structure. You can lean on this class to assemble an element structure with a custom XML parser, or with a parser for some other XML-like format.

*element_factory*, when supplied, must be a callable accepting a pair of positional arguments — a tag together with a dict of attributes. Its job is to hand back a new element instance.

The *comment_factory* and *pi_factory* functions, when supplied, ought to act like the `Comment()` and `ProcessingInstruction()` functions in creating comments and processing instructions. When omitted, the default factories step in. When *insert_comments* and/or *insert_pis* is true, comments/pis get inserted into the tree if they show up inside the root element (though not outside it).

[Subject index](INDEX.md) · [Previous](xml-etree-elementtree-qname-class.md) · [Continue](xml-tree-builder-events-and-canonical-writer.md) · [Owning module, declaration or section: xml.etree.ElementTree](xml-etree-elementtree-the-elementtree-xml-api.md)
