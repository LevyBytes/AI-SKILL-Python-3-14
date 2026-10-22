# Python 3.11.0 beta 1 / library / functions and types

[gh-92210](https://github.com/python/cpython/issues/92210): Move `socket.__init__` over to Argument Clinic. Cinder authored the patch.

[gh-85984](https://github.com/python/cpython/issues/85984): A new function os.login_tty() is available for Unix.

[gh-91231](https://github.com/python/cpython/issues/91231): Give the `multiprocessing.BaseManager` constructor an optional keyword *shutdown_timeout* parameter. Should terminate() exceed the timeout, the process is killed. Victor Stinner authored the patch.

[bpo-46547](https://bugs.python.org/issue?@action=redirect&bpo=46547): Stop variables from leaking into the `pydoc.Helper` class namespace.

[bpo-43827](https://bugs.python.org/issue?@action=redirect&bpo=43827): Every positional-or-keyword parameter of `ABCMeta.__new__` has become positional-only, sidestepping clashes with keyword arguments that are meant to flow through to `__init_subclass__()`.

[bpo-47211](https://bugs.python.org/issue?@action=redirect&bpo=47211): Delete the undocumented and nonfunctional `re.template()` function plus the `re.TEMPLATE` flag. That removal was undone later in 3.11.0b2 and a deprecation was applied instead.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
