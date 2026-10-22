# dis / Python Bytecode Instructions: `dis.Positions`, `COPY()`, `SWAP()`

*class *dis.Positions

In case the information is not available, some fields might be `None`.

 lineno

 end_lineno

 col_offset

 end_col_offset

Added in version 3.11.

The Python compiler currently generates the following bytecode instructions.

**General instructions**

Throughout what follows, We will call the interpreter stack `STACK` and portray operations against it as though it were a Python list. In this notation the stack's top maps to `STACK[-1]`.

 NOP

A do-nothing code. The bytecode optimizer leans on it as a placeholder, and it also produces line tracing events.

 NOT_TAKEN

A do-nothing code. Used by the interpreter to record [`BRANCH_LEFT`](https://docs.python.org/3.14/library/sys.monitoring.html#monitoring-event-BRANCH_LEFT) and [`BRANCH_RIGHT`](https://docs.python.org/3.14/library/sys.monitoring.html#monitoring-event-BRANCH_RIGHT) events for [`sys.monitoring`](https://docs.python.org/3.14/library/sys.monitoring.html#module-sys.monitoring).

Added in version 3.14.

 POP_ITER

Removes the iterator from the top of the stack.

Added in version 3.14.

 POP_TOP

Removes the top-of-stack item:

```python
STACK.pop()

```

 END_FOR

Drops the top-of-stack item. The same as `POP_TOP`. Employed for cleanup once a loop finishes, which is where its name comes from.

Added in version 3.12.

 END_SEND

Implements `del STACK[-2]`. Used to clean up when a generator exits.

Added in version 3.12.

 COPY(*i*)

Copy the i-th item up to the stack's top while leaving the original where it sits:

```python
assert i > 0
STACK.append(STACK[-i])

```

Added in version 3.11.

 SWAP(*i*)

Swap the top of the stack with the i-th element:

```python
STACK[-i], STACK[-1] = STACK[-1], STACK[-i]

```

Added in version 3.11.

[Subject index](INDEX.md) · [Previous](python-bytecode-instructions.md) · [Continue](dis-positions-binary-op.md) · [Owning module, declaration or section: dis](dis-disassembler-for-python-bytecode.md) · [Owning module, declaration or section: Python Bytecode Instructions](dis-instruction-class.md)
