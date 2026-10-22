# dis.Positions: `SET_UPDATE()`, `DICT_UPDATE()`, `DICT_MERGE()`, `LOAD_ATTR()`, `LOAD_SUPER_ATTR()`, `COMPARE_OP()`, `IS_OP()`

SET_UPDATE(*i*)

Carries out:

```python
seq = STACK.pop()
set.update(STACK[-i], seq)

```

Applied when building sets.

Added in version 3.9.

 DICT_UPDATE(*i*)

Carries out:

```python
map = STACK.pop()
dict.update(STACK[-i], map)

```

Applied when building dicts.

Added in version 3.9.

 DICT_MERGE(*i*)

Behaves like `DICT_UPDATE`, but throws an exception when keys are duplicated.

Added in version 3.9.

 LOAD_ATTR(*namei*)

When the low bit of `namei` is unset, this swaps `STACK[-1]` for `getattr(STACK[-1], co_names[namei>>1])`.

When the low bit of `namei` is set, it tries to load a method called `co_names[namei>>1]` from the `STACK[-1]` object. `STACK[-1]` is popped. The bytecode separates two situations: when `STACK[-1]` owns a method bearing the right name, the bytecode pushes the unbound method together with `STACK[-1]`. That `STACK[-1]` then becomes the first argument (`self`) used by `CALL` or `CALL_KW` while invoking the unbound method. If not, `NULL` along with the object that the attribute lookup returned are pushed.

Changed in version 3.12: When the low bit of `namei` is set, a `NULL` or `self` gets pushed onto the stack ahead of the attribute or unbound method, respectively.

 LOAD_SUPER_ATTR(*namei*)

This opcode provides [`super()`](https://docs.python.org/3.14/library/functions.html#super), covering both its zero-argument and two-argument forms (for instance `super().method()`, `super().attr` and `super(cls, self).method()`, `super(cls, self).attr`).

It removes three values from the stack (going from the top downward):

- `self`: the first argument passed to the current method

- `cls`: the class in which the current method was defined

- the global `super`

Regarding its argument, it operates much like `LOAD_ATTR`, with the difference that `namei` is shifted left by 2 bits rather than 1.

The low bit of `namei` indicates that a method load should be attempted, just as with `LOAD_ATTR`, which leads to pushing `NULL` plus the loaded method. When that bit is clear, only one value is pushed onto the stack.

The second-low bit of `namei`, when set, indicates this was a two-argument call to [`super()`](https://docs.python.org/3.14/library/functions.html#super) (clear meaning zero-argument).

Added in version 3.12.

 COMPARE_OP(*opname*)

Carries out a Boolean operation. You can find the operation name at `cmp_op[opname >> 5]`. When the fifth-lowest bit of `opname` is set (`opname & 16`), the outcome ought to be coerced to `bool`.

Changed in version 3.13: A forced conversion to [`bool`](https://docs.python.org/3.14/library/functions.html#bool) is now signaled by the oparg's fifth-lowest bit.

 IS_OP(*invert*)

Carries out an `is` comparison, or `is not` when `invert` is 1.

Added in version 3.9.

[Subject index](INDEX.md) · [Previous](bytecode-interpolation-and-container-construction.md) · [Continue](dis-positions-contains-op-to-dis-positions-load-fast.md) · [Owning module, declaration or section: dis](dis-disassembler-for-python-bytecode.md) · [Owning module, declaration or section: dis.Positions](dis-positions-class-to-dis-positions-swap.md) · [Owning module, declaration or section: Python Bytecode Instructions](dis-instruction-class.md)
