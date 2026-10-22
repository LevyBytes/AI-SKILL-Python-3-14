# site — Module contents

### Module contents

 site.PREFIXES

A list of prefixes for site-packages directories.

 site.ENABLE_USER_SITE

A flag reporting the state of the user site-packages directory. A value of `True` says it is on and was placed onto `sys.path`. `False` says the user turned it off (via [`-s`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-s) or [`PYTHONNOUSERSITE`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONNOUSERSITE)). `None` says it was shut off either for security (a mismatch between the user or group id and the effective id) or by an administrator.

 site.USER_SITE

The location of the user site-packages belonging to the active Python. It may be `None` while `getusersitepackages()` has yet to be called. Its default works out to `~/.local/lib/python*X.Y*[t]/site-packages` on UNIX and non-framework macOS builds, `~/Library/Python/*X.Y*/lib/python/site-packages` on macOS framework builds, and `*%APPDATA%*\Python\Python*XY*\site-packages` under Windows. That optional “t” signals the free-threaded build. Because this is a site directory, the `.pth` files within it will be processed.

 site.USER_BASE

The location of the base directory underneath the user site-packages. It may be `None` until `getuserbase()` has been called. Its default comes to `~/.local` on UNIX and non-framework macOS builds, `~/Library/Python/*X.Y*` on macOS framework builds, and `*%APPDATA%*\Python` on Windows. From this value Python derives the install directories for scripts, data files, modules, and the like under the [user installation scheme](https://docs.python.org/3.14/library/sysconfig.html#sysconfig-user-scheme). Consult [`PYTHONUSERBASE`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONUSERBASE) as well.

 site.main()

Appends every standard site-specific directory onto the module search path. Importing this module calls the function for you automatically, except when the Python interpreter began with the [`-S`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-S) flag.

Changed in version 3.3: In the past, this function was always called, no conditions attached.

 site.addsitedir(*sitedir*, *known_paths=None*)

Place a directory onto sys.path and handle the `.pth` files inside it. This is commonly invoked from `sitecustomize` or `usercustomize` (described earlier).

 site.getsitepackages()

Hand back a list holding every global site-packages directory.

Added in version 3.2.

 site.getuserbase()

Give back the path of the user base directory, `USER_BASE`. Where it remains uninitialized, this function will initialize it too, honoring [`PYTHONUSERBASE`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONUSERBASE).

Added in version 3.2.

 site.getusersitepackages()

Give back the path of the user-specific site-packages directory, `USER_SITE`. When it has not yet been initialized, this function initializes it as well, honoring `USER_BASE`. Checking whether that user-specific site-packages made it onto `sys.path` is what `ENABLE_USER_SITE` is for.

Added in version 3.2.

[Subject index](INDEX.md) · [Previous](readline-configuration.md) · [Continue](command-line-interface.md) · [Owning module, declaration or section: site](site-site-specific-configuration-hook.md)
