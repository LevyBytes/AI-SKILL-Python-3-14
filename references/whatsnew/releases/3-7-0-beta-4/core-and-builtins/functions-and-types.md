# Python 3.7.0 beta 4 / core and builtins / functions and types

[bpo-33363](https://bugs.python.org/issue?@action=redirect&bpo=33363): Raise a SyntaxError when `async with` and `async for` statements appear outside of async functions.

[bpo-33205](https://bugs.python.org/issue?@action=redirect&bpo=33205): Switch the dict growth function from `round_up_to_power_2(used*2+hashtable_size/2)` to `round_up_to_power_2(used*3)`. Formerly a dict shrank only when `used == 0`. The dict now has a greater opportunity to be shrunk.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
