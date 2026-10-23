# What's New In Python 3.2 / elementtree - xml.etree.elementtree

### elementtree

Both the [`xml.etree.ElementTree`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#module-xml.etree.ElementTree) package and the matching `xml.etree.cElementTree` have been brought up to version 1.3.

A number of handy new functions and methods now exist:

- [`xml.etree.ElementTree.fromstringlist()`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.fromstringlist) which assembles an XML document out of a sequence of fragments

- [`xml.etree.ElementTree.register_namespace()`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.register_namespace) for recording a global namespace prefix

- [`xml.etree.ElementTree.tostringlist()`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.tostringlist) for a string rendering that takes in all sublists

- [`xml.etree.ElementTree.Element.extend()`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.extend) for tacking on a sequence of zero or more elements

- [`xml.etree.ElementTree.Element.iterfind()`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.iterfind) searches an element and subelements

- [`xml.etree.ElementTree.Element.itertext()`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.itertext) creates a text iterator over an element and its subelements

- [`xml.etree.ElementTree.TreeBuilder.end()`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.TreeBuilder.end) closes the current element

- [`xml.etree.ElementTree.TreeBuilder.doctype()`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.TreeBuilder.doctype) handles a doctype declaration

A pair of methods are now deprecated:

- `xml.etree.ElementTree.getchildren()` use `list(elem)` instead.

- `xml.etree.ElementTree.getiterator()` use `Element.iter` instead.

To read up on the update, consult [Introducing ElementTree](https://web.archive.org/web/20200703234532/http://effbot.org/zone/elementtree-13-intro.htm) over on Fredrik Lundh's website.

(Contributed by Florent Xicluna and Fredrik Lundh, [bpo-6472](https://bugs.python.org/issue?@action=redirect&bpo=6472).)

[Subject index](INDEX.md) · [Previous source section](email.md) · [Next source section](functools.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
