# weakref: `weakref.proxy()`, `weakref.getweakrefcount()`, `weakref.getweakrefs()`

weakref.proxy(*object*[, *callback*])

Hand back a proxy aimed at *object* that operates through a weak reference. This lets the proxy stand in across most contexts, sparing you the explicit dereferencing that weak reference objects demand. The object handed back has a type of either `ProxyType` or `CallableProxyType`, according to whether *object* is callable. Proxy objects are never [hashable](https://docs.python.org/3.14/glossary.html#term-hashable), whatever the referent; this dodges a host of issues stemming from their inherently mutable character and bars their use as dictionary keys. The *callback* here matches the like-named parameter of the `ref()` function.

Touching an attribute of the proxy object after the referent has been garbage collected throws [`ReferenceError`](https://docs.python.org/3.14/library/exceptions.html#ReferenceError).

Changed in version 3.8: Broadened the operator support on proxy objects to take in the matrix multiplication operators `@` and `@=`.

 weakref.getweakrefcount(*object*)

Hand back the count of weak references plus proxies pointing at *object*.

 weakref.getweakrefs(*object*)

Hand back a list of every weak reference and proxy object pointing at *object*.

[Subject index](INDEX.md) · [Previous](weakref-weak-references.md) · [Continue](weakref-weakkeydictionary-class-to-weakkeydictionary-keyrefs.md) · [Owning module, declaration or section: weakref](weakref-ref-class.md)
