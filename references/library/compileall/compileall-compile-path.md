# compileall: `compileall.compile_path()`

`compileall.compile_path(*skip_curdir=True*, *maxlevels=0*, *force=False*, *quiet=0*, *legacy=False*, *optimize=-1*, *invalidation_mode=None*)`

Byte-compile every `.py` file discovered along `sys.path`. Hand back a true value when all of them compiled cleanly, and a false value otherwise.

A true *skip_curdir* (the default) keeps the current directory out of the search. Every remaining parameter is forwarded to the `compile_dir()` function. Be aware that, in contrast to the other compile functions, `maxlevels` here defaults to `0`.

Changed in version 3.2: Added the *legacy* and *optimize* parameter.

Changed in version 3.5: The *quiet* parameter gained multilevel behavior.

Changed in version 3.5: Whatever value *optimize* holds, the *legacy* parameter writes out nothing but `.pyc` files, leaving `.pyo` files aside.

Changed in version 3.7: The *invalidation_mode* parameter was added.

Changed in version 3.7.2: The default of the *invalidation_mode* parameter was changed to `None`.

To compel a fresh compile of every `.py` file inside the `Lib/` subdirectory together with all of its descendants:

```python
import compileall

compileall.compile_dir('Lib/', force=True)

# Perform same compilation, excluding files in .svn directories.
import re
compileall.compile_dir('Lib/', rx=re.compile(r'[/\\][.]svn'), force=True)

# pathlib.Path objects can also be used.
import pathlib
compileall.compile_dir(pathlib.Path('Lib/'), force=True)

```

See also

Module [`py_compile`](https://docs.python.org/3.14/library/py_compile.html#module-py_compile)

Byte-compiles one source file on its own.

[Subject index](INDEX.md) · [Previous](compileall-compile-dir-to-compileall-compile-file.md) · [Continue](../compression/the-compression-package.md) · [Owning module, declaration or section: compileall](compileall-byte-compile-python-libraries.md) · [Owning module, declaration or section: Public functions](compileall-compile-dir-to-compileall-compile-file.md)
