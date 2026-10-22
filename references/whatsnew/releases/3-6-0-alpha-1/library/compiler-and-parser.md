# Python 3.6.0 alpha 1 / library / compiler and parser

[bpo-25638](https://bugs.python.org/issue?@action=redirect&bpo=25638): ElementTree.iterparse() was optimized and now runs 2x faster, while ElementTree parsing was optimized and runs 10% faster.

[bpo-25380](https://bugs.python.org/issue?@action=redirect&bpo=25380): Corrected the protocol governing the STACK_GLOBAL opcode inside pickletools.opcodes.

[bpo-23718](https://bugs.python.org/issue?@action=redirect&bpo=23718): Repaired the parsing of times falling in week 0 ahead of Jan 1. Tamás Bence Gedai supplied the original patch.

[bpo-22642](https://bugs.python.org/issue?@action=redirect&bpo=22642): The trace module's option parsing was migrated over to argparse. SilentGhost sent in the patch.

[bpo-25554](https://bugs.python.org/issue?@action=redirect&bpo=25554): Eliminated circular references arising during regular expression parsing.

[bpo-25382](https://bugs.python.org/issue?@action=redirect&bpo=25382): For the MEMOIZE opcode, pickletools.dis() now prints the implicit memo index.

[bpo-25850](https://bugs.python.org/issue?@action=redirect&bpo=25850): For 64-bit Windows, cross-compilation is now the default.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
