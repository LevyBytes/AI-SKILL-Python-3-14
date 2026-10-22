# Python 3.7.0 alpha 3 / core and builtins / numbers

[bpo-31618](https://bugs.python.org/issue?@action=redirect&bpo=31618): The per-frame tracing machinery added back in 3.7a1 has been changed so that `frame->f_lineno` gets refreshed ahead of either a `"line"` or an `"opcode"` event firing. Formerly opcode events fired first and could therefore now and then report stale line numbers for the frame. One side effect is a slight behaviour shift: with both `f_trace_lines` and `f_trace_opcodes` turned on, line events now arrive first.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
