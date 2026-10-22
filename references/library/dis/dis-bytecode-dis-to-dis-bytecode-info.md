# dis.Bytecode: `from_traceback()`, `dis()`, `info()`

*classmethod *from_traceback(*tb*, ***, *show_caches=False*)

Build a `Bytecode` instance out of the supplied traceback, fixing *current_offset* at the instruction that triggered the exception.

 codeobj

The compiled code object.

 first_line

The first source line of the code object (if available)

 dis()

Hand back a formatted rendering of the bytecode operations (identical to what `dis.dis()` prints, except delivered as a multi-line string).

 info()

Hand back a formatted multi-line string carrying thorough information regarding the code object, in the manner of `code_info()`.

Changed in version 3.7: Coroutine and asynchronous generator objects are now handled by this.

Changed in version 3.11: Brought in the *show_caches* together with the *adaptive* parameters.

Changed in version 3.13: Brought in the *show_offsets* parameter

Changed in version 3.14: Brought in the *show_positions* parameter.

Example:

```pycon
>>> bytecode = dis.Bytecode(myfunc)
>>> for instr in bytecode:
...     print(instr.opname)
...
RESUME
LOAD_GLOBAL
LOAD_FAST_BORROW
CALL
RETURN_VALUE

```

[Subject index](INDEX.md) · [Previous](dis-bytecode-class.md) · [Continue](dis-code-info-to-dis-distb.md) · [Owning module, declaration or section: dis](dis-disassembler-for-python-bytecode.md) · [Owning module, declaration or section: dis.Bytecode](dis-bytecode-class.md) · [Owning module, declaration or section: Bytecode analysis](dis-bytecode-class.md)
