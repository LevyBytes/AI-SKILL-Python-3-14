# dis.Positions: Local-variable, cell and closure bytecodes

LOAD_FAST_BORROW(*var_num*)

Places a borrowed reference to the local `co_varnames[var_num]` onto the stack.

Added in version 3.14.

 LOAD_FAST_LOAD_FAST(*var_nums*)

Places references to `co_varnames[var_nums >> 4]` and `co_varnames[var_nums & 15]` onto the stack.

Added in version 3.13.

 LOAD_FAST_BORROW_LOAD_FAST_BORROW(*var_nums*)

Places borrowed references to `co_varnames[var_nums >> 4]` and `co_varnames[var_nums & 15]` onto the stack.

Added in version 3.14.

 LOAD_FAST_CHECK(*var_num*)

Places a reference to the local `co_varnames[var_num]` onto the stack, raising an [`UnboundLocalError`](https://docs.python.org/3.14/library/exceptions.html#UnboundLocalError) when the local variable has not yet been initialized.

Added in version 3.12.

 LOAD_FAST_AND_CLEAR(*var_num*)

Places a reference to the local `co_varnames[var_num]` onto the stack (or places `NULL` onto the stack when the local variable has not been initialized) and resets `co_varnames[var_num]` to `NULL`.

Added in version 3.12.

 STORE_FAST(*var_num*)

Saves `STACK.pop()` into the local `co_varnames[var_num]`.

 STORE_FAST_STORE_FAST(*var_nums*)

Saves `STACK[-1]` into `co_varnames[var_nums >> 4]` and `STACK[-2]` into `co_varnames[var_nums & 15]`.

Added in version 3.13.

 STORE_FAST_LOAD_FAST(*var_nums*)

Saves `STACK.pop()` into the local `co_varnames[var_nums >> 4]` and places a reference to the local `co_varnames[var_nums & 15]` onto the stack.

Added in version 3.13.

 DELETE_FAST(*var_num*)

Removes local `co_varnames[var_num]`.

 MAKE_CELL(*i*)

Builds a new cell in slot `i`. Should that slot already hold a value, that value is saved into the new cell.

Added in version 3.11.

 LOAD_DEREF(*i*)

Loads the cell held in slot `i` of the ?fast locals? storage. Places a reference to the object inside the cell onto the stack.

Changed in version 3.11: The length of [`co_varnames`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_varnames) no longer offsets `i`.

 LOAD_FROM_DICT_OR_DEREF(*i*)

Removes a mapping from the stack and resolves, within that mapping, the name tied to slot `i` of the ?fast locals? storage. Should the name be absent there, it is loaded from the cell held in slot `i`, much like `LOAD_DEREF`. This serves to load [closure variables](https://docs.python.org/3.14/glossary.html#term-closure-variable) in class bodies (which formerly used `LOAD_CLASSDEREF`) and in [annotation scopes](https://docs.python.org/3.14/reference/executionmodel.html#annotation-scopes) inside class bodies.

Added in version 3.12.

 STORE_DEREF(*i*)

Saves `STACK.pop()` into the cell held in slot `i` of the ?fast locals? storage.

Changed in version 3.11: The length of [`co_varnames`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_varnames) no longer offsets `i`.

 DELETE_DEREF(*i*)

Clears the cell held in slot `i` of the ?fast locals? storage. Used by the [`del`](https://docs.python.org/3.14/reference/simple_stmts.html#del) statement.

Added in version 3.2.

Changed in version 3.11: The length of [`co_varnames`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_varnames) no longer offsets `i`.

[Subject index](INDEX.md) · [Previous](dis-positions-contains-op-to-dis-positions-load-fast.md) · [Continue](bytecode-closure-copying-and-function-calls.md) · [Owning module, declaration or section: dis](dis-disassembler-for-python-bytecode.md) · [Owning module, declaration or section: dis.Positions](dis-positions-class-to-dis-positions-swap.md) · [Owning module, declaration or section: Python Bytecode Instructions](dis-instruction-class.md)
