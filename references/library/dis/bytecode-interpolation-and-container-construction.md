# dis.Positions: `BUILD_INTERPOLATION()`, `BUILD_TUPLE()`, `BUILD_LIST()`, `BUILD_SET()`, `BUILD_MAP()`, `BUILD_STRING()`, `LIST_EXTEND()`

BUILD_INTERPOLATION(*format*)

Builds a fresh [`Interpolation`](https://docs.python.org/3.14/library/string.templatelib.html#string.templatelib.Interpolation) instance out of a value together with its source expression, then places the produced object onto the stack.

When neither a conversion nor a format specification is given, `format` becomes `2`.

When the low bit of `format` is set, that signals the interpolation carries a format specification.

When `format >> 2` is non-zero, that signals the interpolation carries a conversion. The `format >> 2` value identifies the conversion type (`0` for no conversion, `1` for `!s`, `2` for `!r`, and `3` for `!a`):

```python
conversion = format >> 2
if format & 1:
    format_spec = STACK.pop()
else:
    format_spec = None
expression = STACK.pop()
value = STACK.pop()
STACK.append(_build_interpolation(value, expression, conversion, format_spec))

```

Added in version 3.14.

 BUILD_TUPLE(*count*)

Builds a tuple by taking *count* items from the stack, then places the produced tuple onto the stack:

```python
if count == 0:
    value = ()
else:
    value = tuple(STACK[-count:])
    STACK = STACK[:-count]

STACK.append(value)

```

 BUILD_LIST(*count*)

Behaves like `BUILD_TUPLE`, except it builds a list.

 BUILD_SET(*count*)

Behaves like `BUILD_TUPLE`, except it builds a set.

 BUILD_MAP(*count*)

Places a fresh dictionary object onto the stack. Removes `2 * count` items such that the dictionary contains *count* entries: `{..., STACK[-4]: STACK[-3], STACK[-2]: STACK[-1]}`.

Changed in version 3.5: The dictionary is now built directly from stack items rather than first making an empty dictionary pre-sized for *count* items.

 BUILD_STRING(*count*)

Joins *count* strings taken from the stack and places the produced string onto the stack.

Added in version 3.6.

 LIST_EXTEND(*i*)

Carries out:

```python
seq = STACK.pop()
list.extend(STACK[-i], seq)

```

Applied when building lists.

Added in version 3.9.

[Subject index](INDEX.md) · [Previous](bytecode-unpacking-and-name-lookup.md) · [Continue](dis-positions-set-update-to-dis-positions-is-op.md) · [Owning module, declaration or section: dis](dis-disassembler-for-python-bytecode.md) · [Owning module, declaration or section: dis.Positions](dis-positions-class-to-dis-positions-swap.md) · [Owning module, declaration or section: Python Bytecode Instructions](dis-instruction-class.md)
