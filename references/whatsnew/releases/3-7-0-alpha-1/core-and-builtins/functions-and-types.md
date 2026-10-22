# Python 3.7.0 alpha 1 / core and builtins / functions and types

[bpo-26182](https://bugs.python.org/issue?@action=redirect&bpo=26182): Emit DeprecationWarning whenever the async and await keywords serve as a variable/attribute/class/function name.

[bpo-26110](https://bugs.python.org/issue?@action=redirect&bpo=26110): Accelerate method calls by adding the LOAD_METHOD and CALL_METHOD opcodes.

[bpo-31071](https://bugs.python.org/issue?@action=redirect&bpo=31071): Stop masking the original TypeError during a call using * unpacking when further arguments are supplied.

[bpo-25794](https://bugs.python.org/issue?@action=redirect&bpo=25794): For attribute names that aren't interned, type.__setattr__() and type.__delattr__() were fixed. Eryk Sun contributed the underlying patch.

[bpo-29914](https://bugs.python.org/issue?@action=redirect&bpo=29914): The default __reduce__ and __reduce_ex__() implementations were fixed. object.__reduce__() now accepts no arguments, while object.__reduce_ex__() now demands a single argument.

[bpo-12844](https://bugs.python.org/issue?@action=redirect&bpo=12844): A function may now receive a count of arguments exceeding 255.

[bpo-27100](https://bugs.python.org/issue?@action=redirect&bpo=27100): A with-statement now looks for __enter__ ahead of looking for __exit__, which yields clearer error messages whenever both of those methods are absent. Jonathan Ellington supplied the patch.

[bpo-28376](https://bugs.python.org/issue?@action=redirect&bpo=28376): Building range_iterator instances by invoking the range_iterator type is now forbidden. The sole supported route is to call iter() on a range instance. Oren Milman wrote the patch.

[bpo-26906](https://bugs.python.org/issue?@action=redirect&bpo=26906): Looking up the special methods of an uninitialized type now triggers that type's implicit initialization rather than failing.

[bpo-28289](https://bugs.python.org/issue?@action=redirect&bpo=28289): ImportError.__init__ now clears any attributes that were not specified.

[bpo-28214](https://bugs.python.org/issue?@action=redirect&bpo=28214): __set_name__ is now resolved on the class rather than on the instance.

[bpo-29602](https://bugs.python.org/issue?@action=redirect&bpo=29602): Signed-zero mishandling in the complex constructor was fixed for complex subclasses and for inputs carrying a __complex__ method. Serhiy Storchaka provided the patch.

[bpo-29049](https://bugs.python.org/issue?@action=redirect&bpo=29049): Invoke _PyObject_GC_TRACK() lazily during calls to a Python function. The calling of a function runs up to 5% quicker.

[bpo-18896](https://bugs.python.org/issue?@action=redirect&bpo=18896): A Python function may now take more than 255 parameters. collections.namedtuple() now handles tuples holding more than 255 elements.

[bpo-28512](https://bugs.python.org/issue?@action=redirect&bpo=28512): Setting the offset attribute of SyntaxError through PyErr_SyntaxLocationEx() and PyErr_SyntaxLocationObject() was fixed.

[bpo-23722](https://bugs.python.org/issue?@action=redirect&bpo=23722): In place of quietly yielding a class whose methods can't use zero-argument `super()`, a failure to forward the new `__classcell__` namespace entry up to `type.__new__` now produces a `DeprecationWarning` along with a class that does support zero-argument `super()`.

[bpo-28797](https://bugs.python.org/issue?@action=redirect&bpo=28797): Altering the class __dict__ from inside the __set_name__ method of a descriptor used within that very class no longer stops the __set_name__ method of the remaining descriptors from being called.

[bpo-31271](https://bugs.python.org/issue?@action=redirect&bpo=31271): An assertion failure in the `write()` method of `io.TextIOWrapper` was fixed for when the encoder hands back something that isn't a bytes object. Oren Milman provided the patch.

[bpo-31243](https://bugs.python.org/issue?@action=redirect&bpo=31243): A crash in several `io.TextIOWrapper` methods was fixed for the case where the decoder's state is invalid. Oren Milman provided the patch.

[bpo-31095](https://bugs.python.org/issue?@action=redirect&bpo=31095): Fix a potential GC crash brought on by a `tp_dealloc` that neglects to call `PyObject_GC_UnTrack()`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
