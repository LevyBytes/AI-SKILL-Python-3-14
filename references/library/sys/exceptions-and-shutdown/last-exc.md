# sys.last_exc

sys.last_exc

This variable does not always have a value; it receives the exception instance whenever an exception goes unhandled and the interpreter emits an error message together with a stack traceback. The reason it exists is to let an interactive user pull in a debugger module and perform post-mortem debugging without needing to rerun the command that triggered the error. (A common pattern is `import pdb; pdb.pm()` to launch the post-mortem debugger; consult the [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) module for further details.)

Added in version 3.12.

[API family](INDEX.md) · [sys context index](../INDEX.md).
