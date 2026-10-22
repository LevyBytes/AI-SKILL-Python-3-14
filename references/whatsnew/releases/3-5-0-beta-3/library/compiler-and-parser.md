# Python 3.5.0 beta 3 / library / compiler and parser

[bpo-19176](https://bugs.python.org/issue?@action=redirect&bpo=19176): Corrected doctype()-related defects in the C implementation of ElementTree. An XMLParser subclass carrying the default doctype() method no longer triggers a deprecation warning. Calling doctype() directly now raises a warning. When the target's doctype() runs, the parser's own doctype() is no longer invoked. Martin Panter's patch was the basis.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
