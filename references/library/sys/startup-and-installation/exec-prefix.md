# sys.exec_prefix

sys.exec_prefix

A string naming the site-specific directory prefix where the platform-dependent Python files live; by default this too is `'/usr/local'`. It can be fixed at build time through the `--exec-prefix` argument to the **configure** script. To be precise, all configuration files (the `pyconfig.h` header file, for example) get installed under the directory `*exec_prefix*/lib/python*X.Y*/config`, and shared library modules go under `*exec_prefix*/lib/python*X.Y*/lib-dynload`, where *X.Y* is Python's version number, say `3.2`.

Note

Where a [virtual environment](https://docs.python.org/3.14/library/venv.html#venv-def) is active, this `exec_prefix` will refer to the virtual environment. The value belonging to the Python installation remains reachable through `base_exec_prefix`. See [Virtual Environments](https://docs.python.org/3.14/library/sys_path_init.html#sys-path-init-virtual-environments) for further details.

Changed in version 3.14: While running inside a [virtual environment](https://docs.python.org/3.14/library/venv.html#venv-def), it is now the [path initialization](https://docs.python.org/3.14/library/sys_path_init.html#sys-path-init) — rather than [`site`](https://docs.python.org/3.14/library/site.html#module-site) — that assigns the virtual environment prefix to `prefix` and `exec_prefix`. As a result, `prefix` and `exec_prefix` keep pointing at the virtual environment even with `site` turned off ([`-S`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-S)).

[API family](INDEX.md) · [sys context index](../INDEX.md).
