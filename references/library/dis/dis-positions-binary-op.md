# dis.Positions: `BINARY_OP()`

CACHE

This opcode is not a genuine instruction; instead it earmarks additional room so the interpreter can cache useful data right inside the bytecode itself. Every `dis` utility conceals it automatically, although `show_caches=True` will reveal it.

In logical terms, this room belongs to the instruction that comes before it. A great many opcodes anticipate being trailed by a precise count of caches, and they direct the interpreter to step past them at runtime.

Because populated caches can resemble arbitrary instructions, you must exercise great caution while reading or altering raw, adaptive bytecode that holds quickened data.

Added in version 3.11.

**Unary operations**

A unary operation grabs the stack's top value, runs the operation on it, then pushes the outcome back onto the stack.

 UNARY_NEGATIVE

Implements `STACK[-1] = -STACK[-1]`.

 UNARY_NOT

Implements `STACK[-1] = not STACK[-1]`.

Changed in version 3.13: An exact [`bool`](https://docs.python.org/3.14/library/functions.html#bool) operand is now demanded by this instruction.

 UNARY_INVERT

Implements `STACK[-1] = ~STACK[-1]`.

 GET_ITER

Implements `STACK[-1] = iter(STACK[-1])`.

 GET_YIELD_FROM_ITER

When `STACK[-1]` is already a [generator iterator](https://docs.python.org/3.14/glossary.html#term-generator-iterator) or [coroutine](https://docs.python.org/3.14/glossary.html#term-coroutine) object, it stays untouched. If not, this implements `STACK[-1] = iter(STACK[-1])`.

Added in version 3.5.

 TO_BOOL

Implements `STACK[-1] = bool(STACK[-1])`.

Added in version 3.13.

**Binary and in-place operations**

Binary operations strip the top pair of items off the stack (`STACK[-1]` and `STACK[-2]`). They carry out the operation, then place the result back onto the stack.

In-place operations resemble binary operations, except that the work happens in-place whenever `STACK[-2]` allows it, and the resulting `STACK[-1]` might (though it need not) be the original `STACK[-2]`.

 BINARY_OP(*op*)

Carries out the binary as well as the in-place operators (according to what *op* is set to):

```python
rhs = STACK.pop()
lhs = STACK.pop()
STACK.append(lhs op rhs)

```

Added in version 3.11.

Changed in version 3.14: With oparg :`NB_SUBSCR`, implements binary subscript (replaces opcode `BINARY_SUBSCR`)

 STORE_SUBSCR

Implements:

```python
key = STACK.pop()
container = STACK.pop()
value = STACK.pop()
container[key] = value

```

[Subject index](INDEX.md) · [Previous](dis-positions-class-to-dis-positions-swap.md) · [Continue](dis-positions-get-awaitable.md) · [Owning module, declaration or section: dis](dis-disassembler-for-python-bytecode.md) · [Owning module, declaration or section: dis.Positions](dis-positions-class-to-dis-positions-swap.md) · [Owning module, declaration or section: Python Bytecode Instructions](dis-instruction-class.md)
