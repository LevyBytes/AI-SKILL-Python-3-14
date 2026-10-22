# Python 3.8.0 beta 1 / core and builtins / functions and types

[bpo-36027](https://bugs.python.org/issue?@action=redirect&bpo=36027): Modular inverses can now be computed with three-argument `pow`: a negative value is now accepted for the second argument provided the first and third arguments share no common factor.

[bpo-28866](https://bugs.python.org/issue?@action=redirect&bpo=28866): Skips caching the attributes of classes whose type supplies mro(), sidestepping a thorny cache invalidation problem.

[bpo-27639](https://bugs.python.org/issue?@action=redirect&bpo=27639): Fixes the return type produced by UserList slicing operations. Michael Blahay, Erick Cervantes, and vaultah wrote the patch.

[bpo-36045](https://bugs.python.org/issue?@action=redirect&bpo=36045): `builtins.help()` now puts the `async` prefix ahead of async functions.

[bpo-35983](https://bugs.python.org/issue?@action=redirect&bpo=35983): Introduces new trashcan macros that handle a double deallocation able to surface once a subclass's `tp_dealloc` invokes the `tp_dealloc` of a base class while that base class relies on the trashcan mechanism. Jeroen Demeyer wrote the patch.

[bpo-37122](https://bugs.python.org/issue?@action=redirect&bpo=37122): The *co_argcount* attribute on code objects now reports the full count of positional arguments, positional-only ones included. You can read *co_posonlyargcount* to tell which arguments are positional only, and subtracting (*co_argcount* - *co_posonlyargcount*) yields how many are positional-or-keyword. Pablo Galindo wrote the patch.

[bpo-22385](https://bugs.python.org/issue?@action=redirect&bpo=22385): The `bytes.hex`, `bytearray.hex`, and `memoryview.hex` methods, plus the `binascii.hexlify` and `b2a_hex` functions, gain the option to insert a separator between hex bytes. MicroPython’s hexlify implementation prompted this addition.

[bpo-36907](https://bugs.python.org/issue?@action=redirect&bpo=36907): Cures a crash that arose when a C function got called with a keyword dict (`f(**kwargs)`) and the dict `kwargs` was mutated mid-execution of that function.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
