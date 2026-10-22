# Python 3.8.0 alpha 3 / library / collections and iteration

[bpo-36235](https://bugs.python.org/issue?@action=redirect&bpo=36235): Repair `CFLAGS` within `customize_compiler()` of `distutils.sysconfig`: whenever the `CFLAGS` environment variable is set, stop overriding the `CFLAGS` variable using the `OPT` variable. David Malcolm authored the initial patch.

[bpo-36091](https://bugs.python.org/issue?@action=redirect&bpo=36091): Tidy up the reference to an async generator within Lib/types. Henry Chen wrote the patch.

[bpo-30670](https://bugs.python.org/issue?@action=redirect&bpo=30670): A new `pprint.pp` helper now pretty-prints objects while keeping dictionary keys in their insertion order by default. A *sort_dicts* parameter joins `pprint.pprint`, `pprint.pformat` and `pprint.PrettyPrinter`. Rémi Lapeyre contributed this.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
