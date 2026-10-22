# sys.prefix

sys.prefix

A string holding the site-specific directory prefix at which the platform independent Python files are installed; on Unix the default is `/usr/local`. You can set it at build time with the [`--prefix`](https://docs.python.org/3.14/using/configure.html#cmdoption-prefix) argument to the **configure** script. Consult [Installation paths](https://docs.python.org/3.14/library/sysconfig.html#installation-paths) for derived paths.

Note

When a [virtual environment](https://docs.python.org/3.14/library/venv.html#venv-def) is active, this `prefix` will point at the virtual environment. The value for the Python installation remains reachable through `base_prefix`. Refer to [Virtual Environments](https://docs.python.org/3.14/library/sys_path_init.html#sys-path-init-virtual-environments) for more information.

Changed in version 3.14: While running inside a [virtual environment](https://docs.python.org/3.14/library/venv.html#venv-def), `prefix` and `exec_prefix` are now assigned the virtual environment prefix by the [path initialization](https://docs.python.org/3.14/library/sys_path_init.html#sys-path-init), rather than by [`site`](https://docs.python.org/3.14/library/site.html#module-site). The upshot is that `prefix` and `exec_prefix` always point at the virtual environment, even with `site` disabled ([`-S`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-S)).

[API family](INDEX.md) · [sys context index](../INDEX.md).
