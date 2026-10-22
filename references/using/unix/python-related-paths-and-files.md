# 2.3. Python-related paths and files

### 2.3. Python-related paths and files

These can vary according to whatever local install conventions are in force; [`prefix`](https://docs.python.org/3.14/using/configure.html#cmdoption-prefix) and [`exec_prefix`](https://docs.python.org/3.14/using/configure.html#cmdoption-exec-prefix) hinge on the installation and carry the same meaning they do for GNU software, and the two might coincide.

To take one case, the default for each on the bulk of Linux systems is `/usr`.

| File/directory | Meaning |
| --- | --- |
| `*exec_prefix*/bin/python3` | Where the interpreter is meant to live. |
| `*prefix*/lib/python*version*`, `*exec_prefix*/lib/python*version*` | Where the folders holding the standard modules are meant to live. |
| `*prefix*/include/python*version*`, `*exec_prefix*/include/python*version*` | Where the folders holding the header files are meant to live, the ones you need when building Python extensions or embedding the interpreter. |

[Subject index](INDEX.md) · [Previous source section](building-python.md) · [Following source section](miscellaneous.md)
