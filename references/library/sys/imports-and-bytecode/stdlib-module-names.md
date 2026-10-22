# sys.stdlib_module_names

sys.stdlib_module_names

A frozenset of strings holding the names of the standard library modules.

It stays identical from one platform to the next. Modules absent on certain platforms, plus modules switched off at Python build time, appear here too. Every flavor of module is covered: pure Python, built-in, frozen and extension modules. Test modules are left out.

Where packages are concerned, only the top-level package shows up; sub-packages and sub-modules do not. The `email` package, for instance, is listed, whereas the `email.mime` sub-package and the `email.message` sub-module are not.

Refer as well to the `sys.builtin_module_names` list.

Added in version 3.10.

[API family](INDEX.md) · [sys context index](../INDEX.md).
