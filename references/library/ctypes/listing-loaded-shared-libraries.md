# ctypes — Listing loaded shared libraries

### Listing loaded shared libraries

When you’re writing code that depends on functionality pulled in from shared libraries, knowing which shared libraries are already loaded in the current process can come in handy.

For that, the `ctypes.util` module supplies the `dllist()` function, which invokes the assorted APIs offered by the different platforms to figure out which shared libraries have already been loaded into the current process.

Exactly what this function prints varies by system. On the majority of platforms, the list’s first entry stands for the current process itself and may be an empty string. As an example, on glibc-based Linux the result might look like this:

```python
>>> from ctypes.util import dllist
>>> dllist()
['', 'linux-vdso.so.1', '/lib/x86_64-linux-gnu/libm.so.6', '/lib/x86_64-linux-gnu/libc.so.6', ... ]

```

[Subject index](INDEX.md) · [Previous](ctypes-util-find-library.md) · [Continue](ctypes-cdll-class.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md)
