# Python 3.9.0 alpha 3 / library / logging

[bpo-39198](https://bugs.python.org/issue?@action=redirect&bpo=39198): Should an exception escape from `Logger.isEnabledFor` — for instance via asyncio timeouts or stopit — the `logging` global lock might not be freed correctly, leading to deadlock. The fix surrounds that section with `try...finally` so the lock is always released.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
