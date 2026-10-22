# Python 3.9.0 alpha 1 / core and builtins / should garbage collector run pass where certain objects resurrect

[bpo-38379](https://bugs.python.org/issue?@action=redirect&bpo=38379): Should the garbage collector run a pass where certain objects resurrect ? becoming reachable from beyond the isolated cycles once finalizers complete ? it now avoids blocking the collection of every object that stays unreachable. Pablo Galindo and Tim Peters supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
