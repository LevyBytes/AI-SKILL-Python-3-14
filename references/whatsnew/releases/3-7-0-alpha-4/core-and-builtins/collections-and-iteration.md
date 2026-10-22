# Python 3.7.0 alpha 4 / core and builtins / collections and iteration

[bpo-32329](https://bugs.python.org/issue?@action=redirect&bpo=32329): When the [`PYTHONHASHSEED`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONHASHSEED) environment variable equals `0`, the [`-R`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-R) option now switches on hash randomization. The option used to be ignored. On top of that, `sys.flags.hash_randomization` is now correctly set to 0 once hash randomization gets turned off via `PYTHONHASHSEED=0`.

[bpo-20361](https://bugs.python.org/issue?@action=redirect&bpo=20361): `-b` plus `-bb` now push `'default::BytesWarning'` and `error::BytesWarning` entries onto `sys.warnoptions`, making sure they outrank any other warning filters set through the `-W` option or the `PYTHONWARNINGS` environment variable.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
