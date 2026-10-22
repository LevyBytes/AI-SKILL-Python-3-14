# Python 3.7.0 alpha 4 / library / functions and types

[bpo-30050](https://bugs.python.org/issue?@action=redirect&bpo=30050): A new warn_on_full_buffer argument on signal.set_wakeup_fd lets you decide whether Python writes a warning to stderr once the wakeup fd buffer overflows.

[bpo-32272](https://bugs.python.org/issue?@action=redirect&bpo=32272): Drop the asyncio.async() function.

[bpo-32269](https://bugs.python.org/issue?@action=redirect&bpo=32269): Provide the asyncio.get_running_loop() function.

[bpo-22589](https://bugs.python.org/issue?@action=redirect&bpo=22589): The .bmp MIME type switched away from "image/x-ms-bmp" over to "image/bmp"

[bpo-32356](https://bugs.python.org/issue?@action=redirect&bpo=32356): Now idempotent, asyncio.transport.resume_reading() and pause_reading() behave consistently. A new transport.is_reading() method has been added.

[bpo-32227](https://bugs.python.org/issue?@action=redirect&bpo=32227): `functools.singledispatch` can now register implementations through type annotations.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
