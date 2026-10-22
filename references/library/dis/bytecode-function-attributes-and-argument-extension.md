# dis.Positions: `SET_FUNCTION_ATTRIBUTE()`, `BUILD_SLICE()`, `EXTENDED_ARG()`

PUSH_NULL

Places a `NULL` onto the stack. Used during the call sequence to mirror the `NULL` that `LOAD_METHOD` pushes for non-method calls.

Added in version 3.11.

 MAKE_FUNCTION

Places a new function object onto the stack, built from the code object held at `STACK[-1]`.

Changed in version 3.10: The `0x04` flag value is now a tuple of strings rather than a dictionary

Changed in version 3.11: The qualified name held at `STACK[-1]` was dropped.

Changed in version 3.13: The extra function attributes carried on the stack, indicated through oparg flags, were dropped. `SET_FUNCTION_ATTRIBUTE` now handles them.

 SET_FUNCTION_ATTRIBUTE(*flag*)

Assigns an attribute to a function object. Expects the function at `STACK[-1]` together with the attribute value to assign at `STACK[-2]`; consumes both and leaves the function at `STACK[-1]`. The flag selects which attribute gets set:

- `0x01` a tuple holding, in positional order, the default values for positional-only plus positional-or-keyword parameters

- `0x02` a dictionary holding the default values of keyword-only parameters

- `0x04` a tuple of strings holding the annotations of the parameters

- `0x08` a tuple holding cells for free variables, which forms a closure

- `0x10` the [annotate function](https://docs.python.org/3.14/glossary.html#term-annotate-function) for the function object

Added in version 3.13.

Changed in version 3.14: Introduced `0x10` to mark the annotate function belonging to the function object.

 BUILD_SLICE(*argc*)

Places a slice object onto the stack. *argc* must be 2 or 3. When it is 2, it carries out:

```python
end = STACK.pop()
start = STACK.pop()
STACK.append(slice(start, end))

```

when it is 3, it carries out:

```python
step = STACK.pop()
end = STACK.pop()
start = STACK.pop()
STACK.append(slice(start, end, step))

```

Refer to the [`slice()`](https://docs.python.org/3.14/library/functions.html#slice) built-in function for further detail.

 EXTENDED_ARG(*ext*)

Sits in front of any opcode whose argument is too large to fit within the standard single byte. *ext* supplies an extra byte that serves as higher bits in the argument. Per opcode, no more than three leading `EXTENDED_ARG` are permitted, producing an argument ranging from two bytes to four bytes.

[Subject index](INDEX.md) · [Previous](bytecode-closure-copying-and-function-calls.md) · [Continue](dis-positions-convert-value-to-dis-positions-match-class.md) · [Owning module, declaration or section: dis](dis-disassembler-for-python-bytecode.md) · [Owning module, declaration or section: dis.Positions](dis-positions-class-to-dis-positions-swap.md) · [Owning module, declaration or section: Python Bytecode Instructions](dis-instruction-class.md)
