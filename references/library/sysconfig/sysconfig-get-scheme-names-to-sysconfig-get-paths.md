# sysconfig — Installation path functions

### Installation path functions

`sysconfig` offers a handful of functions for working out these installation paths.

 sysconfig.get_scheme_names()

Yields a tuple listing every scheme `sysconfig` presently backs.

 sysconfig.get_default_scheme()

Yields the default scheme name for the platform you are on.

Added in version 3.10: This function used to go by the name `_get_default_scheme()` and was regarded as an implementation detail.

Changed in version 3.11: Whenever Python is running out of a virtual environment, the *venv* scheme comes back.

 sysconfig.get_preferred_scheme(*key*)

Yields a preferred scheme name for the installation layout that *key* picks out.

*key* has to be one of `"prefix"`, `"home"`, or `"user"`.

What comes back is a scheme name found in `get_scheme_names()`. You may feed it to any `sysconfig` function that accepts a *scheme* argument, `get_paths()` for one.

Added in version 3.10.

Changed in version 3.11: Whenever Python is running out of a virtual environment with `key="prefix"`, the *venv* scheme comes back.

 sysconfig._get_preferred_schemes()

Yields a dict of the preferred scheme names for the platform you are on. Those who implement or redistribute Python may register their own preferred schemes in the `_INSTALL_SCHEMES` module-level global and adjust this function to surface those names — for instance to hand system and language package managers separate schemes, so that packages installed by one stay clear of those installed by the other.

This function is not meant for end users; they should turn to `get_default_scheme()` and `get_preferred_scheme()` instead.

Added in version 3.10.

 sysconfig.get_path_names()

Yields a tuple listing every path name `sysconfig` presently backs.

 sysconfig.get_path(*name*[, *scheme*[, *vars*[, *expand*]]])

Yields the installation path that matches the path *name*, drawn from the install scheme called *scheme*.

*name* must be one of the values found in the list `get_path_names()` returns.

`sysconfig` retains an installation path for each path name on every platform, with variables left to be expanded. As an example, the *stdlib* path under the *nt* scheme reads: `{base}/Lib`.

To expand the path, `get_path()` draws on the variables `get_config_vars()` returns. Since every variable carries platform defaults, you can call this function and simply receive the default value.

When *scheme* is supplied, it must be one of the values listed by `get_scheme_names()`. Otherwise the default scheme for the platform you are on applies.

When *vars* is supplied, it must be a dictionary of variables that augments the dictionary `get_config_vars()` returns.

When *expand* is set to `False`, the variables are not used to expand the path.

Should *name* be absent, a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) is raised.

 sysconfig.get_paths([*scheme*[, *vars*[, *expand*]]])

Yields a dictionary holding every installation path that belongs to an installation scheme. Consult `get_path()` for further detail.

When *scheme* is left out, the default scheme for the platform you are on applies.

When *vars* is supplied, it must be a dictionary of variables that augments the dictionary used to expand the paths.

When *expand* is set to false, the paths go unexpanded.

Should *scheme* name no existing scheme, `get_paths()` raises a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError).

[Subject index](INDEX.md) · [Previous](nt.md) · [Continue](python-version-platform-and-makefile-queries.md) · [Owning module, declaration or section: sysconfig](python-configuration-access-overview.md)
