# Python 3.11.0 alpha 6 / core and builtins / collections and iteration

[bpo-46615](https://bugs.python.org/issue?@action=redirect&bpo=46615): While looping over sets internally inside `setobject.c`, take strong references to the items the set yields. Doing so heads off crashes in edge cases of assorted set operations where the set ends up mutated.

[bpo-46903](https://bugs.python.org/issue?@action=redirect&bpo=46903): Make str subclasses usable as attribute names on instances that have virtual dictionaries. Corrects a 3.11alpha regression

[bpo-46891](https://bugs.python.org/issue?@action=redirect&bpo=46891): Correct a 3.11alpha-era bug where subclasses of `types.ModuleType` declaring `__slots__` were not set up correctly, which crashed the interpreter.

[bpo-40116](https://bugs.python.org/issue?@action=redirect&bpo=40116): Correct a regression in which dict.update(other) might fail to honor the iteration order of other when other happens to be a key-sharing dict.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
