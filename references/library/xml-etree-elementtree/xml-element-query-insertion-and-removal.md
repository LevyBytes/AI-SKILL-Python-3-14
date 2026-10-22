# xml.etree.ElementTree.Element: `iterfind()`, `itertext()`, `makeelement()`, `remove()`

iterfind(*match*, *namespaces=None*)

Locates every matching subelement, by tag name or path. What comes back is an iterable that yields all matching elements, in document order. *namespaces*, an optional argument, maps a namespace prefix onto its full name.

Added in version 3.2.

 itertext()

Builds a text iterator. The iterator runs over this element and every subelement, in document order, returning all inner text.

Added in version 3.2.

 makeelement(*tag*, *attrib*)

Builds a fresh element object of the same type as this element. Refrain from calling this method; reach for the `SubElement()` factory function instead.

 remove(*subelement*)

Deletes *subelement* from the element. Unlike the find* methods, this method matches elements by instance identity rather than by tag value or contents.

`Element` objects additionally support the following sequence type methods for handling subelements: [`__delitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__delitem__), [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__), [`__setitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__setitem__), [`__len__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__len__).

Caution: Elements that have no subelements evaluate as `False`. A coming Python release will make every element evaluate as `True` regardless of whether subelements are present. So instead, favour explicit `len(elem)` or `elem is not None` tests.:

```python
element = root.find('foo')

if not element:  # careful!
    print("element not found, or element has no subelements")

if element is None:
    print("element not found")

```

Changed in version 3.12: Evaluating an Element for its truth value now raises [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning).

Before Python 3.8, the serialisation order of an element's XML attributes was forced to be predictable by sorting those attributes on their name. Resting on the now-guaranteed ordering of dicts, this artificial reordering was dropped in Python 3.8 so that the order in which attributes were first parsed or built by user code is kept.

As a rule, user code ought to avoid relying on any particular attribute ordering, since the [XML Information Set](https://www.w3.org/TR/xml-infoset/) deliberately leaves attribute order out of what carries information. Your code should be ready to cope with whatever ordering arrives on input. Where deterministic XML output matters, for instance with cryptographic signing or test data sets, canonical serialisation is on hand through the `canonicalize()` function.

Where canonical output does not fit yet a particular attribute order is still wanted on output, code should try to create the attributes straight away in the order you want, so that readers of the code are not thrown by a mismatch. Where doing so is awkward, a recipe such as the one below may be run just before serialisation to impose an order that is independent of Element creation:

```python
def reorder_attributes(root):
    for el in root.iter():
        attrib = el.attrib
        if len(attrib) > 1:
            # adjust attribute order, e.g. by sorting
            attribs = sorted(attrib.items())
            attrib.clear()
            attrib.update(attribs)

```

[Subject index](INDEX.md) · [Previous](xml-element-clearing-attributes-and-iteration.md) · [Continue](xml-etree-elementtree-elementtree-class.md) · [Owning module, declaration or section: xml.etree.ElementTree](xml-etree-elementtree-the-elementtree-xml-api.md) · [Owning module, declaration or section: xml.etree.ElementTree.Element](xml-etree-elementtree-element-class.md) · [Owning module, declaration or section: Element Objects](xml-etree-elementtree-element-class.md)
