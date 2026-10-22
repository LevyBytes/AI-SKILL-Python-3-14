# dis.Positions: Membership, imports, jumps and loop bytecodes

CONTAINS_OP(*invert*)

Carries out an `in` comparison, or `not in` when `invert` is 1.

Added in version 3.9.

 IMPORT_NAME(*namei*)

Brings in the module `co_names[namei]`. Both `STACK[-1]` and `STACK[-2]` are popped and supply the *fromlist* and *level* arguments for [`__import__()`](https://docs.python.org/3.14/library/functions.html#import__). The module object is then placed onto the stack. The present namespace stays untouched: for a real import statement, a following `STORE_FAST` instruction alters the namespace.

 IMPORT_FROM(*namei*)

Loads the attribute `co_names[namei]` out of the module held in `STACK[-1]`. The resulting object is placed onto the stack, later to be stored by a `STORE_FAST` instruction.

 JUMP_FORWARD(*delta*)

Adds *delta* to the bytecode counter.

 JUMP_BACKWARD(*delta*)

Subtracts *delta* from the bytecode counter. Checks for interrupts.

Added in version 3.11.

 JUMP_BACKWARD_NO_INTERRUPT(*delta*)

Subtracts *delta* from the bytecode counter. Skips checking for interrupts.

Added in version 3.11.

 POP_JUMP_IF_TRUE(*delta*)

When `STACK[-1]` is true, adds *delta* to the bytecode counter. `STACK[-1]` is popped.

Changed in version 3.11: The oparg is now a relative delta instead of an absolute target. This opcode acts as a pseudo-instruction, swapped out in final bytecode for the directed variants (forward/backward).

Changed in version 3.12: This is no longer a pseudo-instruction.

Changed in version 3.13: This instruction now demands an exact [`bool`](https://docs.python.org/3.14/library/functions.html#bool) operand.

 POP_JUMP_IF_FALSE(*delta*)

When `STACK[-1]` is false, adds *delta* to the bytecode counter. `STACK[-1]` is popped.

Changed in version 3.11: The oparg is now a relative delta instead of an absolute target. This opcode acts as a pseudo-instruction, swapped out in final bytecode for the directed variants (forward/backward).

Changed in version 3.12: This is no longer a pseudo-instruction.

Changed in version 3.13: This instruction now demands an exact [`bool`](https://docs.python.org/3.14/library/functions.html#bool) operand.

 POP_JUMP_IF_NOT_NONE(*delta*)

When `STACK[-1]` is not `None`, adds *delta* to the bytecode counter. `STACK[-1]` is popped.

Added in version 3.11.

Changed in version 3.12: This is no longer a pseudo-instruction.

 POP_JUMP_IF_NONE(*delta*)

When `STACK[-1]` is `None`, adds *delta* to the bytecode counter. `STACK[-1]` is popped.

Added in version 3.11.

Changed in version 3.12: This is no longer a pseudo-instruction.

 FOR_ITER(*delta*)

Here `STACK[-1]` is an [iterator](https://docs.python.org/3.14/glossary.html#term-iterator). Its [`__next__()`](https://docs.python.org/3.14/library/stdtypes.html#iterator.__next__) method is called. Should that produce a fresh value, it is pushed onto the stack (with the iterator left beneath it). Should the iterator report that it is exhausted, the byte code counter is increased by *delta*.

Changed in version 3.12: Through 3.11 the iterator was popped once it became exhausted.

 LOAD_GLOBAL(*namei*)

Loads the global called `co_names[namei>>1]` onto the stack.

Changed in version 3.11: When the low bit of `namei` is set, a `NULL` gets pushed onto the stack ahead of the global variable.

 LOAD_FAST(*var_num*)

Places a reference to the local `co_varnames[var_num]` onto the stack.

Changed in version 3.12: This opcode is now reserved for cases where the local variable is certain to have been initialized. It cannot raise [`UnboundLocalError`](https://docs.python.org/3.14/library/exceptions.html#UnboundLocalError).

[Subject index](INDEX.md) · [Previous](dis-positions-set-update-to-dis-positions-is-op.md) · [Continue](dis-positions-load-fast-borrow-to-dis-positions-delete-deref.md) · [Owning module, declaration or section: dis](dis-disassembler-for-python-bytecode.md) · [Owning module, declaration or section: dis.Positions](dis-positions-class-to-dis-positions-swap.md) · [Owning module, declaration or section: Python Bytecode Instructions](dis-instruction-class.md)
