# dis: `dis.disassemble()`, `dis.disco()`, `dis.get_instructions()`, `dis.findlinestarts()`, `dis.findlabels()`

dis.disassemble(*code*, *lasti=-1*, ***, *file=None*, *show_caches=False*, *adaptive=False*, *show_offsets=False*, *show_positions=False*)

 dis.disco(*code*, *lasti=-1*, ***, *file=None*, *show_caches=False*, *adaptive=False*, *show_offsets=False*, *show_positions=False*)

Disassemble a code object, flagging the final instruction whenever *lasti* is supplied. These are the columns into which the output is split:

1.

the instruction's location within the source code. Full location detail appears when *show_positions* is true. If not (which is the default), what shows is just the line number.

2.

the current instruction, indicated as `-->`,

3.

a labelled instruction, indicated with `>>`,

4.

the address of the instruction,

5.

the operation code name,

6.

operation parameters, and

7.

interpretation of the parameters in parentheses.

Interpreting the parameters covers local and global variable names, constant values, branch targets, and compare operators.

Text from the disassembly goes to the *file* argument you pass when one is given, and otherwise to `sys.stdout`.

Changed in version 3.4: Brought in the *file* parameter.

Changed in version 3.11: Brought in the *show_caches* together with the *adaptive* parameters.

Changed in version 3.13: Brought in the *show_offsets* parameter.

Changed in version 3.14: Brought in the *show_positions* parameter.

 dis.get_instructions(*x*, ***, *first_line=None*, *show_caches=False*, *adaptive=False*)

Hand back an iterator across the instructions found in the given function, method, source code string or code object.

What the iterator yields is a run of `Instruction` named tuples spelling out the particulars of every operation within the supplied code.

When *first_line* is something other than `None`, it states which line number ought to be reported for the disassembled code's opening source line. Failing that, the source line data (if there is any) comes straight from the disassembled code object.

The *adaptive* parameter behaves the same way it does within `dis()`.

Added in version 3.4.

Changed in version 3.11: Brought in the *show_caches* together with the *adaptive* parameters.

Changed in version 3.13: The *show_caches* parameter is now deprecated and does nothing. The iterator produces the `Instruction` instances carrying a populated *cache_info* field (no matter what *show_caches* is set to) and stops yielding separate entries for the cache entries.

 dis.findlinestarts(*code*)

By way of the [`co_lines()`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_lines) method belonging to the [code object](https://docs.python.org/3.14/reference/datamodel.html#code-objects) *code*, this generator function locates the offsets that begin lines within the source code. They emerge as `(offset, lineno)` pairs.

Changed in version 3.6: It is now possible for line numbers to decrease. Earlier they only ever rose.

Changed in version 3.10: In place of the [code object](https://docs.python.org/3.14/reference/datamodel.html#code-objects)'s [`co_firstlineno`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_firstlineno) and [`co_lnotab`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_lnotab) attributes, the [**PEP 626**](https://peps.python.org/pep-0626/) [`co_lines()`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_lines) method is now what gets used.

Changed in version 3.13: For bytecode lacking a mapping to source lines, line numbers may come back as `None`.

 dis.findlabels(*code*)

Within the raw compiled bytecode string *code*, locate every offset acting as a jump target, and return those offsets as a list.

[Subject index](INDEX.md) · [Previous](dis-code-info-to-dis-distb.md) · [Continue](dis-stack-effect.md) · [Owning module, declaration or section: dis](dis-disassembler-for-python-bytecode.md) · [Owning module, declaration or section: Analysis functions](dis-code-info-to-dis-distb.md)
