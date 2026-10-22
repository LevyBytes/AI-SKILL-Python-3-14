# dis.Positions: `SET_ADD()`, `LIST_APPEND()`, `MAP_ADD()`

CLEANUP_THROW

Deals with an exception thrown during a [`throw()`](https://docs.python.org/3.14/reference/expressions.html#generator.throw) or [`close()`](https://docs.python.org/3.14/reference/expressions.html#generator.close) call by way of the current frame. Where `STACK[-1]` is an instance of [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration), pop three values off the stack and push that object's `value` member. If not, re-raise `STACK[-1]`.

Added in version 3.12.

**Miscellaneous opcodes**

 SET_ADD(*i*)

Implements:

```python
item = STACK.pop()
set.add(STACK[-i], item)

```

Used to implement set comprehensions.

 LIST_APPEND(*i*)

Implements:

```python
item = STACK.pop()
list.append(STACK[-i], item)

```

Used to implement list comprehensions.

 MAP_ADD(*i*)

Implements:

```python
value = STACK.pop()
key = STACK.pop()
dict.__setitem__(STACK[-i], key, value)

```

Used to implement dict comprehensions.

Added in version 3.1.

Changed in version 3.8: The map value is `STACK[-1]` while the map key is `STACK[-2]`. Previously those two were the other way around.

Across each of the `SET_ADD`, `LIST_APPEND` and `MAP_ADD` instructions, even as the appended value or key/value pair is popped away, the container object stays on the stack so it remains accessible for the loop's later iterations.

 RETURN_VALUE

Returns with `STACK[-1]` to the caller of the function.

 YIELD_VALUE

Yields `STACK.pop()` from a [generator](https://docs.python.org/3.14/glossary.html#term-generator).

Changed in version 3.11: oparg is set to the depth of the stack.

Changed in version 3.12: oparg is set to the exception block depth, which lets generators close efficiently.

Changed in version 3.13: oparg equals `1` when this instruction belongs to a yield-from or await, and `0` if not.

 SETUP_ANNOTATIONS

Tests whether `__annotations__` exists within `locals()`, and when it does not, sets it up as an empty `dict`. Only when a class or module body statically holds [variable annotations](https://docs.python.org/3.14/glossary.html#term-variable-annotation) does this opcode get emitted.

Added in version 3.6.

 POP_EXCEPT

Takes a value off the stack and uses it to bring the exception state back.

Changed in version 3.11: The stack's exception representation now holds a single item rather than three.

 RERAISE

Throws once more the exception that currently sits atop the stack. Should oparg be non-zero, an extra value is popped off the stack and used to set the current frame's [`f_lasti`](https://docs.python.org/3.14/reference/datamodel.html#frame.f_lasti).

Added in version 3.9.

Changed in version 3.11: The stack's exception representation now holds a single item rather than three.

[Subject index](INDEX.md) · [Previous](dis-positions-get-awaitable.md) · [Owning module, declaration or section: dis](dis-disassembler-for-python-bytecode.md) · [Owning module, declaration or section: dis.Positions](dis-positions-class-to-dis-positions-swap.md) · [Owning module, declaration or section: Python Bytecode Instructions](dis-instruction-class.md)
