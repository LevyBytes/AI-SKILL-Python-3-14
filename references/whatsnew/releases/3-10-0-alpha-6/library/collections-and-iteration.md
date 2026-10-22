# Python 3.10.0 alpha 6 / library / collections and iteration

[bpo-43102](https://bugs.python.org/issue?@action=redirect&bpo=43102): On the namedtuple __new__ method, __builtins__ had been assigned None rather than a real dictionary. Introspection tooling ran into trouble because of that.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
