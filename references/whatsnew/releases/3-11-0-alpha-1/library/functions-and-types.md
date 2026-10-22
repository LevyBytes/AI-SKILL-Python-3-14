# Python 3.11.0 alpha 1 / library / functions and types

[bpo-44353](https://bugs.python.org/issue?@action=redirect&bpo=44353): `typing.NewType` was reworked from a plain function into a callable class. Yurii Karabas supplied the patch.

[bpo-38371](https://bugs.python.org/issue?@action=redirect&bpo=38371): Eliminated the deprecated `split()` method on `_tkinter.TkappType`. Erlend E. Aasland authored this patch.

[bpo-44356](https://bugs.python.org/issue?@action=redirect&bpo=44356): [Enum] Allow multiple data-type mixins if they are all the same.

[bpo-44524](https://bugs.python.org/issue?@action=redirect&bpo=44524): Closed an issue under which the `__name__` and `__qualname__` attributes belonging to subscribed specialforms could come out as `None`.

[bpo-44793](https://bugs.python.org/issue?@action=redirect&bpo=44793): Corrected the argument-count check performed while subscribing a generic type that takes a `ParamSpec` parameter.

[bpo-44150](https://bugs.python.org/issue?@action=redirect&bpo=44150): Add optional *weights* argument to statistics.fmean().

[bpo-44077](https://bugs.python.org/issue?@action=redirect&bpo=44077): The type of service (ToS), otherwise known as differentiated services (DS), otherwise known as differentiated services code point (DSCP), plus explicit congestion notification (ECN) IP header fields can now be received through `socket.IP_RECVTOS`.

[bpo-45238](https://bugs.python.org/issue?@action=redirect&bpo=45238): Corrected `unittest.IsolatedAsyncioTestCase.debug()` so that coroutine-based methods and their callbacks now execute.

[bpo-45225](https://bugs.python.org/issue?@action=redirect&bpo=45225): Switched capwords over to the map function rather than a genexpr.

[bpo-45121](https://bugs.python.org/issue?@action=redirect&bpo=45121): Resolve the case where `Protocol.__init__` throws `RecursionError` upon a direct call or one through `super()`. Yurii Karabas supplied the patch.

[bpo-44019](https://bugs.python.org/issue?@action=redirect&bpo=44019): Introduced a fresh function `operator.call`, defined so that `operator.call(obj, *args, **kwargs) == obj(*args, **kwargs)`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
