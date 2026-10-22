# dis.Positions: `SETUP_FINALLY()`, `SETUP_CLEANUP()`, `SETUP_WITH()`, `LOAD_CONST_IMMORTAL()`, `LOAD_CLOSURE()`

CALL_INTRINSIC_2

Invokes an intrinsic function passing two arguments. Employed for behavior where performance does not matter:

```python
arg2 = STACK.pop()
arg1 = STACK.pop()
result = intrinsic2(arg1, arg2)
STACK.append(result)

```

Which intrinsic function runs is decided by the operand:

| Operand | Description |
| --- | --- |
| `INTRINSIC_2_INVALID` | Not valid |
| `INTRINSIC_PREP_RERAISE_STAR` | Calculates the `ExceptionGroup` to raise from a `try-except*`. |
| `INTRINSIC_TYPEVAR_WITH_BOUND` | Creates a `typing.TypeVar` with a bound. |
| `INTRINSIC_TYPEVAR_WITH_CONSTRAINTS` | Creates a `typing.TypeVar` with constraints. |
| `INTRINSIC_SET_FUNCTION_TYPE_PARAMS` | Sets the `__type_params__` attribute of a function. |

Added in version 3.12.

 LOAD_SPECIAL

Runs a special method lookup against `STACK[-1]`. When `type(STACK[-1]).__xxx__` turns out to be a method, the stack is left holding `type(STACK[-1]).__xxx__; STACK[-1]`. When `type(STACK[-1]).__xxx__` is not a method, the stack is left holding `STACK[-1].__xxx__; NULL`.

Added in version 3.14.

**Pseudo-instructions**

None of these opcodes show up in Python bytecode. The compiler relies on them, yet they get swapped for genuine opcodes or stripped out before any bytecode is produced.

 SETUP_FINALLY(*target*)

Install an exception handler covering the code block that follows. Should an exception arise, the value stack is wound back to its present level and execution jumps to the handler located at `target`.

 SETUP_CLEANUP(*target*)

Behaves like `SETUP_FINALLY`, except that when an exception arises it additionally pushes the final instruction (`lasti`) onto the stack, enabling `RERAISE` to bring it back. On an exception, both the value stack level and the frame's last instruction are wound back to their present state, and execution jumps to the handler located at `target`.

 SETUP_WITH(*target*)

Behaves like `SETUP_CLEANUP`, except that when an exception arises one extra item is taken off the stack before execution jumps to the handler located at `target`.

You will find this variant inside [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) and [`async with`](https://docs.python.org/3.14/reference/compound_stmts.html#async-with) blocks, where the stack receives whatever the context manager’s [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) or [`__aenter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__aenter__) returns.

 POP_BLOCK

Signals where the code block tied to the most recent `SETUP_FINALLY`, `SETUP_CLEANUP` or `SETUP_WITH` finishes.

 LOAD_CONST_IMMORTAL(*consti*)

Functions like `LOAD_CONST`, though it handles immortal objects more efficiently.

 JUMP

 JUMP_NO_INTERRUPT

Undirected relative jumps that the assembler swaps out for their directed (forward or backward) equivalents.

 JUMP_IF_TRUE

 JUMP_IF_FALSE

Conditional jumps that leave the stack untouched. Swapped for the run `COPY 1`, `TO_BOOL`, `POP_JUMP_IF_TRUE/FALSE`.

 LOAD_CLOSURE(*i*)

Places a reference onto the stack pointing at the cell held in slot `i` of the “fast locals” storage.

Be aware that the assembler swaps `LOAD_CLOSURE` for `LOAD_FAST`.

Changed in version 3.13: This opcode is now a pseudo-instruction.

[Subject index](INDEX.md) · [Previous](dis-positions-resume-to-dis-positions-send.md) · [Continue](dis-opname-to-dis-hasjabs.md) · [Owning module, declaration or section: dis](dis-disassembler-for-python-bytecode.md) · [Owning module, declaration or section: dis.Positions](dis-positions-class-to-dis-positions-swap.md) · [Owning module, declaration or section: Python Bytecode Instructions](dis-instruction-class.md)
