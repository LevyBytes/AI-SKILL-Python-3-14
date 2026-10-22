# Python 3.11.0 alpha 2 / core and builtins / memory and lifetimes

[bpo-45340](https://bugs.python.org/issue?@action=redirect&bpo=45340): An array, rather than a dictionary, now holds object attributes. The dictionary belonging to an object is built lazily, only once it is required. This cuts the memory footprint of an ordinary Python object by roughly 30%. Mark Shannon wrote the patch.

[bpo-45385](https://bugs.python.org/issue?@action=redirect&bpo=45385): Repair a reference leak originating in descr_check. Donghee Na wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
