# ast: `ast.unparse()`, `ast.literal_eval()`, `ast.get_docstring()`, `ast.get_source_segment()`, `ast.fix_missing_locations()`, `ast.increment_lineno()`, `ast.copy_location()`

Assigning a `(major, minor)` tuple to `feature_version` triggers a “best-effort” parse against the grammar of that Python release. Passing `feature_version=(3, 9)`, for instance, tries to reject [`match`](https://docs.python.org/3.14/reference/compound_stmts.html#match) statements while parsing. For now `major` has to be `3`. The floor is `(3, 7)` (a value later Python releases may raise), and the ceiling sits at `sys.version_info[0:2]`. Calling it “best-effort” means nothing promises the parse — or whether it succeeds — matches what you would see running on the genuine Python release that `feature_version` names.

If source contains a null character (`\0`), [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised.

Warning

Bear in mind that getting source code to parse cleanly into an AST object is no assurance the code is executable Python, because compiling it afterward can still throw [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) exceptions. Take the source `return 42`: it yields a perfectly good AST node for a return statement, yet on its own it will not compile (a function node has to enclose it).

Notably, `ast.parse()` performs none of the scoping verification that compilation carries out.

Warning

A string that is big or intricate enough can bring the Python interpreter down, owing to how far the stack may recurse inside Python’s AST compiler.

Changed in version 3.8: Added `type_comments`, `mode='func_type'` and `feature_version`.

Changed in version 3.13: `feature_version` now has `(3, 7)` as its lowest accepted value. The `optimize` argument arrived too.

 ast.unparse(*ast_obj*)

Take an `ast.AST` object and emit a string of code that, fed back through `ast.parse()`, would rebuild an equivalent `ast.AST` object.

Warning

The code string you get back need not match the original code from which the `ast.AST` object came (setting aside any compiler optimizations, constant tuples/frozensets among them).

Warning

Attempting to unparse an extremely intricate expression ends in a [`RecursionError`](https://docs.python.org/3.14/library/exceptions.html#RecursionError).

Added in version 3.9.

 ast.literal_eval(*node_or_string*)

Compute the value of an expression node, or of a string that carries nothing beyond a Python literal or container display. Whatever string or node you supply may be built only from these Python literal forms: strings, bytes, numbers, tuples, lists, dicts, sets, booleans, `None` and `Ellipsis`.

You can lean on this to evaluate strings holding Python values without parsing those values by hand. It cannot handle expressions of unbounded complexity, though — anything bringing in operators or indexing, say, is out of reach.

Earlier documentation branded this function “safe” yet never spelled out the meaning, which was misleading. Its express purpose is to avoid running Python code, in contrast to the broader [`eval()`](https://docs.python.org/3.14/library/functions.html#eval). It offers no namespace, no name lookups, and no way to call outward. Even so, attacks remain possible: a fairly modest input can drain memory or blow out the C stack, taking the process down with it. Certain inputs can likewise trigger a denial of service through runaway CPU use. For these reasons, running it over data you do not trust is inadvisable.

Warning

Because the AST compiler in Python caps how deep its stack can go, the interpreter can be made to crash.

It can raise [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError), [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError), [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError), [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError) and [`RecursionError`](https://docs.python.org/3.14/library/exceptions.html#RecursionError) depending on the malformed input.

Changed in version 3.2: Now allows bytes and set literals.

Changed in version 3.9: Now supports creating empty sets with `'set()'`.

Changed in version 3.10: When the input is a string, any leading spaces and tabs now get removed.

 ast.get_docstring(*node*, *clean=True*)

Hand back the docstring belonging to the supplied *node* (it has to be a `FunctionDef`, `AsyncFunctionDef`, `ClassDef`, or `Module` node), or `None` when none is present. Should *clean* be true, normalize the docstring’s indentation by way of [`inspect.cleandoc()`](https://docs.python.org/3.14/library/inspect.html#inspect.cleandoc).

Changed in version 3.5: `AsyncFunctionDef` is now supported.

 ast.get_source_segment(*source*, *node*, ***, *padded=False*)

Retrieve the slice of the *source* text from which *node* was produced. When any piece of location data (`lineno`, `end_lineno`, `col_offset`, or `end_col_offset`) is absent, hand back `None`.

With *padded* set to `True`, the opening line of a statement spanning several lines gets prefixed with spaces so it lines up where it originally sat.

Added in version 3.8.

 ast.fix_missing_locations(*node*)

Feeding a node tree to [`compile()`](https://docs.python.org/3.14/library/functions.html#compile) makes the compiler look for `lineno` and `col_offset` attributes on every node capable of holding them. Filling those in by hand on generated nodes is tedious, so this helper walks the tree and, wherever they are missing, supplies them by copying the parent node’s values. The walk begins at *node* and descends from there.

 ast.increment_lineno(*node*, *n=1*)

Bump both the line number and the end line number of every node throughout the tree rooted at *node* by *n*. It comes in handy when you want to “move code” somewhere else within a file.

 ast.copy_location(*new_node*, *old_node*)

Where feasible, transfer the source location (`lineno`, `col_offset`, `end_lineno`, and `end_col_offset`) off *old_node* onto *new_node*, then give back *new_node*.

[Subject index](INDEX.md) · [Continue](ast-iter-fields-to-ast-walk.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md) · [Owning module, declaration or section: `ast` helpers](ast-parse.md) · [Owning module, declaration or section: ast.parse](ast-parse.md) · [Preceding source contract and version conditions](ast-parse.md)
