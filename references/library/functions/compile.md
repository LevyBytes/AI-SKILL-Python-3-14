# compile

compile(*source*, *filename*, *mode*, *flags=0*, *dont_inherit=False*, *optimize=-1*)

Turn the *source* into a code object or AST object. The `exec()` or `eval()` functions can run code objects. *source* may be a regular string, a byte string, or an AST object. Look to the [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast) module documentation to learn how to handle AST objects.

The *filename* argument is meant to name the file the code was read from; when it did not come from a file, pass any recognizable value (`'<string>'` sees frequent use).

The *mode* argument states which kind of code is to be compiled; use `'exec'` when *source* is a series of statements, `'eval'` when it is one expression, or `'single'` when it is one interactive statement (in this last case, expression statements evaluating to anything besides `None` will be printed).

The optional arguments *flags* and *dont_inherit* govern which [compiler options](https://docs.python.org/3.14/library/ast.html#ast-compiler-flags) get switched on and which [future features](https://docs.python.org/3.14/reference/simple_stmts.html#future) get permitted. When neither appears (or both are zero), the code compiles under the same flags that govern the code calling `compile()`. When *flags* is supplied but *dont_inherit* is not (or is zero), then the compiler options and future statements named by *flags* join those that would apply regardless. When *dont_inherit* is a non-zero integer, *flags* stands alone – the flags (future features and compiler options) of the surrounding code get disregarded.

You name compiler options and future statements through bits that can be bitwise ORed together to combine several options. The bitfield naming a particular future feature is available as the [`compiler_flag`](https://docs.python.org/3.14/library/__future__.html#future__._Feature.compiler_flag) attribute on the [`_Feature`](https://docs.python.org/3.14/library/__future__.html#future__._Feature) instance within the [`__future__`](https://docs.python.org/3.14/library/__future__.html#module-__future__) module. The [Compiler flags](https://docs.python.org/3.14/library/ast.html#ast-compiler-flags) live in the [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast) module, carrying the `PyCF_` prefix.

The *optimize* argument sets the compiler’s optimization level; its default of `-1` picks the interpreter’s own optimization level, as dictated by the [`-O`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-O) options. The explicit levels are `0` (no optimization; `__debug__` is true), `1` (asserts dropped, `__debug__` is false) or `2` (docstrings dropped as well).

Should the source being compiled be invalid, this function raises [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) or [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

To parse Python code into its AST form, consult [`ast.parse()`](https://docs.python.org/3.14/library/ast.html#ast.parse).

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `compile` carrying the `source` and `filename` arguments. Implicit compilation can trigger that same event too.

Note

Multi-line code being compiled as a string under `'single'` or `'eval'` mode has to close with at least one newline character. That requirement helps the [`code`](https://docs.python.org/3.14/library/code.html#module-code) module tell complete statements apart from incomplete ones.

Warning

A string that is large or complex enough can crash the Python interpreter while it compiles to an AST object, because Python’s AST compiler has stack depth limits.

Changed in version 3.2: Windows and Mac newlines became acceptable. On top of that, `'exec'` mode input is no longer obliged to finish with a newline. The *optimize* parameter was introduced.

Changed in version 3.5: Earlier on, encountering null bytes in *source* would trigger [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

Added in version 3.8: Passing `ast.PyCF_ALLOW_TOP_LEVEL_AWAIT` in flags is now possible, switching on support for top-level `await`, `async for`, and `async with`.

[Builtin task index](INDEX.md).
