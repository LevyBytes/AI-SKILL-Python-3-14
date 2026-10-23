# os - Files and Directories - Contract: Even though Windows supports `chmod()`, the only thing you can change there is the file's read-only flag (through the `stat.S_IWRITE` and `stat.S_IREAD` constants or an equivalent integer value).

Even though Windows supports `chmod()`, the only thing you can change there is the file's read-only flag (through the `stat.S_IWRITE` and `stat.S_IREAD` constants or an equivalent integer value). Every other bit is disregarded. On Windows the default value of *follow_symlinks* is `False`.

This function is restricted on WASI; consult [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability) for further detail.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.chmod` with arguments `path`, `mode`, `dir_fd`.

Changed in version 3.3: Added the ability to give *path* as an open file descriptor, along with the *dir_fd* and *follow_symlinks* arguments.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Changed in version 3.13: On Windows, a file descriptor plus the *follow_symlinks* argument are now supported.

[Subject index](INDEX.md) · [Previous](os-chmod-to-stat-s-ixoth.md) · [Continue](os-chown-to-os-lchown.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Files and Directories](os-access.md) · [Owning module, declaration or section: os.chmod](os-chmod-to-stat-s-ixoth.md)
