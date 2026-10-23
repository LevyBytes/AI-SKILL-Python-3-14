# What’s New In Python 3.8 / xml - xml.dom.minidom, xml.etree.elementtree, xml.sax

### xml

To guard against DTD and external entity retrieval, the [`xml.dom.minidom`](https://docs.python.org/3.14/library/xml.dom.minidom.html#module-xml.dom.minidom) and [`xml.sax`](https://docs.python.org/3.14/library/xml.sax.html#module-xml.sax) modules henceforth skip processing external entities by default. (Contributed by Christian Heimes in [bpo-17239](https://bugs.python.org/issue?@action=redirect&bpo=17239).)

Within the [`xml.etree.ElementTree`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#module-xml.etree.ElementTree) module, the `.find*()` methods accept wildcard searches: `{*}tag` disregards the namespace, while `{namespace}*` brings back every tag belonging to the named namespace. (Contributed by Stefan Behnel in [bpo-28238](https://bugs.python.org/issue?@action=redirect&bpo=28238).)

A new function, [`canonicalize()`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.canonicalize), in the [`xml.etree.ElementTree`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#module-xml.etree.ElementTree) module implements C14N 2.0. (Contributed by Stefan Behnel in [bpo-13611](https://bugs.python.org/issue?@action=redirect&bpo=13611).)

A [`xml.etree.ElementTree.XMLParser`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser) target object can be notified of namespace declaration events by way of the fresh callback methods `start_ns()` and `end_ns()`. Furthermore, you can set up the [`xml.etree.ElementTree.TreeBuilder`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.TreeBuilder) target so it handles events for comments and processing instructions, folding them into the tree it produces. (Contributed by Stefan Behnel in [bpo-36676](https://bugs.python.org/issue?@action=redirect&bpo=36676) and [bpo-36673](https://bugs.python.org/issue?@action=redirect&bpo=36673).)

[Subject index](INDEX.md) · [Previous source section](weakref.md) · [Next source section](xmlrpc.md) · [Release/subject declaration](assignment-expressions.md)
