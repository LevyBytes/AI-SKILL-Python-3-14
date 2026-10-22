# Python 3.7.0 alpha 4 / library / carry out asyncio current task asyncio all tasks

[bpo-32250](https://bugs.python.org/issue?@action=redirect&bpo=32250): Carry out `asyncio.current_task()` and `asyncio.all_tasks()`. Provide helpers meant for use by alternative task implementations: `asyncio._register_task`, `asyncio._enter_task`, `asyncio._leave_task` and `asyncio._unregister_task`. Deprecate `asyncio.Task.current_task()` and `asyncio.Task.all_tasks()`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
