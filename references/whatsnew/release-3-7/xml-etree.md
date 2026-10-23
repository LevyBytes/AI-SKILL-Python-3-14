# What's New In Python 3.7 / xml.etree - xml.etree.elementtree

### xml.etree

Within the `find()` methods, [ElementPath](https://docs.python.org/3.14/library/xml.etree.elementtree.html#elementtree-xpath) predicates can now match the present node's own text using `[. = "text"]`, not just the text held by children. Spaces may also be inserted into predicates to make them easier to read. (Contributed by Stefan Behnel in [bpo-31648](https://bugs.python.org/issue?@action=redirect&bpo=31648).)

[Subject index](INDEX.md) · [Previous source section](xml.md) · [Next source section](xmlrpc-server.md) · [Release/subject declaration](summary-release-highlights.md)
