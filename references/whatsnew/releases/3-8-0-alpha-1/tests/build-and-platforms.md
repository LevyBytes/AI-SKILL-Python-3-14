# Python 3.8.0 alpha 1 / tests / build and platforms

[bpo-32517](https://bugs.python.org/issue?@action=redirect&bpo=32517): Repair a `test_asyncio` failure under macOS 10.12.2+ stemming from the `KqueueSelector` loop transport not getting closed.

[bpo-32710](https://bugs.python.org/issue?@action=redirect&bpo=32710): `test_asyncio/test_sendfile.py` now restores the event loop policy through `tearDownModule()`, matching what other tests do, which prevents a warning while running the tests on Windows.

[bpo-33725](https://bugs.python.org/issue?@action=redirect&bpo=33725): test_multiprocessing_fork can crash on newer macOS releases. Skip the test on macOS until that issue gets sorted out.

[bpo-21263](https://bugs.python.org/issue?@action=redirect&bpo=21263): Following multiple reports that test_gdb misbehaves on macOS, and given that gdb no longer ships by default, test_gdb is now bypassed on macOS whenever LLVM Clang was used to build Python. Patch by Lysandros Nikolaou

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
