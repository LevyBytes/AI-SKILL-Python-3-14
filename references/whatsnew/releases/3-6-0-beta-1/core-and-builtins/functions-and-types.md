# Python 3.6.0 beta 1 / core and builtins / functions and types

[bpo-27506](https://bugs.python.org/issue?@action=redirect&bpo=27506): Allow the bytes/bytearray.translate() “delete” argument to be passed by keyword.

[bpo-27792](https://bugs.python.org/issue?@action=redirect&bpo=27792): Applying the modulo operation to `bool` and other `int` subclasses now consistently yields an `int`. Formerly the result type hinged on the inputs. Xiang Zhang wrote the patch.

[bpo-24254](https://bugs.python.org/issue?@action=redirect&bpo=24254): Have the class-definition namespace be ordered by default.

[bpo-27157](https://bugs.python.org/issue?@action=redirect&bpo=27157): Limit the one-argument form so that only type() itself accepts it. Eryk Sun and Emanuel Barry wrote the patch.

[bpo-25856](https://bugs.python.org/issue?@action=redirect&bpo=25856): For extension classes and functions the __module__ attribute is now interned. The result is more compact pickle data under protocol 4.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
