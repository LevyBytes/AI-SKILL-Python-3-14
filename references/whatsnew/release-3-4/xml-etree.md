# What's New In Python 3.4 / xml.etree — xml.etree.elementtree

### xml.etree

A brand-new parser, [`XMLPullParser`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLPullParser), lets non-blocking applications work through XML documents. You can find a worked example over at [Pull API for non-blocking parsing](https://docs.python.org/3.14/library/xml.etree.elementtree.html#elementtree-pull-parsing). (Contributed by Antoine Pitrou in [bpo-17741](https://bugs.python.org/issue?@action=redirect&bpo=17741).)

The [`xml.etree.ElementTree`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#module-xml.etree.ElementTree) [`tostring()`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.tostring) and [`tostringlist()`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.tostringlist) functions, plus the [`ElementTree`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree) [`write()`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree.write) method, have picked up a *short_empty_elements* [keyword-only parameter](https://docs.python.org/3.14/glossary.html#keyword-only-parameter) that lets you decide whether content-free elements get serialized in the short (`<tag />`) or the long (`<tag></tag>`) form. (Contributed by Ariel Poliak and Serhiy Storchaka in [bpo-14377](https://bugs.python.org/issue?@action=redirect&bpo=14377).)

[Subject index](INDEX.md) · [Previous source section](weakref.md) · [Next source section](zipfile.md) · [Release/subject declaration](release-highlights.md)
