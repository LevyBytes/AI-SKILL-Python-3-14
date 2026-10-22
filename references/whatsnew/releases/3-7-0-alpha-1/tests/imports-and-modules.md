# Python 3.7.0 alpha 1 / tests / imports and modules

[bpo-30695](https://bugs.python.org/issue?@action=redirect&bpo=30695): Introduce the `set_nomemory(start, stop)` and `remove_mem_hooks()` helpers within the `_testcapi` module.

[bpo-30197](https://bugs.python.org/issue?@action=redirect&bpo=30197): Improved the swap_attr() and swap_item() helpers found in the test.support module. They now behave correctly when you delete the substituted attribute or item from inside the with statement. Whenever an “as” clause is present, its target now receives the prior value of the attribute or item (or None when no such value existed).

[bpo-28217](https://bugs.python.org/issue?@action=redirect&bpo=28217): Introduces the _testconsole module so console input can be tested.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
