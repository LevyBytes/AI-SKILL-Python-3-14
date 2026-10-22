# dis: `dis.stack_effect()`

dis.stack_effect(*opcode*, *oparg=None*, ***, *jump=None*)

Work out the stack effect of *opcode* given the argument *oparg*.

When the code carries a jump target and *jump* is `True`, `stack_effect()` returns the stack effect of taking the jump. When *jump* is `False`, the stack effect returned is for not jumping. And when *jump* is `None` (the default), what comes back is the larger stack effect of the two scenarios.

Added in version 3.4.

Changed in version 3.8: Brought in the *jump* parameter.

Changed in version 3.13: When `oparg` is left out (or set to `None`), the stack effect now comes back for `oparg=0`. Formerly that raised an error for opcodes consuming their arg. Likewise, passing an integer `oparg` where the `opcode` ignores it is no longer an error; that `oparg` is simply disregarded.

[Subject index](INDEX.md) · [Previous](dis-disassemble-to-dis-findlabels.md) · [Continue](dis-instruction-class.md) · [Owning module, declaration or section: dis](dis-disassembler-for-python-bytecode.md) · [Owning module, declaration or section: Analysis functions](dis-code-info-to-dis-distb.md)
