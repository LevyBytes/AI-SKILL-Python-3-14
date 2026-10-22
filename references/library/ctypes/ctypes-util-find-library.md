# ctypes — Finding shared libraries

### ctypes reference

### Finding shared libraries

In a compiled language, shared libraries come into play both while compiling or linking a program and while the program runs.

The job of the `find_library()` function is to track down a library much like the compiler or runtime loader would (on platforms carrying several versions of a shared library, the newest one ought to load), whereas the ctypes library loaders behave as a running program does and invoke the runtime loader directly.

A function that helps you figure out which library to load is provided by the `ctypes.util` module.

 ctypes.util.find_library(*name*)

Attempt to locate a library and give back a pathname. *name* is the bare library name, dropping any prefix such as *lib*, any suffix like `.so`, `.dylib`, or a version number (this matches the form the posix linker option `-l` expects). When nothing can be found, the return is `None`.

How precisely it works depends on the system.

On Linux, `find_library()` shells out to external programs (`/sbin/ldconfig`, `gcc`, `objdump`, and `ld`) to track down the library file, and it returns that file’s filename.

Keep in mind that if those programs’ output doesn’t line up with the dynamic linker Python actually uses, this function’s result might lead you astray.

Changed in version 3.6: On Linux, the `LD_LIBRARY_PATH` environment variable’s value is consulted while searching for libraries, whenever a library can’t be located by other means.

A few examples follow:

```python
>>> from ctypes.util import find_library
>>> find_library("m")
'libm.so.6'
>>> find_library("c")
'libc.so.6'
>>> find_library("bz2")
'libbz2.so.1.0'
>>>

```

On macOS and Android, `find_library()` applies the system’s standard naming conventions and search paths to find the library, returning a full pathname when it succeeds:

```python
>>> from ctypes.util import find_library
>>> find_library("c")
'/usr/lib/libc.dylib'
>>> find_library("m")
'/usr/lib/libm.dylib'
>>> find_library("bz2")
'/usr/lib/libbz2.dylib'
>>> find_library("AGL")
'/System/Library/Frameworks/AGL.framework/AGL'
>>>

```

On Windows, `find_library()` looks along the system search path and returns the full pathname; but because there’s no fixed naming scheme there, a call such as `find_library("c")` will come up empty and return `None`.

If you’re wrapping a shared library with `ctypes`, it *might* serve you better to settle on the shared library name during development and bake it into the wrapper module, rather than calling `find_library()` to find the library at runtime.

[Subject index](INDEX.md) · [Continue](listing-loaded-shared-libraries.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md)
