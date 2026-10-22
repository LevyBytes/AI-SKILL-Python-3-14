# xml.etree.ElementTree.XMLParser: `close()`, `feed()`, `flush()`

close()

Finishes feeding data to the parser. It returns the result of calling the *target*'s `close()` method (the *target* handed in at construction); by default this is the toplevel document element.

 feed(*data*)

Feeds data to the parser. *data* is encoded data.

 flush()

Forces parsing of any data already fed but not yet parsed, which is useful for ensuring more immediate feedback, especially with Expat >=2.6.0. Internally, `flush()` briefly turns off reparse deferral in Expat (where it is currently on) and forces a reparse. Turning off reparse deferral carries security implications; consult [`xml.parsers.expat.xmlparser.SetReparseDeferralEnabled()`](https://docs.python.org/3.14/library/pyexpat.html#xml.parsers.expat.xmlparser.SetReparseDeferralEnabled) for the details.

Note that `flush()` has been backported to a number of earlier CPython releases as a security fix. Test for the presence of `flush()` with [`hasattr()`](https://docs.python.org/3.14/library/functions.html#hasattr) when your code runs across an assortment of Python versions.

Added in version 3.13.

`XMLParser.feed()` invokes the *target*'s `start(tag, attrs_dict)` method for every opening tag, its `end(tag)` method for every closing tag, and routes data through the `data(data)` method. For the rest of the supported callback methods, see the `TreeBuilder` class. `XMLParser.close()` invokes the *target*'s `close()` method. `XMLParser` is good for more than just assembling a tree structure. The following counts the maximum depth of an XML file:

```python
>>> from xml.etree.ElementTree import XMLParser
>>> class MaxDepth:                     # The target object of the parser
...     maxDepth = 0
...     depth = 0
...     def start(self, tag, attrib):   # Called for each opening tag.
...         self.depth += 1
...         if self.depth > self.maxDepth:
...             self.maxDepth = self.depth
...     def end(self, tag):             # Called for each closing tag.
...         self.depth -= 1
...     def data(self, data):
...         pass            # We do not need to do anything with data.
...     def close(self):    # Called when all data has been parsed.
...         return self.maxDepth
...
>>> target = MaxDepth()
>>> parser = XMLParser(target=target)
>>> exampleXml = """
... <a>
...   <b>
...   </b>
...   <b>
...     <c>
...       <d>
...       </d>
...     </c>
...   </b>
... </a>"""
>>> parser.feed(exampleXml)
>>> parser.close()
4

```

[Subject index](INDEX.md) · [Previous](xml-etree-elementtree-xmlparser-class.md) · [Continue](xml-etree-elementtree-xmlpullparser-class.md) · [Owning module, declaration or section: xml.etree.ElementTree](xml-etree-elementtree-the-elementtree-xml-api.md) · [Owning module, declaration or section: xml.etree.ElementTree.XMLParser](xml-etree-elementtree-xmlparser-class.md) · [Owning module, declaration or section: XMLParser Objects](xml-etree-elementtree-xmlparser-class.md)
