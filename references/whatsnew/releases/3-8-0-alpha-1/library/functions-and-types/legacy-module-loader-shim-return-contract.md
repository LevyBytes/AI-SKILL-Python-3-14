# Python 3.8.0 alpha 1 / library / make certain loader shim built imp load module always hands back

[bpo-34056](https://bugs.python.org/issue?@action=redirect&bpo=34056): Make certain the loader shim built by `imp.load_module` always hands back bytes out of its `get_data()` function. That repairs `imp.load_module` usage with [**PEP 552**](https://peps.python.org/pep-0552/) hash-based pycs.

[Subject index](INDEX.md) · [Release version, date and status](../../release-overview/overview.md)
