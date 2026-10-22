# dis.Positions: `CONVERT_VALUE()`, `MATCH_CLASS()`

CONVERT_VALUE(*oparg*)

Turns value into a string, according to `oparg`:

```python
value = STACK.pop()
result = func(value)
STACK.append(result)

```

- `oparg == 1`: call [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) on *value*

- `oparg == 2`: call [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) on *value*

- `oparg == 3`: call [`ascii()`](https://docs.python.org/3.14/library/functions.html#ascii) on *value*

Used to implement formatted string literals (f-strings).

Added in version 3.13.

 FORMAT_SIMPLE

Formats the value sitting on top of the stack:

```python
value = STACK.pop()
result = value.__format__("")
STACK.append(result)

```

Used to implement formatted string literals (f-strings).

Added in version 3.13.

 FORMAT_WITH_SPEC

Formats the supplied value using the supplied format spec:

```python
spec = STACK.pop()
value = STACK.pop()
result = value.__format__(spec)
STACK.append(result)

```

Used to implement formatted string literals (f-strings).

Added in version 3.13.

 MATCH_CLASS(*count*)

[Subject index](INDEX.md) · [Previous](bytecode-function-attributes-and-argument-extension.md) · [Owning module, declaration or section: dis](dis-disassembler-for-python-bytecode.md) · [Owning module, declaration or section: dis.Positions](dis-positions-class-to-dis-positions-swap.md) · [Owning module, declaration or section: Python Bytecode Instructions](dis-instruction-class.md) · [Required continuation of the source contract](match-class-bytecode-instruction.md)
