# Python 3.9.0 beta 1 / library / functions and types

[bpo-40286](https://bugs.python.org/issue?@action=redirect&bpo=40286): The C-coded `randbytes()`, namely `_random.Random.randbytes()`, was dropped. Recoding the method in Python makes subclassing simpler, since `randbytes()` at this point leans straight on `getrandbits()`.

[bpo-40389](https://bugs.python.org/issue?@action=redirect&bpo=40389): For a `typing.Union` built from two types where one of them is `NoneType`, `repr()` at this point yields `typing.Optional[T]`.

[bpo-31033](https://bugs.python.org/issue?@action=redirect&bpo=31033): Give `Future.cancel()` and `Task.cancel()` a `msg` argument.

[bpo-40541](https://bugs.python.org/issue?@action=redirect&bpo=40541): Gave random.sample() an optional *counts* parameter.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
