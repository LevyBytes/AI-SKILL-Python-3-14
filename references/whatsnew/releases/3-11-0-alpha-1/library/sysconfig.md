# Python 3.11.0 alpha 1 / library / sysconfig

[bpo-44351](https://bugs.python.org/issue?@action=redirect&bpo=44351): `parse_makefile()` was restored to `distutils.sysconfig` since it acts differently from the comparable implementation found in [`sysconfig`](https://docs.python.org/3.14/library/sysconfig.html#module-sysconfig).

[bpo-44860](https://bugs.python.org/issue?@action=redirect&bpo=44860): Fixed the `posix_user` scheme within [`sysconfig`](https://docs.python.org/3.14/library/sysconfig.html#module-sysconfig) so it no longer hinges on [`sys.platlibdir`](https://docs.python.org/3.14/library/sys.html#sys.platlibdir).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
