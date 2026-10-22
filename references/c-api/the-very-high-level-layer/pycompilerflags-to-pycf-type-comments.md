# the very high level layer C API: `PyCompilerFlags`, `PyCF_ALLOW_TOP_LEVEL_AWAIT`, `PyCF_ONLY_AST`, `PyCF_OPTIMIZED_AST`, `PyCF_TYPE_COMMENTS`

struct PyCompilerFlags

This is the structure that holds compiler flags. When code is merely being compiled, it travels as `int flags`, and when code is being executed, it travels as `PyCompilerFlags *flags`. In that latter case, `from __future__ import` is able to modify *flags*.

Any time `PyCompilerFlags *flags` is `NULL`, `cf_flags` is taken to be equal to `0`, and whatever modification `from __future__ import` would have made is thrown away.

 int cf_flags

Compiler flags.

 int cf_feature_version

*cf_feature_version* is the minor Python version. It should be initialized to `PY_MINOR_VERSION`.

By default this field gets ignored; it comes into play if and only if the `PyCF_ONLY_AST` flag has been set in `cf_flags`.

Changed in version 3.8: Added *cf_feature_version* field.

The compiler flags that are available can be reached through macros:

 PyCF_ALLOW_TOP_LEVEL_AWAIT

 PyCF_ONLY_AST

 PyCF_OPTIMIZED_AST

 PyCF_TYPE_COMMENTS

Refer to [compiler flags](https://docs.python.org/3.14/library/ast.html#ast-compiler-flags) within the docs for the `ast` Python module; that module re-exports these same constants by the same names.

You can join the "`PyCF`" flags listed above with "`CO_FUTURE`" flags such as [`CO_FUTURE_ANNOTATIONS`](https://docs.python.org/3.14/c-api/code.html#c.CO_FUTURE_ANNOTATIONS) to switch on features that are normally chosen through [future statements](https://docs.python.org/3.14/reference/simple_stmts.html#future). Consult [Code Object Flags](https://docs.python.org/3.14/c-api/code.html#c-codeobject-flags) for the full list.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyrun-anyfile-to-pyrun-interactiveloopflags.md) · [Previous source contract](pyeval-evalcodeex-to-pyeval-mergecompilerflags.md) · [Following source contract](py-eval-input-to-ast-functiontype.md)
