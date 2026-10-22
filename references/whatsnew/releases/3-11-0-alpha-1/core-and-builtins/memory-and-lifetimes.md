# Python 3.11.0 alpha 1 / core and builtins / memory and lifetimes

[bpo-44553](https://bugs.python.org/issue?@action=redirect&bpo=44553): Added GC methods to `types.Union` so reference cycles get broken and memory leaks are avoided.

[bpo-45061](https://bugs.python.org/issue?@action=redirect&bpo=45061): Give the bool type a deallocator that catches refcount bugs in C extensions that mistakenly call Py_DECREF(Py_True) or Py_DECREF(Py_False). It likewise catches refcount bugs whenever the empty tuple singleton or the Unicode empty string singleton gets destroyed by accident. Victor Stinner contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
