# xml.dom.minidom — `xml.dom.minidom` — Minimal DOM implementation

### `xml.dom.minidom` — Minimal DOM implementation

**Source code:** [Lib/xml/dom/minidom.py](https://github.com/python/cpython/tree/3.14/Lib/xml/dom/minidom.py)

---

As a pared-down take on the Document Object Model interface, `xml.dom.minidom` carries an API much like the ones found in other languages. The aim is to keep it both plainer and a good deal more compact than the full DOM. Anyone not yet at home with the DOM would do well to turn to the [`xml.etree.ElementTree`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#module-xml.etree.ElementTree) module for their XML work instead.

Note

Should you have to parse data that is untrusted or unauthenticated, consult [XML security](https://docs.python.org/3.14/library/xml.html#xml-security).

As a rule, DOM applications kick off by parsing a piece of XML into a DOM. Under `xml.dom.minidom`, the parse functions are how that gets done:

```python
from xml.dom.minidom import parse, parseString

dom1 = parse('c:\\temp\\mydata.xml')  # parse an XML file by name

datasource = open('c:\\temp\\mydata.xml')
dom2 = parse(datasource)  # parse an open file

dom3 = parseString('<myxml>Some data<empty/> some more data</myxml>')

```

You may hand the `parse()` function either a filename or an already-open file object.

 xml.dom.minidom.parse(*filename_or_file*, *parser=None*, *bufsize=None*)

Hand back a `Document` built from the input supplied. The *filename_or_file* can be a file name or else a file-like object. Where you pass *parser*, it has to be a SAX2 parser object. The function swaps in its own document handler on that parser and switches namespace support on; any other parser setup, such as wiring up an entity resolver, needs to have been taken care of beforehand.

When your XML already sits in a string, the `parseString()` function serves instead:

 xml.dom.minidom.parseString(*string*, *parser=None*)

Hand back a `Document` that stands for the *string*. Internally the method wraps the string in an [`io.StringIO`](https://docs.python.org/3.14/library/io.html#io.StringIO) object and forwards that along to `parse()`.

Either way, both functions give you a `Document` object that captures the document's contents.

At bottom, what `parse()` and `parseString()` accomplish is to hook an XML parser up to a “DOM builder” - one that takes parse events from any SAX parser and turns them into a DOM tree. The function names may mislead a little, yet they become clear once you get acquainted with the interfaces. By the time these functions return, the document has already been fully parsed; the catch is merely that they don't bundle a parser implementation of their own.

Another route to a `Document` is to invoke a method on a “DOM Implementation” object. That object comes from calling the `getDOMImplementation()` function, found either in the [`xml.dom`](https://docs.python.org/3.14/library/xml.dom.html#module-xml.dom) package or in the `xml.dom.minidom` module. With a `Document` in hand, you fill out the DOM by attaching child nodes to it:

```python
from xml.dom.minidom import getDOMImplementation

impl = getDOMImplementation()

newdoc = impl.createDocument(None, "some_tag", None)
top_element = newdoc.documentElement
text = newdoc.createTextNode('Some textual content.')
top_element.appendChild(text)

```

Holding a DOM document object, you reach the pieces of your XML document by way of its properties and methods, all of which the DOM specification lays out. The document object's central property is `documentElement`, which yields the XML document's top element - the one enclosing every other. A sample program follows:

```python
dom3 = parseString("<myxml>Some data</myxml>")
assert dom3.documentElement.tagName == "myxml"

```

Once you've wrapped up with a DOM tree, you have the option of calling the `unlink()` method to nudge the no-longer-wanted objects toward early cleanup. As an `xml.dom.minidom`-specific add-on to the DOM API, `unlink()` leaves the node together with everything beneath it effectively unusable. Skip it, and Python's garbage collector will in time deal with the tree's objects on its own.

See also

[Document Object Model (DOM) Level 1 Specification](https://www.w3.org/TR/REC-DOM-Level-1/)

The W3C's recommendation covering the DOM that `xml.dom.minidom` implements.

[Subject index](INDEX.md) · [Previous](minimal-dom-implementation.md) · [Continue](node-unlink-to-node-toprettyxml.md)
