# xml.etree.ElementTree - Finding interesting elements

### Finding interesting elements

`Element` offers a few handy methods for walking recursively through the entire sub-tree underneath it (its children, those children's children, and onward). Take `Element.iter()` as an instance:

```python
>>> for neighbor in root.iter('neighbor'):
...     print(neighbor.attrib)
...
{'name': 'Austria', 'direction': 'E'}
{'name': 'Switzerland', 'direction': 'W'}
{'name': 'Malaysia', 'direction': 'N'}
{'name': 'Costa Rica', 'direction': 'W'}
{'name': 'Colombia', 'direction': 'E'}

```

`Element.findall()` returns only those elements bearing a given tag that are direct children of the current element. `Element.find()` returns the *first* child carrying a specific tag, while `Element.text` reaches the element's text content. `Element.get()` reaches the element's attributes:

```python
>>> for country in root.findall('country'):
...     rank = country.find('rank').text
...     name = country.get('name')
...     print(name, rank)
...
Liechtenstein 1
Singapore 4
Panama 68

```

You can express more elaborate rules about which elements to target by turning to XPath.

[Subject index](INDEX.md) · [Previous](pull-api-for-non-blocking-parsing.md) · [Continue](modifying-an-xml-file.md) · [Owning module, declaration or section: xml.etree.ElementTree](xml-etree-elementtree-the-elementtree-xml-api.md)
