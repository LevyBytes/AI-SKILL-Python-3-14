# xml.etree.ElementTree.Element: `clear()`, `get()`, `items()`, `keys()`, `set()`, `append()`, `extend()`, `find()`, `findall()`, `findtext()`, `insert()`, `iter()`

tag

A string that names the kind of data this element stands for (that is, the element type).

 text

 tail

These two attributes serve to carry extra data tied to the element. Typically their values are strings, though they may be any application-specific object. When the element originates in an XML file, the *text* attribute holds whatever text falls after the element's start tag and before its first child (or its end tag), or else `None`; the *tail* attribute holds whatever text falls after the element's end tag and before the next tag, or else `None`. Given the XML data

```xml
<a><b>1<c>2<d/>3</c></b>4</a>

```

the *a* element holds `None` for both its *text* and *tail* attributes, the *b* element holds *text* `"1"` and *tail* `"4"`, the *c* element holds *text* `"2"` and *tail* `None`, and the *d* element holds *text* `None` and *tail* `"3"`.

For gathering the inner text of an element, consult `itertext()`, as in `"".join(element.itertext())`.

Programs are free to stash arbitrary objects within these attributes.

 attrib

A dictionary that holds the element's attributes. Bear in mind that although the *attrib* value is invariably a genuine mutable Python dictionary, an ElementTree implementation is allowed to keep some other internal form and only materialize the dictionary on demand. To benefit from such implementations, lean on the dictionary methods listed below wherever you can.

The dictionary-style methods below operate on the element attributes.

 clear()

Resets an element. This call strips out every subelement, wipes all attributes, and sets both the text and tail attributes to `None`.

 get(*key*, *default=None*)

Fetches the element attribute called *key*.

The return value is the attribute's value, or *default* when the attribute was absent.

 items()

Hands back the element attributes as a sequence of (name, value) pairs. The ordering of the attributes is arbitrary.

 keys()

Hands back the element's attribute names as a list. Their ordering is arbitrary.

 set(*key*, *value*)

Set the attribute *key* on the element to *value*.

The methods below act on the element's children (subelements).

 append(*subelement*)

Tacks the element *subelement* onto the tail of this element's internal subelement list. Raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) if *subelement* is not an `Element`.

 extend(*subelements*)

Appends *subelements* drawn from an iterable of elements. Raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) if a subelement is not an `Element`.

Added in version 3.2.

 find(*match*, *namespaces=None*)

Locates the first subelement that matches *match*. *match* may be a tag name or a path. What comes back is an element instance, or `None`. *namespaces*, an optional argument, maps a namespace prefix onto its full name. Hand `''` as the prefix to push every unprefixed tag name in the expression into the supplied namespace.

 findall(*match*, *namespaces=None*)

Locates every matching subelement, by tag name or path. What comes back is a list holding all matching elements, in document order. *namespaces*, an optional argument, maps a namespace prefix onto its full name. Hand `''` as the prefix to push every unprefixed tag name in the expression into the supplied namespace.

 findtext(*match*, *default=None*, *namespaces=None*)

Locates text belonging to the first subelement that matches *match*. A tag name or a path may serve as *match*. The return value is the text content of the first matching element, or *default* when no element turned up. Keep in mind that when the matching element has no text content, an empty string comes back. *namespaces*, an optional argument, maps a namespace prefix onto its full name. Hand `''` as the prefix to push every unprefixed tag name in the expression into the supplied namespace.

 insert(*index*, *subelement*)

Slots *subelement* into the stated position in this element. Raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) if *subelement* is not an `Element`.

 iter(*tag=None*)

Builds a tree [iterator](https://docs.python.org/3.14/glossary.html#term-iterator) rooted at the current element. The iterator walks over this element and every element beneath it, in document (depth first) order. When *tag* is something other than `None` or `'*'`, the iterator yields only elements whose tag equals *tag*. Modifying the tree structure mid-iteration leaves the outcome undefined.

Added in version 3.2.

[Subject index](INDEX.md) · [Previous](xml-etree-elementtree-element-class.md) · [Continue](xml-element-query-insertion-and-removal.md) · [Owning module, declaration or section: xml.etree.ElementTree](xml-etree-elementtree-the-elementtree-xml-api.md) · [Owning module, declaration or section: xml.etree.ElementTree.Element](xml-etree-elementtree-element-class.md) · [Owning module, declaration or section: Element Objects](xml-etree-elementtree-element-class.md)
