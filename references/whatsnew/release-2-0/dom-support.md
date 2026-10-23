# What’s New in Python 2.0 / DOM Support - xml.dom.minidom

### DOM Support

The Document Object Model is a tree-shaped representation of an XML document. A top-level `Document` instance forms the root of the tree and holds one child, the top-level `Element` instance. That `Element` carries child nodes standing for character data and any sub-elements, which can in turn hold further children of their own, and so on. With the DOM you can walk the resulting tree however you wish, read element and attribute values, add and remove nodes, and turn the tree back into XML.

The DOM comes in handy for editing XML documents, since you can build a DOM tree, change it by inserting new nodes or shuffling subtrees, and then emit a fresh XML document as the result. You can equally assemble a DOM tree by hand and convert it to XML, which can be a more flexible route to XML output than just writing `<tag1>`…`</tag1>` straight to a file.

Python’s bundled DOM implementation resides in the [`xml.dom.minidom`](https://docs.python.org/3.14/library/xml.dom.minidom.html#module-xml.dom.minidom) module. It’s a lightweight take on the Level 1 DOM that supports XML namespaces. The `parse()` and `parseString()` convenience functions are supplied for producing a DOM tree:

```python
from xml.dom import minidom
doc = minidom.parse('hamlet.xml')

```

Here `doc` holds a `Document` instance. Together with every other DOM class — `Element` and `Text` among them — `Document` derives from the `Node` base class. As a result, each node within a DOM tree shares a handful of common methods, `toxml()` being one, which yields a string holding the XML form of that node along with everything beneath it. On top of that, every class carries its own dedicated methods; `Element` and `Document` instances, for instance, expose one that gathers all child elements matching a particular tag name. Picking up where the earlier 2-line example left off:

```python
perslist = doc.getElementsByTagName( 'PERSONA' )
print perslist[0].toxml()
print perslist[1].toxml()

```

Run against the *Hamlet* XML file, those handful of lines print:

```python
<PERSONA>CLAUDIUS, king of Denmark. </PERSONA>
<PERSONA>HAMLET, son to the late, and nephew to the present king.</PERSONA>

```

You reach the document's root element through `doc.documentElement`, and reshaping its children is straightforward — you delete, append, or pull out nodes:

```python
root = doc.documentElement

# Remove the first child
root.removeChild( root.childNodes[0] )

# Move the new first child to the end
root.appendChild( root.childNodes[0] )

# Insert the new first child (originally,
# the third child) before the 20th child.
root.insertBefore( root.childNodes[0], root.childNodes[20] )

```

As before, the Python documentation is the place to look for an exhaustive rundown of the assorted `Node` classes and the methods each one offers.

[Subject index](INDEX.md) · [Previous source section](sax2-support.md) · [Release/subject declaration](introduction.md) · [Next source section](relationship-to-pyxml.md)
