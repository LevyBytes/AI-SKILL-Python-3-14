# Python 3.8.0 alpha 1 / library / inspect

[bpo-34890](https://bugs.python.org/issue?@action=redirect&bpo=34890): The functions [`inspect.iscoroutinefunction()`](https://docs.python.org/3.14/library/inspect.html#inspect.iscoroutinefunction), [`inspect.isgeneratorfunction()`](https://docs.python.org/3.14/library/inspect.html#inspect.isgeneratorfunction) and [`inspect.isasyncgenfunction()`](https://docs.python.org/3.14/library/inspect.html#inspect.isasyncgenfunction) now operate correctly alongside [`functools.partial()`](https://docs.python.org/3.14/library/functools.html#functools.partial). Pablo Galindo wrote the patch.

[bpo-34871](https://bugs.python.org/issue?@action=redirect&bpo=34871): Stopped the inspect module from polluting `sys.modules` while it parses the `__text_signature__` of a callable.

[bpo-17185](https://bugs.python.org/issue?@action=redirect&bpo=17185): Place `__signature__` onto a mock so that [`inspect`](https://docs.python.org/3.14/library/inspect.html#module-inspect) can retrieve its signature. Patch by Karthikeyan Singaravelan.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
