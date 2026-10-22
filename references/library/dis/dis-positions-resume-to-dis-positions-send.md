# dis.Positions: `RESUME()`, `SEND()`

RESUME(*context*)

Does nothing operationally. It carries out internal tracing, debugging and optimization checks.

Two distinct fields make up the `context` operand. Where the `RESUME` sits is encoded by the bottom two bits:

- `0` The opening of a function that is not a generator, coroutine, nor an async generator

- `1` Following a `yield` expression

- `2` Following a `yield from` expression

- `3` Following an `await` expression

When the RESUME lands at except-depth `1` the subsequent bit is `1`; otherwise it is `0`.

Added in version 3.11.

Changed in version 3.13: The oparg now also encodes the except-depth detail.

 RETURN_GENERATOR

Build a generator, coroutine, or async generator out of the active frame. This serves as the opening opcode within the code object for the callables named above. It empties the present frame and hands back the freshly built generator.

Added in version 3.11.

 SEND(*delta*)

Equivalent to `STACK[-1] = STACK[-2].send(STACK[-1])`. Used in `yield from` and `await` statements.

Should the call throw [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration), remove the stack's topmost entry, push the `value` attribute carried by the exception, and advance the bytecode counter by *delta*.

Added in version 3.11.

 HAVE_ARGUMENT

This isn't actually an opcode at all. Its purpose is to mark the boundary, among opcodes spanning [0,255], separating those that ignore their argument from those that consume it (`< HAVE_ARGUMENT` versus `>= HAVE_ARGUMENT`, in that order).

When your program deals with pseudo instructions or specialized instructions, reach for the `hasarg` collection in its place.

Changed in version 3.6: Every instruction nowadays carries an argument, though opcodes `< HAVE_ARGUMENT` pay it no attention. Formerly, an argument belonged only to opcodes `>= HAVE_ARGUMENT`.

Changed in version 3.12: With pseudo instructions joining the `dis` module, checking one against `HAVE_ARGUMENT` no longer reliably tells you whether it consumes an arg.

Deprecated since version 3.13: Use `hasarg` instead.

 CALL_INTRINSIC_1

Invokes an intrinsic function passing a single argument. It hands `STACK[-1]` over as that argument and stores the outcome back into `STACK[-1]`. Employed for behavior where performance does not matter.

Which intrinsic function runs is decided by the operand:

| Operand | Description |
| --- | --- |
| `INTRINSIC_1_INVALID` | Not valid |
| `INTRINSIC_PRINT` | Prints the argument to standard out. Used in the REPL. |
| `INTRINSIC_IMPORT_STAR` | Performs `import *` for the named module. |
| `INTRINSIC_STOPITERATION_ERROR` | Extracts the return value from a `StopIteration` exception. |
| `INTRINSIC_ASYNC_GEN_WRAP` | Wraps an async generator value |
| `INTRINSIC_UNARY_POSITIVE` | Performs the unary `+` operation |
| `INTRINSIC_LIST_TO_TUPLE` | Converts a list to a tuple |
| `INTRINSIC_TYPEVAR` | Creates a `typing.TypeVar` |
| `INTRINSIC_PARAMSPEC` | Creates a `typing.ParamSpec` |
| `INTRINSIC_TYPEVARTUPLE` | Creates a `typing.TypeVarTuple` |
| `INTRINSIC_SUBSCRIPT_GENERIC` | Returns `typing.Generic` subscripted with the argument |
| `INTRINSIC_TYPEALIAS` | Creates a `typing.TypeAliasType`; used in the `type` statement. Its argument bundles, as a tuple, the alias name alongside its type parameters and value. |

Added in version 3.12.

[Subject index](INDEX.md) · [Previous](match-class-bytecode-instruction.md) · [Continue](dis-positions-setup-finally-to-dis-positions-load-closure.md) · [Owning module, declaration or section: dis](dis-disassembler-for-python-bytecode.md) · [Owning module, declaration or section: dis.Positions](dis-positions-class-to-dis-positions-swap.md) · [Owning module, declaration or section: Python Bytecode Instructions](dis-instruction-class.md)
