# -X importtime

- `-X importtime` to reveal the duration of each import. It lists the module name, cumulative time (nested imports included) and self time (nested imports excluded). Keep in mind that this output can be garbled in a multi-threaded application. The usual invocation is `python -X importtime -c 'import asyncio'`.

`-X importtime=2` turns on extra output that flags when an imported module was already loaded. Whenever that happens, the string `cached` appears in both time columns.

See also `PYTHONPROFILEIMPORTTIME`.

Added in version 3.7.

Changed in version 3.14: introduced `-X importtime=2` so that imports of already-loaded modules get traced too; any value besides `1` and `2` is held back for later use.

[Subject index](INDEX.md) · [Previous source section](x-int-max-str-digits.md) · [Following source section](x-dev.md)
