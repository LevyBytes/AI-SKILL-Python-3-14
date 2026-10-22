# dis: `dis.Bytecode`

### Bytecode analysis

Added in version 3.4.

Through the bytecode analysis API, fragments of Python code can be enclosed in a `Bytecode` object that exposes convenient access to the compiled code's specifics.

 *class *dis.Bytecode(*x*, ***, *first_line=None*, *current_offset=None*, *show_caches=False*, *adaptive=False*, *show_offsets=False*, *show_positions=False*)

Examine the bytecode tied to a function, generator, asynchronous generator, coroutine, method, source code string, or a code object (such as what [`compile()`](https://docs.python.org/3.14/library/functions.html#compile) hands back).

Serving as a handy wrapper over numerous functions described farther down — chiefly `get_instructions()` — this means that looping over a `Bytecode` instance produces the bytecode operations as `Instruction` instances.

When *first_line* is something other than `None`, it states which line number ought to be reported for the disassembled code's opening source line. Failing that, the source line data (if there is any) comes straight from the disassembled code object.

When *current_offset* is something other than `None`, it points to an instruction offset inside the disassembled code. Configuring this causes `dis()` to render a “current instruction” marker beside the named opcode.

When *show_caches* is `True`, `dis()` renders the inline cache entries the interpreter relies on to specialize the bytecode.

When *adaptive* is `True`, `dis()` renders specialized bytecode that can diverge from the original bytecode.

When *show_offsets* is `True`, `dis()` adds instruction offsets into the output.

When *show_positions* is `True`, `dis()` adds instruction source code positions into the output.

[Subject index](INDEX.md) · [Previous](command-line-interface.md) · [Continue](dis-bytecode-dis-to-dis-bytecode-info.md) · [Owning module, declaration or section: dis](dis-disassembler-for-python-bytecode.md)
