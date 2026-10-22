# Python 3.8.0 alpha 1 / core and builtins / dis

[bpo-33041](https://bugs.python.org/issue?@action=redirect&bpo=33041): Introduced the new opcode [`END_ASYNC_FOR`](https://docs.python.org/3.14/library/dis.html#opcode-END_ASYNC_FOR) and resolves the issues listed below:

  - Setting a global [`StopAsyncIteration`](https://docs.python.org/3.14/library/exceptions.html#StopAsyncIteration) no longer disrupts `async for` loops.

  - Jumping into an `async for` loop is now blocked.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
