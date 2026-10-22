# Declaration utilities

### Declaration utilities

You can put the macros below to work in declarations. They prove most valuable when defining the C API itself, while offering extension authors limited use. The bulk of them expand into compiler-specific renderings of widespread extensions to the C language.

 Py_ALWAYS_INLINE

Request that the compiler always inline a static inline function. The compiler is free to disregard the request and choose not to inline it.

Maps to the `always_inline` attribute under GCC and to `__forceinline` under MSVC.

You can apply it to inline performance critical static inline functions while compiling Python in debug mode with function inlining switched off. MSC, for example, turns off function inlining when building in debug mode.

Slapping Py_ALWAYS_INLINE onto a static inline function without thought can backfire into worse performance (because of larger code size, for one). For the cost/benefit tradeoff, the compiler tends to outsmart the developer.

When Python has been [built in debug mode](https://docs.python.org/3.14/using/configure.html#debug-build) (when the `Py_DEBUG` macro is defined), the `Py_ALWAYS_INLINE` macro does nothing at all.

You have to place it ahead of the function return type. Usage:

```c
static inline Py_ALWAYS_INLINE int random(void) { return 4; }

```

Added in version 3.11.

 Py_NO_INLINE

Turns off inlining for a function. One benefit, for instance, is trimming C stack usage: handy on LTO+PGO builds that inline code aggressively (see [bpo-33720](https://bugs.python.org/issue?@action=redirect&bpo=33720)).

Maps to the `noinline` attribute/specification under GCC and MSVC.

Usage:

```c
Py_NO_INLINE static int random(void) { return 4; }

```

Added in version 3.11.

 Py_DEPRECATED(version)

Reach for this to mark APIs that became deprecated as of a particular CPython version. You have to position the macro ahead of the symbol name.

Example:

```c
Py_DEPRECATED(3.8) PyAPI_FUNC(int) Py_OldFunction(void);

```

Changed in version 3.8: MSVC support was added.

 Py_LOCAL(type)

Declares a function whose return is the given *type*, applying a fast-calling qualifier meant for functions confined to the current file. In meaning, this matches `static *type*`.

 Py_LOCAL_INLINE(type)

Matches `Py_LOCAL`, but on top of that asks for the function to be inlined.

 Py_LOCAL_SYMBOL

A macro for marking a symbol as local (hidden) to the shared library. Where the platform supports it, the symbol is kept from being exported.

Under compatible GCC/Clang versions, it expands to `__attribute__((visibility("hidden")))`.

 Py_EXPORTED_SYMBOL

A macro for marking a symbol (either function or data) as exported. Under Windows this expands to `__declspec(dllexport)`. Under compatible GCC/Clang versions it expands to `__attribute__((visibility("default")))`. This macro exists for defining the C API itself; extension modules ought not to use it.

 Py_IMPORTED_SYMBOL

A macro for marking a symbol as imported. Under Windows this expands to `__declspec(dllimport)`. This macro exists for defining the C API itself; extension modules ought not to use it.

 PyAPI_FUNC(type)

A macro CPython relies on to mark a function as belonging to the C API. How it expands hinges on the platform and the build configuration. The intent behind this macro is defining CPython's own C API; extension modules ought not to apply it to their own symbols.

 PyAPI_DATA(type)

A macro CPython relies on to mark a public global variable as belonging to the C API. How it expands hinges on the platform and the build configuration. The intent behind this macro is defining CPython's own C API; extension modules ought not to apply it to their own symbols.

[Subject index](INDEX.md) · [Previous source contract](py-force-expansion-to-py-stringify.md) · [Following source contract](py-aligned-to-py-va-copy.md)
