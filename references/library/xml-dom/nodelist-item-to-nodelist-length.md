# xml.dom - NodeList Objects

### NodeList Objects

A `NodeList` stands for a sequence of nodes. The DOM Core recommendation puts these objects to two uses: an `Element` object exposes one as its roster of child nodes, and the `getElementsByTagName()` and `getElementsByTagNameNS()` methods on `Node` hand back objects bearing this interface to convey query results.

For these objects the DOM Level 2 recommendation specifies a single method plus a single attribute:

 NodeList.item(*i*)

Hand back the *i*'th entry of the sequence when there is one, or otherwise `None`. The index *i* may not drop below zero, nor may it reach or exceed the sequence's length.

 NodeList.length

How many nodes the sequence holds.

On top of that, the Python DOM interface calls for extra support enabling `NodeList` objects to behave as Python sequences. Every `NodeList` implementation has to back [`__len__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__len__) and [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__); doing so permits walking the `NodeList` inside [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for) statements and lets the [`len()`](https://docs.python.org/3.14/library/functions.html#len) built-in work correctly.

When a DOM implementation permits altering the document, its `NodeList` implementation must additionally back the [`__setitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__setitem__) and [`__delitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__delitem__) methods.

[Subject index](INDEX.md) · [Previous](node-replacechild-to-node-clonenode.md) · [Continue](documenttype-publicid-to-documenttype-notations.md) · [Owning module, declaration or section: xml.dom](xml-dom-the-document-object-model-api.md)
