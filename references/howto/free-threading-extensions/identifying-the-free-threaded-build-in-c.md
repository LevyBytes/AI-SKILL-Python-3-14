# Identifying the Free-Threaded Build in C

### Identifying the Free-Threaded Build in C

A `Py_GIL_DISABLED` macro is published through the CPython C API: under the free-threaded build its value is `1`, while under the ordinary build it stays undefined. Reach for it whenever you want to gate code so that it executes solely on the free-threaded build:

```c
#ifdef Py_GIL_DISABLED
/* code that only runs in the free-threaded build */
#endif

```

Note

Under Windows the macro will not appear on its own; you have to pass it to the compiler yourself at build time. To find out whether the interpreter you are presently running was compiled with the macro set, call the [`sysconfig.get_config_var()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.get_config_var) function.

[Subject index](INDEX.md) · [Previous source context](c-api-extension-support-for-free-threading.md) · [Following source context](module-initialization.md)
