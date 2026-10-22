# Python 3.8.0 beta 1 / library / imports and modules

[bpo-36867](https://bugs.python.org/issue?@action=redirect&bpo=36867): A multiprocessing.resource_tracker module now stands in for multiprocessing.semaphore_tracker. Beyond semaphores, resource_tracker keeps an eye on shared_memory segments as well.

[bpo-29262](https://bugs.python.org/issue?@action=redirect&bpo=29262): Supplies `get_origin()` plus `get_args()` introspection helpers to the `typing` module.

[bpo-37058](https://bugs.python.org/issue?@action=redirect&bpo=37058): PEP 544: Brings `Protocol` and `@runtime_checkable` into the `typing` module.

[bpo-37049](https://bugs.python.org/issue?@action=redirect&bpo=37049): PEP 589: Brings `TypedDict` into the `typing` module.

[bpo-37046](https://bugs.python.org/issue?@action=redirect&bpo=37046): PEP 586: Brings `Literal` into the `typing` module.

[bpo-37045](https://bugs.python.org/issue?@action=redirect&bpo=37045): PEP 591: Brings a `Final` qualifier and a `@final` decorator into the `typing` module.

[bpo-36972](https://bugs.python.org/issue?@action=redirect&bpo=36972): Adds the SupportsIndex protocol to the typing module so a type checker can spot classes acceptable to `hex()`, `oct()` and `bin()`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
