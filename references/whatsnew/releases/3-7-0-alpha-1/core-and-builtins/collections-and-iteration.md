# Python 3.7.0 alpha 1 / core and builtins / collections and iteration

[bpo-28120](https://bugs.python.org/issue?@action=redirect&bpo=28120): Repair dict.pop() for a split dictionary whenever it tries to remove a "pending key" (Not yet inserted in split-table). Xiang Zhang wrote the patch.

[bpo-28721](https://bugs.python.org/issue?@action=redirect&bpo=28721): Repair the asynchronous generator methods aclose() and athrow() so they propagate StopAsyncIteration correctly.

[bpo-30486](https://bugs.python.org/issue?@action=redirect&bpo=30486): Cell values for __closure__ can now be set. Lisa Roach provided the patch.

[bpo-29935](https://bugs.python.org/issue?@action=redirect&bpo=29935): The index() method of tuple, list and deque now reports better error messages when handed indices of the wrong type.

[bpo-28580](https://bugs.python.org/issue?@action=redirect&bpo=28580): Make the iteration over split table values faster. Xiang Zhang wrote the patch.

[bpo-28183](https://bugs.python.org/issue?@action=redirect&bpo=28183): Tune and tidy up dict iteration.

[bpo-28376](https://bugs.python.org/issue?@action=redirect&bpo=28376): The long range iterator's type is registered as Iterator from now on. Oren Milman wrote the patch.

[bpo-28086](https://bugs.python.org/issue?@action=redirect&bpo=28086): A single var-positional argument that was a tuple subtype used to reach the C-defined function untouched. It now gets converted into an exact tuple.

[bpo-29327](https://bugs.python.org/issue?@action=redirect&bpo=29327): A crash that happened when the iterable keyword argument is handed to sorted() was fixed.

[bpo-28991](https://bugs.python.org/issue?@action=redirect&bpo=28991): functools.lru_cache() carried an obscure reentrancy bug that a monkey-patched len() function could set off.

[bpo-31411](https://bugs.python.org/issue?@action=redirect&bpo=31411): When warnings.onceregistry isn't a dictionary, a TypeError is now raised rather than SystemError. Oren Milman provided the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
