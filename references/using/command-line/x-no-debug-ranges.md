# -X no_debug_ranges

- `-X no_debug_ranges` turns off the inclusion of the tables that map extra location information (end line, start column offset and end column offset) onto each instruction in code objects. This helps when you want smaller code objects and pyc files, and also when you wish to suppress the additional visual location markers that appear when the interpreter prints tracebacks. See also `PYTHONNODEBUGRANGES`.

Added in version 3.11.

[Subject index](INDEX.md) · [Previous source section](x-warn-default-encoding.md) · [Following source section](x-frozen-modules.md)
