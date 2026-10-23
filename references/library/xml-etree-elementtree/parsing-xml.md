# xml.etree.ElementTree - Parsing XML

### Parsing XML

For the data in this section, we'll rely on the made-up `country_data.xml` XML document as our example:

```xml
<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>

```

To bring this data in, we can read it out of a file:

```python
import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()

```

Alternatively, straight from a string:

```python
root = ET.fromstring(country_data_as_string)

```

When given a string, `fromstring()` parses the XML directly into an `Element` that serves as the root of the resulting tree. Be aware that some of the other parsing routines hand back an `ElementTree` instead, so consult the documentation when in doubt.

Being an `Element`, `root` carries both a tag and a dictionary of attributes:

```python
>>> root.tag
'data'
>>> root.attrib
{}

```

Additionally, it holds child nodes that we are able to loop through:

```python
>>> for child in root:
...     print(child.tag, child.attrib)
...
country {'name': 'Liechtenstein'}
country {'name': 'Singapore'}
country {'name': 'Panama'}

```

Since children sit inside one another, we may reach particular child nodes through their index:

```python
>>> root[0][1].text
'2008'

```

Note

Parsing the XML input does not necessarily turn every piece of it into an element of the resulting tree. At present, this module disregards any XML comments, processing instructions, and document type declarations that appear in the input. That said, trees assembled through this module's API instead of by parsing XML text are allowed to hold comments and processing instructions, which do appear when XML output is produced. To reach a document type declaration, hand a custom `TreeBuilder` instance to the `XMLParser` constructor.

[Subject index](INDEX.md) · [Previous](xml-tree-and-elements.md) · [Continue](pull-api-for-non-blocking-parsing.md) · [Owning module, declaration or section: xml.etree.ElementTree](xml-etree-elementtree-the-elementtree-xml-api.md)
