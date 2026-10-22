# Python 3.14.6 final / library / pyexpat

[gh-148441](https://github.com/python/cpython/issues/148441): [`xml.parsers.expat`](https://docs.python.org/3.14/library/pyexpat.html#module-xml.parsers.expat): head off a segfault within [`CharacterDataHandler()`](https://docs.python.org/3.14/library/pyexpat.html#xml.parsers.expat.xmlparser.CharacterDataHandler) once the character data length surpasses the parser’s [`buffer size`](https://docs.python.org/3.14/library/pyexpat.html#xml.parsers.expat.xmlparser.buffer_size).

[gh-90949](https://github.com/python/cpython/issues/90949): Attach [`SetBillionLaughsAttackProtectionActivationThreshold()`](https://docs.python.org/3.14/library/pyexpat.html#xml.parsers.expat.xmlparser.SetBillionLaughsAttackProtectionActivationThreshold) plus [`SetBillionLaughsAttackProtectionMaximumAmplification()`](https://docs.python.org/3.14/library/pyexpat.html#xml.parsers.expat.xmlparser.SetBillionLaughsAttackProtectionMaximumAmplification) onto [xmlparser](https://docs.python.org/3.14/library/pyexpat.html#xmlparser-objects) objects so the safeguards against [billion laughs](https://en.wikipedia.org/wiki/Billion_laughs_attack) attacks can be tuned. Bénédikt Tran authored the change.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
