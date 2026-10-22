# sys.base_exec_prefix

sys.base_exec_prefix

The same as `exec_prefix`, except that it refers to the base Python installation.

While a program runs inside [Virtual Environments](https://docs.python.org/3.14/library/sys_path_init.html#sys-path-init-virtual-environments), `exec_prefix` is reassigned to the virtual environment prefix. `base_exec_prefix`, by contrast, holds steady and keeps pointing at the base Python installation. See [Virtual Environments](https://docs.python.org/3.14/library/sys_path_init.html#sys-path-init-virtual-environments) for further details.

Added in version 3.3.

[API family](INDEX.md) · [sys context index](../INDEX.md).
