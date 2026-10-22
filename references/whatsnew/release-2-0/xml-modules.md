# What’s New in Python 2.0 / XML Modules — xml

### XML Modules

Python 1.5.2 shipped a basic XML parser as the `xmllib` module, contributed by Sjoerd Mullender. Since that 1.5.2 release, two separate ways of working with XML have grown popular: SAX2 (the second version of the Simple API for XML) gives you an event-driven interface somewhat resembling `xmllib`, and the DOM (Document Object Model) gives you a tree-based interface, turning an XML document into a tree of nodes you can walk and edit. Python 2.0 ships a SAX2 interface together with a pared-down DOM interface inside the [`xml`](https://docs.python.org/3.14/library/xml.html#module-xml) package. What follows is a quick tour of these new interfaces; for the full story, see the Python documentation or the source. The Python XML SIG is also at work on better documentation.

[Subject index](INDEX.md) · [Previous source section](distutils-making-modules-easy-to-install.md) · [Next source section](sax2-support.md) · [Release/subject declaration](introduction.md)
