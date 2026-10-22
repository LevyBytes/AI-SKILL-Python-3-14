# sys.getobjects

sys.getobjects(*limit*[, *type*])

This function is present only when CPython was compiled with the special configure option [`--with-trace-refs`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-trace-refs). Its sole purpose is debugging garbage-collection problems.

Hand back a list of as many as *limit* dynamically allocated Python objects. When *type* is supplied, only objects of precisely that type (not subtypes) appear.

The objects in the list are not safe to touch. In particular, the result will pull in objects from every interpreter sharing object allocator state (namely, those created with [`PyInterpreterConfig.use_main_obmalloc`](https://docs.python.org/3.14/c-api/subinterpreters.html#c.PyInterpreterConfig.use_main_obmalloc) set to 1 or built through [`Py_NewInterpreter()`](https://docs.python.org/3.14/c-api/subinterpreters.html#c.Py_NewInterpreter), plus the [main interpreter](https://docs.python.org/3.14/c-api/subinterpreters.html#sub-interpreter-support)). Combining objects drawn from separate interpreters can trigger crashes or other surprising behavior.

**CPython implementation detail:** Limit this function to specialized purposes alone. There is no guarantee that it exists across all Python implementations.

Changed in version 3.14: Objects belonging to other interpreters can now show up in the result.

[API family](INDEX.md) · [sys context index](../INDEX.md).
