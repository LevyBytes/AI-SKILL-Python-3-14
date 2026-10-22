# Python 3.10.0 beta 1 / library / sysconfig

[bpo-43312](https://bugs.python.org/issue?@action=redirect&bpo=43312): Two new helpers, [`sysconfig.get_preferred_scheme()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.get_preferred_scheme) and [`sysconfig.get_default_scheme()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.get_default_scheme), let you ask a platform which scheme name it favors for the "user", "home", and "prefix" (default) cases.

[bpo-41282](https://bugs.python.org/issue?@action=redirect&bpo=41282): The install schemes used by `distutils.command.install` now come from [`sysconfig`](https://docs.python.org/3.14/library/sysconfig.html#module-sysconfig).

[bpo-41282](https://bugs.python.org/issue?@action=redirect&bpo=41282): The `distutils.sysconfig` module was folded into [`sysconfig`](https://docs.python.org/3.14/library/sysconfig.html#module-sysconfig).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
