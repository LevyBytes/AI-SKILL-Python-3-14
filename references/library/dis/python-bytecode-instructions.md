# dis: Instruction opcode and decoded operand fields

opcode

the operation's numeric code, matching the opcode values given farther down plus the bytecode values within the Opcode collections.

 opname

the operation's human readable name

 baseopcode

the base operation's numeric code where the operation is specialized; if not, the same as `opcode`

 baseopname

the base operation's human readable name where the operation is specialized; if not, the same as `opname`

 arg

the operation's numeric argument (where one exists), or else `None`

 oparg

alias for `arg`

 argval

the arg value once resolved (where one exists), or else `None`

 argrepr

a human readable account of the operation argument (where one exists), or else an empty string.

 offset

where the operation begins within the bytecode sequence, as an index

 start_offset

the operation's starting index inside the bytecode sequence, counting any prefixed `EXTENDED_ARG` operations when present; if not, the same as `offset`

 cache_offset

the starting index of the cache entries that come after the operation

 end_offset

the ending index of the cache entries that come after the operation

 starts_line

`True` when this opcode begins a source line, or else `False`

 line_number

the source line number tied to this opcode (where one exists), or else `None`

 is_jump_target

`True` when other code jumps here, or else `False`

 jump_target

the bytecode index of the jump target when this is a jump operation, or else `None`

 positions

`dis.Positions` object that carries the starting and ending locations this instruction spans.

 cache_info

Details about this instruction's cache entries, given as triplets shaped like `(name, size, data)`, in which the `name` and `size` spell out the cache format while data holds the cache's contents. `cache_info` is `None` when the instruction carries no caches.

Added in version 3.4.

Changed in version 3.11: The `positions` field is added here.

Changed in version 3.13: The `starts_line` field was changed.

Added fields `start_offset`, `cache_offset`, `end_offset`, `baseopname`, `baseopcode`, `jump_target`, `oparg`, `line_number` and `cache_info`.

PUSH_EXC_INFO

Removes a value from the stack. Places the active exception at the top of the stack. Restores the value that was first removed back onto the stack. Employed within exception handlers.

Added in version 3.11.

[Subject index](INDEX.md) · [Previous](dis-instruction-class.md) · [Continue](dis-positions-class-to-dis-positions-swap.md) · [Owning module, declaration or section: dis](dis-disassembler-for-python-bytecode.md) · [Owning module, declaration or section: dis.Instruction](dis-instruction-class.md) · [Owning module, declaration or section: Python Bytecode Instructions](dis-instruction-class.md) · [Continue](dis-positions-store-name-to-dis-positions-unpack-sequence.md)
