# Python 3.14.1 final / library / pyexpat

[gh-90949](https://github.com/python/cpython/issues/90949): Gives [xmlparser](https://docs.python.org/3.14/library/pyexpat.html#xmlparser-objects) objects the [`SetAllocTrackerActivationThreshold()`](https://docs.python.org/3.14/library/pyexpat.html#xml.parsers.expat.xmlparser.SetAllocTrackerActivationThreshold) and [`SetAllocTrackerMaximumAmplification()`](https://docs.python.org/3.14/library/pyexpat.html#xml.parsers.expat.xmlparser.SetAllocTrackerMaximumAmplification) methods to fine-tune the safeguards against disproportional amounts of dynamic memory usage inside an Expat parser. Bénédikt Tran authored the patch.

[gh-140593](https://github.com/python/cpython/issues/140593): [`xml.parsers.expat`](https://docs.python.org/3.14/library/pyexpat.html#module-xml.parsers.expat): closes a memory leak that could hit anyone whose [`ElementDeclHandler()`](https://docs.python.org/3.14/library/pyexpat.html#xml.parsers.expat.xmlparser.ElementDeclHandler) pointed at a custom element declaration handler. Sebastian Pipping authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
