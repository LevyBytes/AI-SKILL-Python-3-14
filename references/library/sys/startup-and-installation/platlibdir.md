# sys.platlibdir

sys.platlibdir

Name of the platform-specific library directory. It serves to assemble the path of the standard library and the paths of installed extension modules.

On most platforms it equals `"lib"`. On Fedora and SuSE it equals `"lib64"` on 64-bit platforms, which produces the following `sys.path` paths (where `X.Y` stands for the Python `major.minor` version):

- `/usr/lib64/pythonX.Y/`: Standard library (such as `os.py` belonging to the [`os`](https://docs.python.org/3.14/library/os.html#module-os) module)

- `/usr/lib64/pythonX.Y/lib-dynload/`: C extension modules belonging to the standard library (such as the [`errno`](https://docs.python.org/3.14/library/errno.html#module-errno) module, whose precise filename depends on the platform)

- `/usr/lib/pythonX.Y/site-packages/` (always reach for `lib`, not `sys.platlibdir`): Third-party modules

- `/usr/lib64/pythonX.Y/site-packages/`: C extension modules belonging to third-party packages

Added in version 3.9.

[API family](INDEX.md) · [sys context index](../INDEX.md).
