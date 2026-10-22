# Python 3.13.0 alpha 3 / library / pyexpat

[gh-111784](https://github.com/python/cpython/issues/111784): Resolved segfaults within the `_elementtree` module. The first segfault, during deallocation of `_elementtree.XMLParser` instances, is fixed by retaining a strong reference to the `pyexpat` module inside module state for the capsule lifetime. The second segfault, which arises during that same deallocation, is fixed by retaining a strong reference to the `_elementtree` module inside the `XMLParser` structure for the `_elementtree` module lifetime.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
