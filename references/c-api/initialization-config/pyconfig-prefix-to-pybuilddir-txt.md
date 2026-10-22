# PyConfig.prefix

`PyConfig.prefix`

Should even one “output field” go unset, Python works out the path configuration so as to populate whatever fields remain empty. When `module_search_paths_set` equals `0`, `module_search_paths` is replaced and `module_search_paths_set` becomes `1`.

You can sidestep the routine that derives the default path configuration entirely by assigning every path-configuration output field named above by hand. A string counts as set so long as it is non-empty, and `module_search_paths` counts as set once `module_search_paths_set` equals `1`; in that situation `module_search_paths` is taken as-is, unaltered.

Assign `pathconfig_warnings` a value of `0` to mute warnings during path-configuration computation (this is Unix-only, since Windows emits no such warning).

When the `base_prefix` or `base_exec_prefix` fields go unset, each one picks up its value from `prefix` and `exec_prefix` in turn.

[`Py_RunMain()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_RunMain) along with [`Py_Main()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Main) make changes to [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path):

- When `run_filename` is set and points at a directory holding a `__main__.py` script, put `run_filename` at the front of [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path).

- When `isolated` is zero:

  - When `run_module` is set, put the current directory at the front of [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path); if that directory cannot be read, leave things alone.

  - When `run_filename` is set, put the directory containing the filename at the front of [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path).

  - Failing those, put an empty string at the front of [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path).

When `site_import` is non-zero, the [`site`](https://docs.python.org/3.14/library/site.html#module-site) module is permitted to alter [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path). When `user_site_directory` is non-zero and the user’s site-package directory is present, the `site` module tacks that user’s site-package directory onto `sys.path`.

These are the configuration files the path configuration draws on:

- `pyvenv.cfg`

- `._pth` file (ex: `python._pth`)

- `pybuilddir.txt` (Unix only)

Where a `._pth` file exists:

- Set `isolated` to `1`.

- Set `use_environment` to `0`.

- Set `site_import` to `0`.

- Set `safe_path` to `1`.

Where `home` is unset and a `pyvenv.cfg` file sits in the very directory as `executable`, or in its parent, `prefix` and `exec_prefix` are pointed at that location. Even so, `base_prefix` and `base_exec_prefix` hold on to their values, which still reference the base installation. Refer to [Virtual Environments](https://docs.python.org/3.14/library/sys_path_init.html#sys-path-init-virtual-environments) for further details.

The `__PYVENV_LAUNCHER__` environment variable serves to populate `PyConfig.base_executable`.

Changed in version 3.14: `prefix`, along with `exec_prefix`, now point at the `pyvenv.cfg` directory. Formerly [`site`](https://docs.python.org/3.14/library/site.html#module-site) handled this, which left it subject to [`-S`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-S).

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyconfig-home-to-pyconfig-executable.md) · [Following source contract](py-getargcargv.md)
