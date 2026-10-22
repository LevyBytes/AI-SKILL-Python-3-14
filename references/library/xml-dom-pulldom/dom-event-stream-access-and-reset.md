# xml.dom.pulldom.DOMEventStream: `getEvent()`, `expandNode()`, `reset()`

getEvent()

Give back a tuple holding *event* together with the current *node* - as `xml.dom.minidom.Document` when event is `START_DOCUMENT`, as `xml.dom.minidom.Element` when event is `START_ELEMENT` or `END_ELEMENT`, or as `xml.dom.minidom.Text` when event is `CHARACTERS`. That current node carries nothing about its children until you call `expandNode()`.

 expandNode(*node*)

Pull every child of *node* in under *node* itself. For example:

```python
from xml.dom import pulldom

xml = '<html><title>Foo</title> <p>Some text <div>and more</div></p> </html>'
doc = pulldom.parseString(xml)
for event, node in doc:
    if event == pulldom.START_ELEMENT and node.tagName == 'p':
        # Following statement only prints '<p/>'
        print(node.toxml())
        doc.expandNode(node)
        # Following statement prints node with all its children '<p>Some text <div>and more</div></p>'
        print(node.toxml())

```

 reset()

[Subject index](INDEX.md) · [Previous](xml-dom-pulldom-domeventstream-class.md) · [Owning module, declaration or section: xml.dom.pulldom](xml-dom-pulldom-support-for-building-partial-dom-trees.md) · [Owning module, declaration or section: xml.dom.pulldom.DOMEventStream](xml-dom-pulldom-domeventstream-class.md) · [Owning module, declaration or section: DOMEventStream Objects](xml-dom-pulldom-domeventstream-class.md)
