# dis.Positions: `GET_AWAITABLE()`

DELETE_SUBSCR

Implements:

```python
key = STACK.pop()
container = STACK.pop()
del container[key]

```

 BINARY_SLICE

Implements:

```python
end = STACK.pop()
start = STACK.pop()
container = STACK.pop()
STACK.append(container[start:end])

```

Added in version 3.12.

 STORE_SLICE

Implements:

```python
end = STACK.pop()
start = STACK.pop()
container = STACK.pop()
value = STACK.pop()
container[start:end] = value

```

Added in version 3.12.

**Coroutine opcodes**

 GET_AWAITABLE(*where*)

Carries out `STACK[-1] = get_awaitable(STACK[-1])`; here `get_awaitable(o)` gives back `o` whenever `o` is a coroutine object or else a generator object bearing the [`CO_ITERABLE_COROUTINE`](https://docs.python.org/3.14/library/inspect.html#inspect.CO_ITERABLE_COROUTINE) flag, and otherwise resolves `o.__await__`.

>

If the `where` operand is nonzero, it indicates where the instruction occurs:

- `1`: After a call to `__aenter__`

- `2`: After a call to `__aexit__`

Added in version 3.5.

Changed in version 3.11: This instruction formerly carried no oparg.

 GET_AITER

Implements `STACK[-1] = STACK[-1].__aiter__()`.

Added in version 3.5.

Changed in version 3.7: Handing back awaitable objects out of `__aiter__` is no longer permitted.

 GET_ANEXT

Implement `STACK.append(get_awaitable(STACK[-1].__anext__()))` to the stack. See `GET_AWAITABLE` for details about `get_awaitable`.

Added in version 3.5.

 END_ASYNC_FOR

Brings an [`async for`](https://docs.python.org/3.14/reference/compound_stmts.html#async-for) loop to a close. Deals with an exception thrown while awaiting the next item. On the stack sit the async iterable at `STACK[-2]` and the raised exception at `STACK[-1]`. The two are both popped. Where the exception is not [`StopAsyncIteration`](https://docs.python.org/3.14/library/exceptions.html#StopAsyncIteration), it gets re-raised.

Added in version 3.8.

Changed in version 3.11: The stack's exception representation now holds a single item rather than three.

[Subject index](INDEX.md) · [Previous](dis-positions-binary-op.md) · [Continue](dis-positions-set-add-to-dis-positions-map-add.md) · [Owning module, declaration or section: dis](dis-disassembler-for-python-bytecode.md) · [Owning module, declaration or section: dis.Positions](dis-positions-class-to-dis-positions-swap.md) · [Owning module, declaration or section: Python Bytecode Instructions](dis-instruction-class.md)
