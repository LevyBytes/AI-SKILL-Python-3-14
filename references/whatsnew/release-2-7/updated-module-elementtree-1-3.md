# What’s New in Python 2.7 / Updated module: ElementTree 1.3 - xml.etree.elementtree

### Updated module: ElementTree 1.3

The ElementTree library bundled with Python was bumped up to version 1.3. A selection of the new features follows:

- Each of the parsing functions now accepts a *parser* keyword argument supplying an [`XMLParser`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser) instance for it to use. This lets you override the file’s internal encoding:

```python
p = ET.XMLParser(encoding='utf-8')
t = ET.XML("""<root/>""", parser=p)

```

Parsing errors in XML now raise a [`ParseError`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.ParseError) exception, and its instances carry a `position` attribute holding a (*line*, *column*) tuple that pinpoints where the trouble occurred.

- The ElementTree code that turns trees into a string has been heavily overhauled, making it about twice as quick in many situations. The [`ElementTree.write()`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree.write) and `Element.write()` methods now accept a *method* parameter set to “xml” (the default), “html”, or “text”. In HTML mode empty elements come out as `<empty></empty>` rather than `<empty/>`, while text mode passes over elements and emits only the text chunks. Should you set an element’s [`tag`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.tag) attribute to `None` while keeping its children, that element gets left out when the tree is serialized, sparing you the need for more involved rearrangement just to drop one element.

Handling of namespaces has likewise been refined. Every `xmlns:<whatever>` declaration is now emitted on the root element rather than spread across the resulting XML. You may set the default namespace for a tree through the `default_namespace` attribute and register fresh prefixes by means of [`register_namespace()`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.register_namespace). When in XML mode, the true/false *xml_declaration* parameter lets you suppress the XML declaration.

- New [`Element`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element) method: [`extend()`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.extend) tacks the items of a sequence onto the element’s children. Because elements themselves act like sequences, shifting children from one element over to another is simple:

```python
from xml.etree import ElementTree as ET

t = ET.XML("""<list>
  <item>1</item> <item>2</item>  <item>3</item>
</list>""")
new = ET.XML('<root/>')
new.extend(t)

# Outputs <root><item>1</item>...</root>
print ET.tostring(new)

```

- New [`Element`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element) method: [`iter()`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.iter) produces the element’s children as a generator. You can equally write `for child in elem:` to iterate over an element’s children. The older `getiterator()` method is now deprecated, along with `getchildren()`, which builds and returns a list of children.

- New [`Element`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element) method: [`itertext()`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.itertext) produces every chunk of text descending from the element. To illustrate:

```python
t = ET.XML("""<list>
  <item>1</item> <item>2</item>  <item>3</item>
</list>""")

# Outputs ['\n  ', '1', ' ', '2', '  ', '3', '\n']
print list(t.itertext())

```

- Deprecated: treating an element as a Boolean (that is, `if elem:`) used to come back true when the element had any children and false when it had none. This behaviour is confusing – `None` is false, yet so is a childless element? – so it will now raise a [`FutureWarning`](https://docs.python.org/3.14/library/exceptions.html#FutureWarning). In your own code, be explicit: write `len(elem) != 0` when you care about the count of children, or `elem is not None`.

Fredrik Lundh maintains ElementTree and built the 1.3 release; his write-up of 1.3 is available to read at [https://web.archive.org/web/20200703234532/http://effbot.org/zone/elementtree-13-intro.htm](https://web.archive.org/web/20200703234532/http://effbot.org/zone/elementtree-13-intro.htm). Florent Xicluna refreshed the version shipped with Python following discussions on python-dev and in [bpo-6472](https://bugs.python.org/issue?@action=redirect&bpo=6472).)

[Subject index](INDEX.md) · [Previous source section](updated-module-unittest.md) · [Next source section](build-and-c-api-changes.md) · [Release/subject declaration](the-future-for-python-2-x.md)
