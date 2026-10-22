# What's New in Python 2.5 / The ElementTree package

### The ElementTree package

Part of Fredrik Lundh's ElementTree library for handling XML is now bundled with the standard library as `xml.etree`. From ElementTree 1.2.6 the modules on offer are `ElementTree`, `ElementPath`, and `ElementInclude`. The `cElementTree` accelerator module ships as well.

What follows is a short tour of working with ElementTree. The complete ElementTree documentation lives at [https://web.archive.org/web/20201124024954/http://effbot.org/zone/element-index.htm](https://web.archive.org/web/20201124024954/http://effbot.org/zone/element-index.htm).

ElementTree models an XML document as a tree built from element nodes. A document's textual content is kept in the `text` and `tail` attributes of (Here lies one of the big distinctions between ElementTree and the Document Object Model; the DOM has many node types, `TextNode` among them.)

The parsing function you'll reach for most often is `parse()`, which accepts either a string (treated as a filename) or a file-like object and gives back an `ElementTree` instance:

```python
from xml.etree import ElementTree as ET

tree = ET.parse('ex-1.xml')

feed = urllib.urlopen(
          'http://planet.python.org/rss10.xml')
tree = ET.parse(feed)

```

With an `ElementTree` instance in hand, calling its `getroot()` method yields the root `Element` node.

There is additionally an `XML()` function which accepts a string literal and produces an `Element` node (rather than an `ElementTree`). It offers a neat means of folding in XML fragments, coming close to the ease of an XML literal:

```python
svg = ET.XML("""<svg width="10px" version="1.0">
             </svg>""")
svg.set('height', '320px')
svg.append(elem1)

```

Every XML element exposes a mix of dictionary-like and list-like access methods. The dictionary-like operations reach attribute values, whereas the list-like operations reach child nodes.

| Operation | Result |
| --- | --- |
| `elem[n]` | Returns n'th child element. |
| `elem[m:n]` | Returns list of m'th through n'th child elements. |
| `len(elem)` | Returns number of child elements. |
| `list(elem)` | Returns list of child elements. |
| `elem.append(elem2)` | Adds *elem2* as a child. |
| `elem.insert(index, elem2)` | Inserts *elem2* at the specified location. |
| `del elem[n]` | Deletes n'th child element. |
| `elem.keys()` | Returns list of attribute names. |
| `elem.get(name)` | Returns value of attribute *name*. |
| `elem.set(name, value)` | Sets new value for attribute *name*. |
| `elem.attrib` | Retrieves the dictionary containing attributes. |
| `del elem.attrib[name]` | Deletes attribute *name*. |

`Element` nodes likewise stand in for comments and processing instructions. To test whether a given node is a comment or a processing instruction:

```python
if elem.tag is ET.Comment:
    ...
elif elem.tag is ET.ProcessingInstruction:
    ...

```

Producing XML output is a matter of calling the `ElementTree.write()` method. As with `parse()`, it accepts either a string or a file-like object:

```python
# Encoding is US-ASCII
tree.write('output.xml')

# Encoding is UTF-8
f = open('output.xml', 'w')
tree.write(f, encoding='utf-8')

```

(Caution: ASCII is the default output encoding. In typical XML work, where an element's name might hold any Unicode character, ASCII makes a poor encoding because it throws an exception once an element's name carries any character above value 127. For that reason you're better off naming a different encoding such as UTF-8, which copes with any Unicode character.)

This is merely a partial account of the ElementTree interfaces. For the full picture, consult the package's official documentation.

See also

[https://web.archive.org/web/20201124024954/http://effbot.org/zone/element-index.htm](https://web.archive.org/web/20201124024954/http://effbot.org/zone/element-index.htm)

Official documentation for ElementTree.

[Subject index](INDEX.md) · [Previous source section](the-ctypes-package.md) · [Next source section](the-hashlib-package.md) · [Release/subject declaration](pep-308-conditional-expressions.md)
