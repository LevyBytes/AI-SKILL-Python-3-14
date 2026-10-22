# Python 3.11.0 alpha 3 / core and builtins / compiler and parser

[bpo-45727](https://bugs.python.org/issue?@action=redirect&bpo=45727): Narrow the bespoke syntax error hinting at a possible missing comma so it fires solely when the expressions appear inside parentheses or brackets. The patch came from Pablo Galindo

[bpo-45885](https://bugs.python.org/issue?@action=redirect&bpo=45885): Using the PEP 659 machinery, the `COMPARE_OP` opcode was specialized.

[bpo-45450](https://bugs.python.org/issue?@action=redirect&bpo=45450): Sharpen the syntax error wording for parenthesized arguments. Pablo Galindo supplied the patch.

[bpo-45811](https://bugs.python.org/issue?@action=redirect&bpo=45811): Better tokenizer diagnostics when the parser runs into invisible control characters. The patch came from Pablo Galindo

[bpo-45848](https://bugs.python.org/issue?@action=redirect&bpo=45848): Permit the parser to read error lines straight from encoded files. The patch came from Pablo Galindo

[bpo-45822](https://bugs.python.org/issue?@action=redirect&bpo=45822): Fixed a parser bug that made it ignore [**PEP 263**](https://peps.python.org/pep-0263/) coding cookies whenever no flags were supplied. The patch came from Pablo Galindo

[bpo-45820](https://bugs.python.org/issue?@action=redirect&bpo=45820): Address a segfault occurring when the parser fails before consuming any input. The patch came from Pablo Galindo

[bpo-45738](https://bugs.python.org/issue?@action=redirect&bpo=45738): Correct how the parser computes the error position for invalid continuation characters. Pablo Galindo supplied the patch.

[bpo-45773](https://bugs.python.org/issue?@action=redirect&bpo=45773): Resolve a compiler hang that occurred while trying to optimize particular jump patterns.

[bpo-45609](https://bugs.python.org/issue?@action=redirect&bpo=45609): Using the PEP 659 machinery, the `STORE_SUBSCR` opcode was specialized.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
