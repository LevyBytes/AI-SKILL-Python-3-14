# xml.dom.pulldom: Pull-DOM parsing model and partial tree construction

## xml.dom.pulldom - Support for building partial DOM trees

### `xml.dom.pulldom` - Support for building partial DOM trees

**Source code:** [Lib/xml/dom/pulldom.py](https://github.com/python/cpython/tree/3.14/Lib/xml/dom/pulldom.py)

---

The `xml.dom.pulldom` module hands you a “pull parser” that, when needed, can also be asked to turn out DOM-accessible fragments of the document. At its heart the idea is to draw “events” out of a stream of incoming XML and act on them. SAX likewise rides an event-driven processing model paired with callbacks, but here it falls to the pull-parser user to pull events from the stream on purpose, looping across them until the work is done or some error condition crops up.

Note

When the data you must parse is untrusted or unauthenticated, look to [XML security](https://docs.python.org/3.14/library/xml.html#xml-security).

Changed in version 3.7.1: By default the SAX parser has stopped handling general external entities, a change made to harden security out of the box. Should you want external entities processed, hand in a custom parser instance:

```python
from xml.dom.pulldom import parse
from xml.sax import make_parser
from xml.sax.handler import feature_external_ges

parser = make_parser()
parser.setFeature(feature_external_ges, True)
parse(filename, parser=parser)

```

Example:

```python
from xml.dom import pulldom

doc = pulldom.parse('sales_items.xml')
for event, node in doc:
    if event == pulldom.START_ELEMENT and node.tagName == 'item':
        if int(node.getAttribute('price')) > 50:
            doc.expandNode(node)
            print(node.toxml())

```

`event` holds a constant, drawn from this set:

- `START_ELEMENT`

- `END_ELEMENT`

- `COMMENT`

- `START_DOCUMENT`

- `END_DOCUMENT`

- `CHARACTERS`

- `PROCESSING_INSTRUCTION`

- `IGNORABLE_WHITESPACE`

`node` is an object whose type is `xml.dom.minidom.Document`, `xml.dom.minidom.Element` or `xml.dom.minidom.Text`.

Because the document arrives as a “flat” run of events, its “tree” gets walked implicitly, and the elements you're after surface no matter how deep they sit. Put another way, you can set aside hierarchical concerns like recursively combing through the document nodes - though where the surrounding context of elements does matter, you'd have to either hold onto some context-related state (that is, track where you stand in the document at any moment) or call on the `DOMEventStream.expandNode()` method and shift into DOM-style processing.

[Subject index](INDEX.md) · [Continue](xml-dom-pulldom-pulldom-class.md)
