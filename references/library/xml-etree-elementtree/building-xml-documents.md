# xml.etree.ElementTree - Building XML documents

### Building XML documents

For making fresh sub-elements under a given element, the `SubElement()` function offers another handy route:

```python
>>> a = ET.Element('a')
>>> b = ET.SubElement(a, 'b')
>>> c = ET.SubElement(a, 'c')
>>> d = ET.SubElement(c, 'd')
>>> ET.dump(a)
<a><b /><c><d /></c></a>

```

[Subject index](INDEX.md) · [Previous](modifying-an-xml-file.md) · [Continue](parsing-xml-with-namespaces.md) · [Owning module, declaration or section: xml.etree.ElementTree](xml-etree-elementtree-the-elementtree-xml-api.md)
