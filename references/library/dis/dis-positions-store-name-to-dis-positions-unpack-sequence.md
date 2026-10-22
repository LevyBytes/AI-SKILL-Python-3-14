# dis.Positions: `STORE_NAME()`, `DELETE_NAME()`, `UNPACK_SEQUENCE()`

CHECK_EXC_MATCH

Carries out exception matching for `except`. Checks whether `STACK[-2]` is an exception that matches `STACK[-1]`. Removes `STACK[-1]` and places the boolean outcome of the check onto the stack.

Added in version 3.11.

 CHECK_EG_MATCH

Carries out exception matching for `except*`. Runs `split(STACK[-1])` against the exception group that `STACK[-2]` represents.

When there is a match, two items are popped from the stack and the non-matching subgroup is pushed (`None` if the match was complete), followed by the matching subgroup. If nothing matches, a single item (the match type) is popped and `None` is pushed.

Added in version 3.11.

 WITH_EXCEPT_START

Invokes the function sitting at position 4 on the stack, passing arguments (type, val, tb) that describe the exception at the top of the stack. This serves to carry out the call `context_manager.__exit__(*exc_info())` after an exception is raised inside a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement.

Added in version 3.9.

Changed in version 3.11: The `__exit__` function now sits at position 4 of the stack rather than 7. The stack's exception representation is now a single item instead of three.

 LOAD_COMMON_CONSTANT

Places a common constant on the stack. A fixed list of constants that this instruction supports is built into the interpreter. The [`assert`](https://docs.python.org/3.14/reference/simple_stmts.html#assert) statement relies on it to load [`AssertionError`](https://docs.python.org/3.14/library/exceptions.html#AssertionError).

Added in version 3.14.

 LOAD_BUILD_CLASS

Places `builtins.__build_class__()` onto the stack. A subsequent call uses it to build a class.

 GET_LEN

Carries out `STACK.append(len(STACK[-1]))`. Applied within [`match`](https://docs.python.org/3.14/reference/compound_stmts.html#match) statements that need a comparison against the pattern's structure.

Added in version 3.10.

 MATCH_MAPPING

When `STACK[-1]` is an instance of [`collections.abc.Mapping`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Mapping) (more precisely: when the [`Py_TPFLAGS_MAPPING`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_MAPPING) flag is set in its [`tp_flags`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_flags)), push `True` onto the stack. If not, push `False`.

Added in version 3.10.

 MATCH_SEQUENCE

When `STACK[-1]` is an instance of [`collections.abc.Sequence`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Sequence) yet is *not* an instance of [`str`](https://docs.python.org/3.14/library/stdtypes.html#str)/[`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes)/[`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) (more precisely: when the [`Py_TPFLAGS_SEQUENCE`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_SEQUENCE) flag is set in its [`tp_flags`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_flags)), push `True` onto the stack. If not, push `False`.

Added in version 3.10.

 MATCH_KEYS

Here `STACK[-1]` holds a tuple of mapping keys, while `STACK[-2]` is the subject being matched. When `STACK[-2]` includes every key found in `STACK[-1]`, push a [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple) holding the matching values. If not, push `None`.

Added in version 3.10.

Changed in version 3.11: Earlier, this instruction additionally pushed a boolean signaling success (`True`) or failure (`False`).

 STORE_NAME(*namei*)

Carries out `name = STACK.pop()`. Here *namei* is the position of *name* in the [`co_names`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_names) attribute of the [code object](https://docs.python.org/3.14/reference/datamodel.html#code-objects). When feasible, the compiler prefers `STORE_FAST` or `STORE_GLOBAL`.

 DELETE_NAME(*namei*)

Carries out `del name`, with *namei* being the position within the [`co_names`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_names) attribute of the [code object](https://docs.python.org/3.14/reference/datamodel.html#code-objects).

 UNPACK_SEQUENCE(*count*)

Splits `STACK[-1]` into *count* separate values, which are placed onto the stack in reverse order. There must be precisely *count* values present.:

```python
assert(len(STACK[-1]) == count)
STACK.extend(STACK.pop()[:-count-1:-1])

```

[Subject index](INDEX.md) · [Previous](python-bytecode-instructions.md) · [Continue](bytecode-unpacking-and-name-lookup.md) · [Owning module, declaration or section: dis](dis-disassembler-for-python-bytecode.md) · [Owning module, declaration or section: dis.Positions](dis-positions-class-to-dis-positions-swap.md) · [Owning module, declaration or section: Python Bytecode Instructions](dis-instruction-class.md)
