# Python 3.7.0 alpha 4 / library / exceptions and tracebacks

[bpo-32363](https://bugs.python.org/issue?@action=redirect&bpo=32363): Have asyncio.Task.set_exception() along with set_result() raise NotImplementedError. When Task._step() and Future.__await__() are in an invalid state they now raise appropriate exceptions in place of an AssertionError.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
