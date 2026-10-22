# Python 3.9.0 alpha 1 / core and builtins / collections and iteration

[bpo-37219](https://bugs.python.org/issue?@action=redirect&bpo=37219): Took out a mistaken optimization applied to empty set differences.

[bpo-8425](https://bugs.python.org/issue?@action=redirect&bpo=8425): Made set difference_update faster for the situation where the other set vastly exceeds the base set in size. Evgeny Kapun suggested it, and Michele Orr? contributed the code.

[bpo-27575](https://bugs.python.org/issue?@action=redirect&bpo=27575): David Su contributed a speedup for dictview intersection by applying set intersection logic directly.

[bpo-38210](https://bugs.python.org/issue?@action=redirect&bpo=38210): Dropped a redundant intersection plus update set operation performed on a dictview against an empty set. Donghee Na landed this in [bpo-38210](https://bugs.python.org/issue?@action=redirect&bpo=38210).

[bpo-11410](https://bugs.python.org/issue?@action=redirect&bpo=11410): Finer control over symbol visibility now comes from the visibility attributes offered in gcc >= 4.0, delivered consistently on both POSIX and Windows. The POSIX build files now compile using -fvisibility=hidden, which trims the set of exported symbols.

[bpo-38613](https://bugs.python.org/issue?@action=redirect&bpo=38613): Tuned several set operations (such as `|`, `^`, and `-`) on `dict_keys`. `d.keys() | other` used to lag behind `set(d) | other`, yet the two now perform at nearly the same speed.

[bpo-37648](https://bugs.python.org/issue?@action=redirect&bpo=37648): Corrected a small inconsistency across `list.__contains__()`, `tuple.__contains__()` and several other spots. From now on the collection's item sits on the left while the needle stays on the right of `==`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
