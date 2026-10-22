# Python 3.5.1 release candidate 1 / library / compiler and parser

[bpo-25554](https://bugs.python.org/issue?@action=redirect&bpo=25554): Eliminated circular references during regular expression parsing.

[bpo-25380](https://bugs.python.org/issue?@action=redirect&bpo=25380): Corrected the protocol of the STACK_GLOBAL opcode within pickletools.opcodes.

[bpo-25262](https://bugs.python.org/issue?@action=redirect&bpo=25262): The pure-Python unpickler gained handling for the BINBYTES8 opcode. On 32-bit platforms the C implementation previously discarded the top 32 bits of the 64-bit length for the BINUNICODE8 and BINBYTES8 opcodes without warning; that no longer happens.

[bpo-25060](https://bugs.python.org/issue?@action=redirect&bpo=25060): The BUILD_MAP opcode's stack usage is now computed correctly.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
