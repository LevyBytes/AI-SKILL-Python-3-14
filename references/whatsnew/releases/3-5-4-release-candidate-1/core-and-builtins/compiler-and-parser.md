# Python 3.5.4 release candidate 1 / core and builtins / compiler and parser

[bpo-29537](https://bugs.python.org/issue?@action=redirect&bpo=29537): Bring back runtime compatibility with bytecode files that CPython 3.5.0 through 3.5.2 produced, and tweak the eval loop to dodge the trouble that the malformed BUILD_MAP_UNPACK_WITH_CALL opcode variant those files may carry could trigger. Petr Viktorin, Serhiy Storchaka, and Nick Coghlan wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
