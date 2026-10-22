# py_compile — Command-Line Interface

### Command-Line Interface

You can launch this module as a script so as to compile a handful of source files. Whatever files *filenames* lists get compiled and the resulting bytecode gets cached the usual way. This program won't crawl a directory structure to track down source files; it compiles only files named explicitly. The exit status comes out nonzero whenever one of the files couldn't be compiled.

 &lt;file&gt; ... &lt;fileN&gt;

 - Positional arguments are files to compile. Should `-` be the lone parameter, the list of files gets pulled from standard input.

 -q, --quiet

Suppress errors output.

Changed in version 3.2: Added support for `-`.

Changed in version 3.10: Added support for `-q`.

See also

Module [`compileall`](https://docs.python.org/3.14/library/compileall.html#module-compileall)

Utilities to compile all Python source files in a directory tree.

[Subject index](INDEX.md) · [Previous](py-compile-pycinvalidationmode-class.md) · [Continue](../pyclbr/pyclbr-readmodule-to-pyclbr-readmodule-ex.md) · [Owning module, declaration or section: py_compile](py-compile-pycompileerror-to-py-compile-compile.md)
