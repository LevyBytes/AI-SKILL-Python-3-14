# Python 3.10.0 alpha 3 / library / functions and types

[bpo-42345](https://bugs.python.org/issue?@action=redirect&bpo=42345): Resolve several problems with `typing.Literal` parameter processing (flattening, deduplicating, keying the cache by type). Yurii Karabas provided the patch.

[bpo-42014](https://bugs.python.org/issue?@action=redirect&bpo=42014): The `onerror` callback fired by `shutil.rmtree` now gets the right function when `os.open` fails.

[bpo-42131](https://bugs.python.org/issue?@action=redirect&bpo=42131): Implement PEP 451/spec methods on zipimport.zipimporter: find_spec(), create_module(), and exec_module().

That work likewise enables the documented deprecation of find_loader(), find_module(), and load_module().

[bpo-41877](https://bugs.python.org/issue?@action=redirect&bpo=41877): Mock objects that are not unsafe will henceforth raise an AttributeError when an attribute beginning with asert, aseert, or assrt is accessed, joining the behaviour that already applied to the prefixes assert or assret.

[bpo-41332](https://bugs.python.org/issue?@action=redirect&bpo=41332): Added missing connect_accepted_socket() method to `asyncio.AbstractEventLoop`.

[bpo-42532](https://bugs.python.org/issue?@action=redirect&bpo=42532): Drop the surprising invocation of `__bool__` triggered when a `spec_arg` argument is handed to a Mock.

[bpo-42392](https://bugs.python.org/issue?@action=redirect&bpo=42392): Drop the loop parameter from the `asyncio.subprocess` and `asyncio.tasks` functions. Yurii Karabas provided the patch.

[bpo-42392](https://bugs.python.org/issue?@action=redirect&bpo=42392): Drop the loop parameter from the `asyncio.open_connection` and `asyncio.start_server` functions. Yurii Karabas provided the patch.

[bpo-42392](https://bugs.python.org/issue?@action=redirect&bpo=42392): Drop the loop parameter from `__init__` across every `asyncio.locks` and `asyncio.Queue` class. Yurii Karabas provided the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
