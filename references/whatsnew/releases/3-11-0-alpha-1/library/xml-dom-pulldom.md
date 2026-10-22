# Python 3.11.0 alpha 1 / library / xml dom pulldom

[bpo-45132](https://bugs.python.org/issue?@action=redirect&bpo=45132): Took out the [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) methods belonging to [`xml.dom.pulldom.DOMEventStream`](https://docs.python.org/3.14/library/xml.dom.pulldom.html#xml.dom.pulldom.DOMEventStream), [`wsgiref.util.FileWrapper`](https://docs.python.org/3.14/library/wsgiref.html#wsgiref.util.FileWrapper), and [`fileinput.FileInput`](https://docs.python.org/3.14/library/fileinput.html#fileinput.FileInput), each deprecated as of Python 3.9.

Hugo van Kemenade supplied this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
