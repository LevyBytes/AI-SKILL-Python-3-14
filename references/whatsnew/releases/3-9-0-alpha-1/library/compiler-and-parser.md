# Python 3.9.0 alpha 1 / library / compiler and parser

[bpo-29412](https://bugs.python.org/issue?@action=redirect&bpo=29412): Cleared an IndexError that arose while parsing a header value which ended without warning. Abhilash Raj authored the patch.

[bpo-38115](https://bugs.python.org/issue?@action=redirect&bpo=38115): Resolved a defect in dis.findlinestarts() that made it hand back invalid bytecode offsets. It is now documented that the co_lnotab of a code object may hold invalid bytecode offsets.

[bpo-35805](https://bugs.python.org/issue?@action=redirect&bpo=35805): Introduced a parser for the Message-ID header and registered it in the default HeaderRegistry. Doing so ought to keep Message-ID from being folded with RFC 2048 encoded words.

[bpo-37268](https://bugs.python.org/issue?@action=redirect&bpo=37268): A deprecation now applies to the `parser` module, which is slated for removal in upcoming Python releases.

[bpo-37965](https://bugs.python.org/issue?@action=redirect&bpo=37965): Silenced a C compiler warning produced by distutils.ccompiler.CCompiler.has_function.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
