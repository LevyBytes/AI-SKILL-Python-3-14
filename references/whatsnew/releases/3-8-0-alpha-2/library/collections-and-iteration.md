# Python 3.8.0 alpha 2 / library / collections and iteration

[bpo-35321](https://bugs.python.org/issue?@action=redirect&bpo=35321): Set `__spec__.origin` on `_frozen_importlib` to frozen so it lines up with how `_frozen_importlib_external` behaves. Patch by Nina Zakharenko.

[bpo-35378](https://bugs.python.org/issue?@action=redirect&bpo=35378): Repair a reference problem within `multiprocessing.Pool` that kept the pool alive whenever it was deleted without an explicit close or terminate. A fresh strong reference now ties the pool iterators to the pool, binding the pool's lifetime to that of its iterators, so the pool survives as long as any pool iterator remains alive.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
