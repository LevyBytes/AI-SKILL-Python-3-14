# xml.etree.ElementTree: XInclude XML and text inclusion examples

### Example

What follows shows the XInclude module in action. To pull an XML document into the present document, employ the `{http://www.w3.org/2001/XInclude}include` element with its **parse** attribute set to `"xml"`, and name the document to pull in via the **href** attribute.

```xml
<?xml version="1.0"?>
<document xmlns:xi="http://www.w3.org/2001/XInclude">
  <xi:include href="source.xml" parse="xml" />
</document>

```

The **href** attribute is, by default, interpreted as a file name. Custom loaders let you change that behaviour. Be aware too that the bundled helper offers no XPointer syntax.

Handling this file means loading it in the usual way and handing its root element to the `xml.etree.ElementTree` module:

```python
from xml.etree import ElementTree, ElementInclude

tree = ElementTree.parse("document.xml")
root = tree.getroot()

ElementInclude.include(root)

```

The ElementInclude module swaps out the `{http://www.w3.org/2001/XInclude}include` element for the root element drawn from the **source.xml** document. What you end up with may resemble:

```xml
<document xmlns:xi="http://www.w3.org/2001/XInclude">
  <para>This is a paragraph.</para>
</document>

```

When the **parse** attribute is left out, its value falls back to "xml". The href attribute must be present.

To bring in a text document, apply the `{http://www.w3.org/2001/XInclude}include` element with its **parse** attribute set to "text":

```xml
<?xml version="1.0"?>
<document xmlns:xi="http://www.w3.org/2001/XInclude">
  Copyright (c) <xi:include href="year.txt" parse="text" />.
</document>

```

What comes out may resemble:

```xml
<document xmlns:xi="http://www.w3.org/2001/XInclude">
  Copyright (c) 2003.
</document>

```

[Subject index](INDEX.md) · [Previous](xinclude-support.md) · [Continue](xml-element-inclusion-and-loader.md) · [Owning module, declaration or section: xml.etree.ElementTree](xml-etree-elementtree-the-elementtree-xml-api.md)
