# xml.etree.ElementTree - XML tree and elements

### XML tree and elements

Because XML is fundamentally a nested data format, a tree is the most fitting structure for modeling it. To that end, `ET` supplies a pair of classes - `ElementTree` stands in for the complete XML document viewed as a tree, while `Element` corresponds to one node within that tree. Operations that touch the document as a whole (loading from and saving to files) typically happen at the `ElementTree` layer. Working with an individual XML element together with its descendants takes place at the `Element` layer.

[Subject index](INDEX.md) · [Previous](tutorial.md) · [Continue](parsing-xml.md) · [Owning module, declaration or section: xml.etree.ElementTree](xml-etree-elementtree-the-elementtree-xml-api.md)
