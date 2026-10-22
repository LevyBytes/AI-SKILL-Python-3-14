# xml.etree.ElementTree: XPath selection and namespace-qualified query examples

### Example

The example below shows off a handful of the module's XPath features. Our source will be the `countrydata` XML document drawn from the Parsing XML section:

```python
import xml.etree.ElementTree as ET

root = ET.fromstring(countrydata)

# Top-level elements
root.findall(".")

# All 'neighbor' grand-children of 'country' children of the top-level
# elements
root.findall("./country/neighbor")

# Nodes with name='Singapore' that have a 'year' child
root.findall(".//year/..[@name='Singapore']")

# 'year' nodes that are children of nodes with name='Singapore'
root.findall(".//*[@name='Singapore']/year")

# All 'neighbor' nodes that are the second child of their parent
root.findall(".//neighbor[2]")

```

With namespaced XML, apply the standard qualified `{namespace}tag` form:

```python
# All dublin-core "title" tags in the document
root.findall(".//{http://purl.org/dc/elements/1.1/}title")

```

[Subject index](INDEX.md) · [Previous](xpath-support.md) · [Continue](supported-xpath-syntax.md) · [Owning module, declaration or section: xml.etree.ElementTree](xml-etree-elementtree-the-elementtree-xml-api.md)
