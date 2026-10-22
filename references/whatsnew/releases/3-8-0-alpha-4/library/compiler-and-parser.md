# Python 3.8.0 alpha 4 / library / compiler and parser

[bpo-35952](https://bugs.python.org/issue?@action=redirect&bpo=35952): Repaired pythoninfo for the case where no compiler is present.

[bpo-36676](https://bugs.python.org/issue?@action=redirect&bpo=36676): Should a parser target supply the callbacks ?start_ns()? and/or ?end_ns()?, the XMLParser() within xml.etree.ElementTree will now feed it namespace prefix context. Stefan Behnel wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
