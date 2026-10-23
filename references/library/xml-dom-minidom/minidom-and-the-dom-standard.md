# xml.dom.minidom - minidom and the DOM standard

### minidom and the DOM standard

At its core the `xml.dom.minidom` module amounts to a DOM 1.0-compatible DOM that also picks up a handful of DOM 2 features (chiefly the namespace ones).

Working with the DOM interface in Python is uncomplicated. These mapping rules hold:

- You reach interfaces by way of instance objects. Rather than instantiate the classes on their own, applications ought to rely on the creator functions that the `Document` object offers. A derived interface carries every operation (and attribute) of its base interfaces and adds whatever new operations it brings.

- Operations come across as methods. Because the DOM works with [`in`](https://docs.python.org/3.14/reference/expressions.html#in) parameters alone, you supply the arguments in their usual left-to-right sequence. None of them is optional. A `void` operation gives back `None`.

- An IDL attribute corresponds to an instance attribute. So as to stay compatible with the OMG IDL language mapping for Python, an attribute `foo` is reachable as well through the accessor methods `_get_foo()` and `_set_foo()`. A `readonly` attribute is one you must leave alone, though nothing at runtime enforces that.

- Each of the types `short int`, `unsigned int`, `unsigned long long`, and `boolean` corresponds to a Python integer object.

- The `DOMString` type corresponds to Python strings. While `xml.dom.minidom` accepts bytes or strings alike, what it usually turns out is strings. A `DOMString` value can be `None` too, wherever the W3C's DOM specification permits it to take the IDL `null` value.

- A `const` declaration corresponds to a variable within its own scope (for instance `xml.dom.minidom.Node.PROCESSING_INSTRUCTION_NODE`), and such variables are not to be altered.

- At present `xml.dom.minidom` carries no support for `DOMException`. In its place, `xml.dom.minidom` falls back on ordinary Python exceptions like [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) and [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError).

- A `NodeList` object is built on Python's built-in list type. Such objects expose the interface the DOM specification calls for, yet under older Python versions they fall short of the official API. Even so, they come across as far more “Pythonic” than the interface the W3C recommendations describe.

These interfaces go unimplemented in `xml.dom.minidom`:

- `DOMTimeStamp`

- `EntityReference`

For the most part, these carry XML document information that holds little practical value for the typical DOM user.

Footnotes

[Subject index](INDEX.md) · [Previous](dom-example.md) · [Continue](../xml-dom-pulldom/xml-dom-pulldom-support-for-building-partial-dom-trees.md) · [Owning module, declaration or section: xml.dom.minidom](xml-dom-minidom-parse-to-xml-dom-minidom-parsestring.md)
