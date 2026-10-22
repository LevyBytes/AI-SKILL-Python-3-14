# xml.etree.ElementTree.ElementTree: `_setroot()`, `find()`, `findall()`, `findtext()`, `getroot()`, `iter()`, `iterfind()`, `parse()`, `write()`

_setroot(*element*)

Swaps out the root element for this tree. This throws away whatever the tree currently holds and puts the given element in its place. Use with care. *element* is an element instance.

 find(*match*, *namespaces=None*)

Same as `Element.find()`, starting at the root of the tree.

 findall(*match*, *namespaces=None*)

Same as `Element.findall()`, starting at the root of the tree.

 findtext(*match*, *default=None*, *namespaces=None*)

Same as `Element.findtext()`, starting at the root of the tree.

 getroot()

Hands back the root element for this tree.

 iter(*tag=None*)

Builds and hands back a tree iterator for the root element. The iterator runs over every element in this tree, in section order. *tag* is the tag to hunt for (with the default being to return every element).

 iterfind(*match*, *namespaces=None*)

Same as `Element.iterfind()`, starting at the root of the tree.

Added in version 3.2.

 parse(*source*, *parser=None*)

Loads an outside XML section into the present element tree. For *source*, give a file name or a [file object](https://docs.python.org/3.14/glossary.html#term-file-object). An optional parser instance may be given as *parser*. When none is supplied, the default `XMLParser` parser applies. The return value is the section's root element.

 write(*file*, *encoding='us-ascii'*, *xml_declaration=None*, *default_namespace=None*, *method='xml'*, ***, *short_empty_elements=True*)

Serialises the element tree out as XML into a file. For *file*, give a file name, or a [file object](https://docs.python.org/3.14/glossary.html#term-file-object) that is open for writing. *encoding* [1] names the output encoding (the default being US-ASCII). *xml_declaration* governs whether an XML declaration gets added to the file. Pass `False` for never, `True` for always, `None` for only when the encoding is not US-ASCII or UTF-8 or Unicode (the default is `None`). *default_namespace* sets the default XML namespace (for "xmlns"). *method* takes one of `"xml"`, `"html"` or `"text"` (defaulting to `"xml"`). The keyword-only *short_empty_elements* parameter governs how elements with no content are formatted. When `True` (the default), each is written as a single self-closed tag; otherwise each becomes a pair of start/end tags.

The output comes back as either a string ([`str`](https://docs.python.org/3.14/library/stdtypes.html#str)) or binary ([`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes)), depending on the *encoding* argument. When *encoding* is `"unicode"`, the output is a string; otherwise it is binary. Watch out that this can clash with the type of *file* when it is an open [file object](https://docs.python.org/3.14/glossary.html#term-file-object); take care not to write a string to a binary stream, nor the reverse.

Changed in version 3.4: Added the *short_empty_elements* parameter.

Changed in version 3.8: The `write()` method keeps whatever attribute order the user established.

Here is the XML file that will be worked on:

```python
<html>
    <head>
        <title>Example page</title>
    </head>
    <body>
        <p>Moved to <a href="http://example.org/">example.org</a>
        or <a href="http://example.com/">example.com</a>.</p>
    </body>
</html>

```

An example that swaps the "target" attribute on every link in the first paragraph:

```python
>>> from xml.etree.ElementTree import ElementTree
>>> tree = ElementTree()
>>> tree.parse("index.xhtml")
<Element 'html' at 0xb77e6fac>
>>> p = tree.find("body/p")     # Finds first occurrence of tag p in body
>>> p
<Element 'p' at 0xb77ec26c>
>>> links = list(p.iter("a"))   # Returns list of all links
>>> links
[<Element 'a' at 0xb77ec2ac>, <Element 'a' at 0xb77ec1cc>]
>>> for i in links:             # Iterates through all found links
...     i.attrib["target"] = "blank"
...
>>> tree.write("output.xhtml")

```

[Subject index](INDEX.md) · [Previous](xml-etree-elementtree-elementtree-class.md) · [Continue](xml-etree-elementtree-qname-class.md) · [Owning module, declaration or section: xml.etree.ElementTree](xml-etree-elementtree-the-elementtree-xml-api.md) · [Owning module, declaration or section: xml.etree.ElementTree.ElementTree](xml-etree-elementtree-elementtree-class.md) · [Owning module, declaration or section: ElementTree Objects](xml-etree-elementtree-elementtree-class.md)
