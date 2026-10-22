# Python 3.9.0 alpha 1 / c api / weakref

[bpo-38395](https://bugs.python.org/issue?@action=redirect&bpo=38395): Repair a crash affecting [`weakref.proxy`](https://docs.python.org/3.14/library/weakref.html#weakref.proxy) objects that stemmed from mishandled lifetimes when certain related methods run that can drop the final reference to the object the proxy points at. Pablo Galindo wrote the patch.

[bpo-38140](https://bugs.python.org/issue?@action=redirect&bpo=38140): Render the dict and weakref offsets opaque for C heap types by routing those offsets via PyMemberDef

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
