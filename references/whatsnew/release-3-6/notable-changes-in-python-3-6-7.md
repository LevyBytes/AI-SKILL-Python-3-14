# What's New In Python 3.6 / Notable changes in Python 3.6.7 - tokenize, xml.dom.minidom, xml.sax

### Notable changes in Python 3.6.7

By default, external entities are no longer handled by the [`xml.dom.minidom`](https://docs.python.org/3.14/library/xml.dom.minidom.html#module-xml.dom.minidom) and [`xml.sax`](https://docs.python.org/3.14/library/xml.sax.html#module-xml.sax) modules. Consult also [gh-61441](https://github.com/python/cpython/issues/61441).

Starting in 3.6.7, whenever the [`tokenize`](https://docs.python.org/3.14/library/tokenize.html#module-tokenize) module is handed input lacking a closing newline, it quietly produces a `NEWLINE` token. That conduct now lines up with how the C tokenizer operates under the hood. (Contributed by Ammar Askar in [bpo-33899](https://bugs.python.org/issue?@action=redirect&bpo=33899).)

[Subject index](INDEX.md) · [Previous source section](notable-changes-in-python-3-6-5.md) · [Next source section](notable-changes-in-python-3-6-10.md) · [Release/subject declaration](summary-release-highlights.md)
