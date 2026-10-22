# dis.Positions: `UNPACK_EX()`, `STORE_ATTR()`, `DELETE_ATTR()`, `STORE_GLOBAL()`, `DELETE_GLOBAL()`, `LOAD_CONST()`, `LOAD_SMALL_INT()`, `LOAD_NAME()`, `LOAD_FROM_DICT_OR_GLOBALS()`

UNPACK_EX(*counts*)

Carries out assignment to a starred target: it splits an iterable held in `STACK[-1]` into separate values, where the count of values may be fewer than the iterable's item count: one of the resulting values becomes a list gathering all the remaining items.

Both the count of values before and the count after the list value cannot exceed 255.

The count of values preceding the list value is held in the opcode's argument. Any count of values following the list is held via an `EXTENDED_ARG`. Because of this, the argument can be regarded as a two-byte value in which the low byte of *counts* gives the count of values before the list value, and the high byte of *counts* gives the count after it.

The pulled-apart values are placed onto the stack in reverse order, that is, `a, *b, c = d` will, once run, end up stored as `STACK.extend((a, b, c))`.

 STORE_ATTR(*namei*)

Carries out:

```python
obj = STACK.pop()
value = STACK.pop()
obj.name = value

```

where *namei* gives the position of name within [`co_names`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_names) of the [code object](https://docs.python.org/3.14/reference/datamodel.html#code-objects).

 DELETE_ATTR(*namei*)

Carries out:

```python
obj = STACK.pop()
del obj.name

```

where *namei* gives the position of name in [`co_names`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_names) of the [code object](https://docs.python.org/3.14/reference/datamodel.html#code-objects).

 STORE_GLOBAL(*namei*)

Behaves like `STORE_NAME`, except the name is stored as a global.

 DELETE_GLOBAL(*namei*)

Behaves like `DELETE_NAME`, except a global name is deleted.

 LOAD_CONST(*consti*)

Places `co_consts[consti]` onto the stack.

 LOAD_SMALL_INT(*i*)

Places the integer `i` onto the stack. `i` must be in `range(256)`

Added in version 3.14.

 LOAD_NAME(*namei*)

Places the value tied to `co_names[namei]` onto the stack. The lookup for the name proceeds through the locals, then the globals, then the builtins.

 LOAD_LOCALS

Places a reference to the locals dictionary onto the stack. This serves to set up namespace dictionaries for `LOAD_FROM_DICT_OR_DEREF` and `LOAD_FROM_DICT_OR_GLOBALS`.

Added in version 3.12.

 LOAD_FROM_DICT_OR_GLOBALS(*i*)

Removes a mapping from the stack and resolves the value for `co_names[namei]`. Should the name be absent there, it is resolved through the globals and then the builtins, much like `LOAD_GLOBAL`. This serves to load global variables in [annotation scopes](https://docs.python.org/3.14/reference/executionmodel.html#annotation-scopes) inside class bodies.

Added in version 3.12.

 BUILD_TEMPLATE

Builds a fresh [`Template`](https://docs.python.org/3.14/library/string.templatelib.html#string.templatelib.Template) instance out of a tuple of strings together with a tuple of interpolations, then places the produced object onto the stack:

```python
interpolations = STACK.pop()
strings = STACK.pop()
STACK.append(_build_template(strings, interpolations))

```

Added in version 3.14.

[Subject index](INDEX.md) · [Previous](dis-positions-store-name-to-dis-positions-unpack-sequence.md) · [Continue](bytecode-interpolation-and-container-construction.md) · [Owning module, declaration or section: dis](dis-disassembler-for-python-bytecode.md) · [Owning module, declaration or section: dis.Positions](dis-positions-class-to-dis-positions-swap.md) · [Owning module, declaration or section: Python Bytecode Instructions](dis-instruction-class.md)
