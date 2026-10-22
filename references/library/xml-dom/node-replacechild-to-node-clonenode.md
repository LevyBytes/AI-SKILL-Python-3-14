# xml.dom: `Node.replaceChild()`, `Node.normalize()`, `Node.cloneNode()`

Node.replaceChild(*newChild*, *oldChild*)

Swap an existing node for a new one. *oldChild* has to be a child of this node; otherwise [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised.

 Node.normalize()

Merge neighboring text nodes so every continuous run of text lives in a single `Text` instance. For many applications this makes handling text drawn from a DOM tree easier.

 Node.cloneNode(*deep*)

Copy this node. Passing *deep* says to copy all of its child nodes too. The copy is handed back.

[Subject index](INDEX.md) · [Previous](node-nodetype-to-node-removechild.md) · [Continue](nodelist-item-to-nodelist-length.md) · [Owning module, declaration or section: xml.dom](xml-dom-the-document-object-model-api.md) · [Owning module, declaration or section: Node Objects](node-nodetype-to-node-removechild.md)
