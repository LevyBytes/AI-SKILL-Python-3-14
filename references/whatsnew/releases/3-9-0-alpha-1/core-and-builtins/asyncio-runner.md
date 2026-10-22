# Python 3.9.0 alpha 1 / core and builtins / asyncio runner

[bpo-38013](https://bugs.python.org/issue?@action=redirect&bpo=38013): Permit invoking `async_generator_athrow().throw(...)` on an async generator helper that has not yet started. This clears up a nagging warning emitted as an [`asyncio.run()`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.run) call concludes.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
