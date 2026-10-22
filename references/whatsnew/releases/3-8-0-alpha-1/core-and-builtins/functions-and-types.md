# Python 3.8.0 alpha 1 / core and builtins / functions and types

[bpo-34149](https://bugs.python.org/issue?@action=redirect&bpo=34149): Correct the min and max functions so their default behavior applies when key is None.

[bpo-34125](https://bugs.python.org/issue?@action=redirect&bpo=34125): Profiling unbound built-in methods now operates correctly when `**kwargs` is supplied.

[bpo-34126](https://bugs.python.org/issue?@action=redirect&bpo=34126): Resolve crashes that arose while profiling certain invalid invocations of unbound methods. Patch by Jeroen Demeyer.

[bpo-33985](https://bugs.python.org/issue?@action=redirect&bpo=33985): Add the contextvars.ContextVar.name attribute.

[bpo-25750](https://bugs.python.org/issue?@action=redirect&bpo=25750): Resolve a rare Python crash caused by faulty refcounting inside `type_getattro()` whenever a descriptor removes itself from its class. Patch by Jeroen Demeyer.

[bpo-34653](https://bugs.python.org/issue?@action=redirect&bpo=34653): Drop the now-unused PyParser_SimpleParseStringFilename function.

[bpo-34641](https://bugs.python.org/issue?@action=redirect&bpo=34641): Tighten further the grammar permitted on the left-hand side of keyword arguments within function calls. Notably, `f((keyword)=arg)` is now rejected.

[bpo-34637](https://bugs.python.org/issue?@action=redirect&bpo=34637): Expose the *start* argument of *sum()* so it is usable as a keyword argument.

[bpo-33073](https://bugs.python.org/issue?@action=redirect&bpo=33073): Gave ints an as_integer_ratio method so they interoperate more readily with floats.

[bpo-33176](https://bugs.python.org/issue?@action=redirect&bpo=33176): Give memoryviews a `toreadonly()` method.

[bpo-33205](https://bugs.python.org/issue?@action=redirect&bpo=33205): Switch the dict growth function from `round_up_to_power_2(used*2+hashtable_size/2)` to `round_up_to_power_2(used*3)`. Formerly a dict was shrunk only where `used == 0`. A dict now stands a better chance of being shrunk.

[bpo-33018](https://bugs.python.org/issue?@action=redirect&bpo=33018): Make the errors thrown by `issubclass()` more consistent when its first argument is a non-class while its second argument is an abstract base class. Patch by Josh Bronson.

[bpo-1617161](https://bugs.python.org/issue?@action=redirect&bpo=1617161): The hash of `BuiltinMethodType` instances (the methods of built-in classes) now derives from the hash of the *__self__* identity rather than its value. For `ModuleType` and `MethodWrapperType` instances (methods of user-defined classes plus some methods of built-in classes like `str.__add__`), both hash and equality now derive from the hash and equality of the *__self__* identity rather than its value. `MethodWrapperType` instances no longer support ordering.

[bpo-33509](https://bugs.python.org/issue?@action=redirect&bpo=33509): Correct the module_globals parameter of warnings.warn_explicit(): avoid a crash whenever module_globals is something other than a dict.

[bpo-33363](https://bugs.python.org/issue?@action=redirect&bpo=33363): Throw a SyntaxError for any `async with` and `async for` statement that sits outside an async function.

[bpo-25862](https://bugs.python.org/issue?@action=redirect&bpo=25862): Resolved assertion failures within the `tell()` method belonging to `io.TextIOWrapper`. Patch by Zackery Spytz.

[bpo-31577](https://bugs.python.org/issue?@action=redirect&bpo=31577): Resolved a crash in `os.utime()` that occurred with a bad ns argument. Patch by Oren Milman.

[bpo-35504](https://bugs.python.org/issue?@action=redirect&bpo=35504): Repaired a SystemError raised when the characters_written attribute of an OSError gets deleted.

[bpo-35444](https://bugs.python.org/issue?@action=redirect&bpo=35444): Repaired error handling in pickling methods when the builtin "getattr" fails to be looked up. Made pickling iterators faster.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
