# Python 3.8.0 alpha 1 / core and builtins / imports and modules

[bpo-34939](https://bugs.python.org/issue?@action=redirect&bpo=34939): Permit annotated names within the module namespace when they were declared global ahead of where the annotation occurs. Patch by Pablo Galindo.

[bpo-34824](https://bugs.python.org/issue?@action=redirect&bpo=34824): Resolve a potential null pointer dereference inside Modules/_ssl.c. Patch by Zackery Spytz.

[bpo-32946](https://bugs.python.org/issue?@action=redirect&bpo=32946): Bringing names in from an already imported module using ?from ? import ?? is now 30% faster provided the module is not a package.

[bpo-33053](https://bugs.python.org/issue?@action=redirect&bpo=33053): With the -m switch, sys.path[0] is now expanded explicitly as the *starting* working directory, instead of staying as the empty path (which lets imports come from whatever the working directory happens to be at import time)

[bpo-30167](https://bugs.python.org/issue?@action=redirect&bpo=30167): `PyRun_SimpleFileExFlags` now strips `__cached__` from the module on top of `__file__`.

[bpo-32305](https://bugs.python.org/issue?@action=redirect&bpo=32305): With namespace packages, guarantee that `__file__` along with `__spec__.origin` both end up set to None.

[bpo-32303](https://bugs.python.org/issue?@action=redirect&bpo=32303): Guarantee that `__spec__.loader` agrees with `__loader__` whenever a namespace package is involved.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
