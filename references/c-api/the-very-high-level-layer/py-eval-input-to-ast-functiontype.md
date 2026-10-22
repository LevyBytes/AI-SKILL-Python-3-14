# Available start symbols

### Available start symbols

 int Py_eval_input

The Python grammar's start symbol for standalone expressions; intended for use alongside `Py_CompileString()`.

 int Py_file_input

The Python grammar's start symbol for runs of statements taken from a file or another source; intended for use alongside `Py_CompileString()`. Reach for this symbol when compiling Python source code of arbitrary length.

 int Py_single_input

The Python grammar's start symbol for an individual statement; intended for use alongside `Py_CompileString()`. This is the symbol the interactive interpreter loop relies on.

 int Py_func_type_input

The Python grammar's start symbol for a function type; intended for use alongside `Py_CompileString()`. It serves to parse "signature type comments" from [**PEP 484**](https://peps.python.org/pep-0484/).

Using this requires that the `PyCF_ONLY_AST` flag be set.

See also

- [`ast.FunctionType`](https://docs.python.org/3.14/library/ast.html#ast.FunctionType)

- [**PEP 484**](https://peps.python.org/pep-0484/)

Added in version 3.8.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyrun-anyfile-to-pyrun-interactiveloopflags.md) · [Previous source contract](pycompilerflags-to-pycf-type-comments.md) · [Following source contract](dis-stack-effect-to-pycompile-opcodestackeffectwithjump.md)
